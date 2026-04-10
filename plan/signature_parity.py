#!/usr/bin/env python3
"""
Tina4 Signature Parity Analyser

Extracts typed method signatures from all 4 frameworks, normalises names
to snake_case, groups equivalent methods, and flags mismatches in:
  - parameter names / types / defaults
  - return types
  - missing methods per framework

Output: SIGNATURE-PARITY.md
"""

import ast
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import date

BASE = Path("/Users/andrevanzuydam/IdeaProjects")

def split_params(params_raw: str) -> list:
    """Split a parameter string on commas, respecting angle-bracket depth (TypeScript generics)."""
    parts = []
    depth = 0
    current = []
    for ch in params_raw:
        if ch in ('<', '[', '('):
            depth += 1
            current.append(ch)
        elif ch in ('>', ']', ')'):
            depth = max(0, depth - 1)
            current.append(ch)
        elif ch == ',' and depth == 0:
            part = ''.join(current).strip()
            if part:
                parts.append(part)
            current = []
        else:
            current.append(ch)
    part = ''.join(current).strip()
    if part:
        parts.append(part)
    return parts

# ── Name normalisation ────────────────────────────────────────────────────────

def to_snake(name):
    """Convert camelCase / PascalCase to snake_case for comparison."""
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    return s.lower().strip('?!_')

# ── Python extraction (AST, full type info) ───────────────────────────────────

def py_param(arg, defaults, offset, kwdefaults=None):
    annotation = ""
    if arg.annotation:
        try:
            annotation = ": " + ast.unparse(arg.annotation)
        except Exception:
            pass
    default = ""
    di = offset
    if di >= 0 and di < len(defaults):
        try:
            default = " = " + ast.unparse(defaults[di])
        except Exception:
            pass
    return f"{arg.arg}{annotation}{default}"

def extract_python_signatures(filepath):
    """Return {class_name: {method_name: {params, returns}}}"""
    src = Path(filepath).read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {}
    result = {}

    def _extract_func_params(item):
        args = item.args
        all_args = args.posonlyargs + args.args
        defaults_offset = len(all_args) - len(args.defaults)
        params = []
        for i, arg in enumerate(all_args):
            if arg.arg in ("self", "cls"):
                continue
            params.append(py_param(arg, args.defaults, i - defaults_offset))
        if args.vararg:
            params.append(f"*{args.vararg.arg}")
        for i, kwarg in enumerate(args.kwonlyargs):
            kd = args.kw_defaults[i]
            ann = f": {ast.unparse(kwarg.annotation)}" if kwarg.annotation else ""
            dflt = f" = {ast.unparse(kd)}" if kd else ""
            params.append(f"{kwarg.arg}{ann}{dflt}")
        if args.kwarg:
            params.append(f"**{args.kwarg.arg}")
        returns = ""
        if item.returns:
            try:
                returns = ast.unparse(item.returns)
            except Exception:
                pass
        return params, returns

    # Class-level methods
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name.startswith("_"):
            continue
        methods = {}
        for item in node.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            name = item.name
            if name.startswith("_") or name == "__init__":
                continue
            params, returns = _extract_func_params(item)
            is_async = isinstance(item, ast.AsyncFunctionDef)
            methods[name] = {"params": params, "returns": returns, "async": is_async}
        if methods:
            result[node.name] = methods

    # Module-level functions (not nested inside a class)
    module_fns = {}
    class_names_in_file = {node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)}
    for node in tree.body:  # only top-level
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        name = node.name
        if name.startswith("_") or name in class_names_in_file:
            continue
        params, returns = _extract_func_params(node)
        is_async = isinstance(node, ast.AsyncFunctionDef)
        module_fns[name] = {"params": params, "returns": returns, "async": is_async}

    if module_fns:
        stem = Path(filepath).stem
        synthetic = stem.capitalize()
        if synthetic not in result:
            result[synthetic] = {}
        for fname, fdata in module_fns.items():
            if fname not in result[synthetic]:
                result[synthetic][fname] = fdata

    return result

# ── PHP extraction (regex, type hints) ───────────────────────────────────────

def extract_php_signatures(filepath):
    src = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    result = {}
    # Find all class declarations and their positions
    class_decl = re.compile(r'(?:^|\n)(?:abstract\s+)?class\s+(\w+)')
    class_positions = [(m.group(1), m.end()) for m in class_decl.finditer(src)]
    if not class_positions:
        return result
    # Assign each method to the class it falls under
    method_pattern = re.compile(
        r'public(?:\s+static)?\s+function\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*([\w\\|?\[\]<>, ]+))?',
        re.MULTILINE
    )
    def _class_for_pos(pos):
        owner = class_positions[0][0]
        for name, cpos in class_positions:
            if cpos <= pos:
                owner = name
        return owner
    # Pre-build a list of @return docblock positions for quick lookup.
    # Capture the type token only — stop before description words (space after type).
    # Handles: bool, ?array, string[], array<string, mixed>, array<int,mixed>|null, etc.
    docblock_return = re.compile(r'@return\s+((?:[\w\\?|]+|<[^>]*>|\[\])+)')
    docblock_returns = [(m.start(), m.end(), m.group(1).strip()) for m in docblock_return.finditer(src)]

    def _docblock_return_for(method_pos):
        """Return the @return type from the docblock immediately before method_pos, or ''."""
        # Find the last docblock that ends before this method (within 200 chars)
        for start, end, ret_type in reversed(docblock_returns):
            if end <= method_pos and (method_pos - end) < 200:
                return ret_type
        return ""

    classes = defaultdict(dict)
    for m in method_pattern.finditer(src):
        name, params_raw, ret = m.group(1), m.group(2), (m.group(3) or "").strip()
        if name == "__construct" or name.startswith("__"):
            continue
        owner = _class_for_pos(m.start())
        # Prefer @return docblock over native return type (it carries generics)
        doc_ret = _docblock_return_for(m.start())
        if doc_ret:
            ret = doc_ret
        params = []
        for p in params_raw.split(","):
            p = p.strip()
            if not p:
                continue
            parts = p.split()
            # Handle reference params like &$instances and variadic like ...$args
            var_part = next((x for x in reversed(parts) if x.startswith("$") or x.startswith("&$") or x.startswith("...$")), None)
            if not var_part:
                continue
            is_variadic = var_part.startswith("...$") or "...$" in var_part
            var_part = var_part.lstrip("&").lstrip("...")
            type_parts = [x for x in parts if not x.startswith("$") and not x.startswith("...") and "=" not in x]
            type_hint = " ".join(type_parts) if type_parts else ""
            default_match = re.search(r'=\s*(.+)$', p)
            default = " = " + default_match.group(1).strip() if default_match else ""
            name_clean = var_part.lstrip("$")
            ann = f": {type_hint}" if type_hint else ""
            prefix = "*" if is_variadic else ""
            params.append(f"{prefix}{name_clean}{ann}{default}")
        classes[owner][name] = {"params": params, "returns": ret, "async": False}
    for cls, methods in classes.items():
        if methods:
            result[cls] = methods

    # Module-level PHP functions (outside any class), e.g. mcp_tool(), mcp_resource()
    # Build precise class body ranges to exclude
    php_class_ranges: list[tuple[int,int]] = []
    class_open_pattern = re.compile(r'(?:^|\n)(?:abstract\s+)?class\s+\w+[^{]*\{', re.MULTILINE)
    for cm in class_open_pattern.finditer(src):
        brace_pos = cm.end() - 1
        depth = 0
        j = brace_pos
        while j < len(src):
            if src[j] == '{':
                depth += 1
            elif src[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        php_class_ranges.append((brace_pos, j))

    def _php_outside_class(pos: int) -> bool:
        return not any(s <= pos <= e for s, e in php_class_ranges)

    php_fn_pattern = re.compile(
        r'^function\s+([a-z]\w*)\s*\(([^)]*)\)\s*(?::\s*([\w\\|?\[\]<>, ]+))?',
        re.MULTILINE
    )
    module_fns_php = {}
    for m in php_fn_pattern.finditer(src):
        if not _php_outside_class(m.start()):
            continue
        fn_name = m.group(1)
        if fn_name.startswith("_"):
            continue
        params_raw = m.group(2).strip()
        ret = (m.group(3) or "").strip()
        params = []
        for p in params_raw.split(","):
            p = p.strip()
            if not p:
                continue
            parts = p.split()
            var_part = next((x for x in reversed(parts) if x.startswith("$") or x.startswith("&$")), None)
            if not var_part:
                continue
            var_part = var_part.lstrip("&")
            type_parts = [x for x in parts if not x.startswith("$") and "=" not in x]
            type_hint = " ".join(type_parts) if type_parts else ""
            default_match = re.search(r'=\s*(.+)$', p)
            default = " = " + default_match.group(1).strip() if default_match else ""
            name_clean = var_part.lstrip("$")
            ann = f": {type_hint}" if type_hint else ""
            params.append(f"{name_clean}{ann}{default}")
        module_fns_php[fn_name] = {"params": params, "returns": ret, "async": False}

    if module_fns_php:
        stem = Path(filepath).stem
        synthetic = stem.capitalize()
        if synthetic not in result:
            result[synthetic] = {}
        for fn_name, fdata in module_fns_php.items():
            if fn_name not in result[synthetic]:
                result[synthetic][fn_name] = fdata

    return result

# ── Ruby extraction (regex, comments for types) ───────────────────────────────

def extract_ruby_signatures(filepath):
    src = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    result = {}
    # Find all class/module declarations and their positions (use innermost class only)
    decl_pattern = re.compile(r'^\s*(?:class|module)\s+([\w:]+)', re.MULTILINE)
    class_positions = [(m.group(1).split("::")[-1], m.end()) for m in decl_pattern.finditer(src)]
    if not class_positions:
        return result
    def _class_for_pos(pos):
        owner = class_positions[0][0]
        for name, cpos in class_positions:
            if cpos <= pos:
                owner = name
        return owner
    method_pattern = re.compile(
        r'^\s{0,12}def\s+((?:self\.)?[\w]+[?!]?)\s*(\([^)]*\))?\s*(?:#\s*->\s*(.+))?',
        re.MULTILINE
    )
    classes = defaultdict(dict)
    for m in method_pattern.finditer(src):
        name = m.group(1)
        params_raw = m.group(2) or "()"
        ret = (m.group(3) or "").strip()
        if name in ("initialize", "method_missing") or name.startswith("_"):
            continue
        owner = _class_for_pos(m.start())
        inner = params_raw.strip("()")
        params = [p.strip() for p in inner.split(",") if p.strip()]
        classes[owner][name] = {"params": params, "returns": ret, "async": False}
    # Detect `alias new_name old_name` and `alias_method :new_name, :old_name`
    alias_pattern = re.compile(
        r'^\s{0,12}alias(?:_method)?\s+:?(\w+)\s+:?(\w+)',
        re.MULTILINE
    )
    for m in alias_pattern.finditer(src):
        new_name, old_name = m.group(1), m.group(2)
        if new_name.startswith("_") or old_name.startswith("_"):
            continue
        owner = _class_for_pos(m.start())
        # Copy the original method's signature if known; otherwise mark as alias
        if old_name in classes[owner]:
            classes[owner][new_name] = classes[owner][old_name]
        else:
            classes[owner][new_name] = {"params": [], "returns": "alias", "async": False}

    for cls, methods in classes.items():
        if methods:
            result[cls] = methods
    return result

# ── TypeScript extraction (regex, full type info) ─────────────────────────────

def extract_ts_signatures(filepath):
    src = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    result = {}
    class_decl = re.compile(r'export\s+(?:abstract\s+)?class\s+(\w+)')
    class_positions = [(m.group(1), m.end()) for m in class_decl.finditer(src)]
    def _class_for_pos(pos):
        if not class_positions:
            return None
        owner = class_positions[0][0]
        for name, cpos in class_positions:
            if cpos <= pos:
                owner = name
        return owner

    # "delete" is excluded here because it's a JS keyword in expressions (delete obj.prop),
    # but it is also a valid ORM instance method name — we allow it through and rely on
    # the context check (indentation + preceding modifiers) to distinguish.
    skip = {"constructor", "if", "for", "while", "switch", "catch", "return",
            "typeof", "instanceof", "new", "void", "throw"}
    classes = defaultdict(dict)

    # Single-line method pattern (indented 0-4 spaces)
    # Return type is captured loosely — stops at { or ; at end of line (handles Array<(fn) => void>)
    pattern = re.compile(
        r'^\s{0,4}(?:(?:public|protected|private|static|async|override)\s+)*\*?\s*'
        r'([a-z]\w*)\s*(?:<[^>\n]*(?:>[^>\n]*)*>)?\s*\(([^)\n]*)\)\s*(?::\s*([^{;\n]+?))?'
        r'\s*(?:\{|;|$)',
        re.MULTILINE
    )
    # Extra pass: methods with function-type params (contain nested parens, e.g. group(prefix, callback: (x) => void))
    nested_paren_decl = re.compile(
        r'^\s{0,6}(?:(?:public|protected|private|static|async|override)\s+)*'
        r'([a-z]\w*)\s*(?:<[^>\n]*>)?\s*\(',
        re.MULTILINE
    )
    for m in nested_paren_decl.finditer(src):
        name = m.group(1)
        if name in skip or name.startswith("_"):
            continue
        line_start = src.rfind('\n', 0, m.start()) + 1
        line = src[line_start:m.start() + len(name) + 10]
        if 'private' in line:
            continue
        owner = _class_for_pos(m.start())
        if name in classes[owner]:
            continue  # already captured by single-line pass
        # Check if there are nested parens in the params
        paren_start = src.index('(', m.start())
        depth = 0
        i = paren_start
        while i < len(src):
            if src[i] == '(': depth += 1
            elif src[i] == ')':
                depth -= 1
                if depth == 0: break
            i += 1
        params_raw = src[paren_start+1:i].replace('\n', ' ')
        if '(' not in params_raw:
            continue  # simple params, already handled by single-line pass
        params_list = split_params(params_raw)
        params_list = [p for p in params_list if not p.startswith('this:')]
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        if owner: classes[owner][name] = {"params": params_list, "returns": ret, "async": is_async}

    for m in pattern.finditer(src):
        name = m.group(1)
        if name in skip or name.startswith("_"):
            continue
        line_start = src.rfind('\n', 0, m.start()) + 1
        line = src[line_start:m.start() + len(name) + 10]
        if 'private' in line:
            continue
        params_raw = m.group(2).strip()
        ret = (m.group(3) or "").strip()
        params = split_params(params_raw)
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        owner = _class_for_pos(m.start())
        if owner:
            classes[owner][name] = {"params": params, "returns": ret, "async": is_async}

    # Multi-line method pattern — method name on its own line, params span multiple lines
    # Matches: `  static methodName<T ...>(` or `  async methodName(` at start of a line
    multiline_decl = re.compile(
        r'^\s{0,6}(?:(?:public|protected|private|static|async|override)\s+)*'
        r'([a-z]\w*)\s*(?:<[^>\n]*(?:>[^>\n]*)*>)?\s*\(\s*$',
        re.MULTILINE
    )
    for m in multiline_decl.finditer(src):
        name = m.group(1)
        if name in skip or name.startswith("_"):
            continue
        line_start = src.rfind('\n', 0, m.start()) + 1
        line = src[line_start:m.start() + len(name) + 10]
        if 'private' in line:
            continue
        owner = _class_for_pos(m.start())
        # Already captured by single-line pattern?
        if name in classes[owner]:
            continue
        # Collect params until closing paren
        paren_start = src.index('(', m.start())
        depth = 0
        i = paren_start
        while i < len(src):
            if src[i] == '(':
                depth += 1
            elif src[i] == ')':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        params_raw = src[paren_start+1:i].replace('\n', ' ')
        # Strip 'this:' TypeScript fake parameter
        params_list = split_params(params_raw)
        params_list = [p for p in params_list if not p.startswith('this:')]
        # Try to get return type after the closing paren
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        if owner: classes[owner][name] = {"params": params_list, "returns": ret, "async": is_async}

    # Third pass: TypeScript static methods with `this: new (...)` generic constraints.
    # These have nested parens in the first parameter that defeat [^)\n]*, e.g.:
    #   static findById<T extends BaseModel>(this: new (...) => T, id: unknown): T | null
    this_param_decl = re.compile(
        r'^\s{1,6}(?:(?:public|protected|private|static|async|override)\s+)+'
        r'([a-z]\w*)\s*(?:<[^>\n]*>)?\s*\(this:\s*new\s*\(',
        re.MULTILINE
    )
    for m in this_param_decl.finditer(src):
        name = m.group(1)
        if name in skip or name.startswith("_"):
            continue
        line_start = src.rfind('\n', 0, m.start()) + 1
        line = src[line_start:m.start() + len(name) + 10]
        if 'private' in line:
            continue
        owner = _class_for_pos(m.start())
        if name in classes[owner]:
            continue
        # Collect all params by paren-depth tracking
        paren_start = src.index('(', m.start())
        depth = 0
        i = paren_start
        while i < len(src):
            if src[i] == '(':
                depth += 1
            elif src[i] == ')':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        params_raw = src[paren_start+1:i].replace('\n', ' ')
        params_list = split_params(params_raw)
        # Strip 'this:' TypeScript fake parameter
        params_list = [p for p in params_list if not p.startswith('this:')]
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        if owner: classes[owner][name] = {"params": params_list, "returns": ret, "async": is_async}

    # Also detect `static propName = functionRef` assignments inside a class body
    static_assign = re.compile(
        r'^\s{1,6}static\s+([a-z]\w*)\s*=\s*(\w+)\s*;',
        re.MULTILINE
    )
    for m in static_assign.finditer(src):
        prop_name = m.group(1)
        fn_name = m.group(2)
        if prop_name.startswith("_"):
            continue
        owner = _class_for_pos(m.start())
        if owner not in classes:
            continue
        if prop_name in classes[owner]:
            continue  # already captured as a method
        # Look up the signature of the referenced standalone export function
        fn_pattern = re.compile(
            r'^export\s+(?:async\s+)?function\s+' + re.escape(fn_name) +
            r'\s*(?:<[^>]*>)?\s*\(([^)]*)\)\s*(?::\s*([\w<>\[\]|&?, ]+?))?'
            r'\s*\{',
            re.MULTILINE
        )
        fn_m = fn_pattern.search(src)
        if fn_m:
            params = [p.strip() for p in fn_m.group(1).split(",") if p.strip()]
            ret = (fn_m.group(2) or "").strip()
            if owner: classes[owner][prop_name] = {"params": params, "returns": ret, "async": False}

    for cls, methods in classes.items():
        if methods:
            result[cls] = methods

    # Fourth pass: TypeScript interface method signatures.
    # Handles factory-function patterns where methods live in an interface
    # rather than a class (e.g. JobLifecycle in job.ts).
    iface_decl = re.compile(r'export\s+interface\s+(\w+)\s*\{', re.MULTILINE)
    iface_method = re.compile(
        r'^\s{1,4}([a-z]\w*)\s*\(([^)]*)\)\s*:\s*([\w<>\[\]|&?, ]+?)\s*;',
        re.MULTILINE
    )
    for im in iface_decl.finditer(src):
        iface_name = im.group(1)
        # Find matching closing brace
        brace_start = im.end() - 1
        depth = 0
        j = brace_start
        while j < len(src):
            if src[j] == '{':
                depth += 1
            elif src[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        iface_body = src[brace_start:j]
        for mm in iface_method.finditer(iface_body):
            mname = mm.group(1)
            if mname in skip or mname.startswith("_"):
                continue
            params_raw = mm.group(2).strip()
            params = split_params(params_raw)
            ret = mm.group(3).strip()
            # Merge into an existing class whose name appears in the interface name
            target = iface_name
            for cname in list(result.keys()):
                if cname in iface_name or iface_name.endswith(cname):
                    target = cname
                    break
            if target not in result:
                result[target] = {}
            if mname not in result[target]:
                result[target][mname] = {"params": params, "returns": ret, "async": False}

    # Fifth pass: top-level exported functions (module-level, not inside a class).
    # Used to pick up Node.js MCP module exports like encodeResponse, decodeRequest, etc.
    # Groups them under a synthetic class name derived from the file stem (CamelCase).
    module_fn = re.compile(
        r'^export\s+(?:async\s+)?function\s+([a-z]\w*)\s*(?:<[^>]*>)?\s*\(([^)]*)\)'
        r'\s*(?::\s*([\w<>\[\]|&?, ]+?))?\s*\{',
        re.MULTILINE
    )
    # Also: export const name = (...) => ... or export const name = function(...)
    module_const_fn = re.compile(
        r'^export\s+const\s+([a-z]\w*)\s*=\s*(?:async\s+)?(?:function\s*\(([^)]*)\)|'
        r'\(([^)]*)\)\s*(?::\s*[\w<>\[\]|&?, ]+?)?\s*=>)',
        re.MULTILINE
    )

    # Build precise class body ranges (start_of_brace .. end_of_brace)
    _class_ranges: list[tuple[int,int]] = []
    for cls_name, cls_start in class_positions:
        brace_pos = src.find('{', cls_start)
        if brace_pos == -1:
            continue
        depth = 0
        j = brace_pos
        while j < len(src):
            if src[j] == '{':
                depth += 1
            elif src[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        _class_ranges.append((brace_pos, j))

    def _is_inside_class(pos: int) -> bool:
        """Return True if pos is inside any class body (between braces)."""
        return any(start <= pos <= end for start, end in _class_ranges)

    module_fns: dict[str, dict] = {}
    for m in module_fn.finditer(src):
        if _is_inside_class(m.start()):
            continue
        name = m.group(1)
        if name in skip or name.startswith("_"):
            continue
        params = split_params(m.group(2).strip())
        ret = (m.group(3) or "").strip()
        is_async = "async" in src[max(0, m.start()-5):m.start()+10]
        module_fns[name] = {"params": params, "returns": ret, "async": is_async}

    # Multi-line module-level function declarations (params span multiple lines)
    module_fn_multiline = re.compile(
        r'^export\s+(?:async\s+)?function\s+([a-z]\w*)\s*(?:<[^>\n]*>)?\s*\(\s*$',
        re.MULTILINE
    )
    for m in module_fn_multiline.finditer(src):
        if _is_inside_class(m.start()):
            continue
        name = m.group(1)
        if name in skip or name.startswith("_") or name in module_fns:
            continue
        paren_start = src.index('(', m.start())
        depth = 0
        i = paren_start
        while i < len(src):
            if src[i] == '(':
                depth += 1
            elif src[i] == ')':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        params_raw = src[paren_start+1:i].replace('\n', ' ')
        params = split_params(params_raw)
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[m.start():m.start()+20]))
        module_fns[name] = {"params": params, "returns": ret, "async": is_async}

    for m in module_const_fn.finditer(src):
        if _is_inside_class(m.start()):
            continue
        name = m.group(1)
        if name in skip or name.startswith("_") or name in module_fns:
            continue
        params_raw = (m.group(2) or m.group(3) or "").strip()
        params = split_params(params_raw)
        module_fns[name] = {"params": params, "returns": "", "async": False}

    # Module-level const aliases: export const foo = existingFn
    module_alias = re.compile(
        r'^export\s+const\s+([a-z]\w*)\s*=\s*([a-z]\w*)\s*;',
        re.MULTILINE
    )
    for m in module_alias.finditer(src):
        if _is_inside_class(m.start()):
            continue
        alias_name = m.group(1)
        target_name = m.group(2)
        if alias_name in skip or alias_name.startswith("_") or alias_name in module_fns:
            continue
        # Look up target in module_fns or in existing result
        if target_name in module_fns:
            module_fns[alias_name] = module_fns[target_name]
        else:
            # Search for the function in the source
            fn_pat = re.compile(
                r'^export\s+(?:async\s+)?function\s+' + re.escape(target_name) +
                r'\s*(?:<[^>]*>)?\s*\(([^)]*)\)\s*(?::\s*([\w<>\[\]|&?, ]+?))?\s*\{',
                re.MULTILINE
            )
            fn_m = fn_pat.search(src)
            if fn_m:
                params = split_params(fn_m.group(1).strip())
                ret = (fn_m.group(2) or "").strip()
                module_fns[alias_name] = {"params": params, "returns": ret, "async": False}

    if module_fns:
        # Derive synthetic class name from filename stem (e.g. mcp.ts -> Mcp)
        stem = Path(filepath).stem
        synthetic = stem.capitalize()
        if synthetic not in result:
            result[synthetic] = {}
        for fname, fdata in module_fns.items():
            if fname not in result[synthetic]:
                result[synthetic][fname] = fdata

    # Sixth pass: function-object method assignments e.g. `response.json = function(...)`
    # Used in response.ts where methods are attached to a callable function, not a class.
    fn_prop_pattern = re.compile(
        r'^\s{0,4}(\w+)\.([a-z]\w*)\s*=\s*(?:async\s+)?function\s*\(([^)]*)\)'
        r'\s*(?::\s*([\w<>\[\]|&?, ]+?))?\s*\{',
        re.MULTILINE
    )
    fn_obj_methods: dict[str, dict[str, dict]] = {}
    for m in fn_prop_pattern.finditer(src):
        obj_name = m.group(1)
        method_name = m.group(2)
        params_raw = m.group(3).strip()
        ret = (m.group(4) or "").strip()
        if method_name in skip or method_name.startswith("_"):
            continue
        if _is_inside_class(m.start()):
            continue
        params = split_params(params_raw)
        is_async = bool(re.search(r'\basync\b', src[max(0, m.start()-5):m.start()+20]))
        if obj_name not in fn_obj_methods:
            fn_obj_methods[obj_name] = {}
        fn_obj_methods[obj_name][method_name] = {"params": params, "returns": ret, "async": is_async}

    # Also catch arrow function form: `response.stream = async function(...)` or
    # `(response as any).stream = async function(...)`
    fn_prop_cast_pattern = re.compile(
        r'^\s{0,4}\(\w+\s+as\s+\w+\)\.([a-z]\w*)\s*=\s*(?:async\s+)?function\s*\(([^)]*)\)'
        r'\s*(?::\s*([\w<>\[\]|&?, ]+?))?\s*\{',
        re.MULTILINE
    )
    for m in fn_prop_cast_pattern.finditer(src):
        method_name = m.group(1)
        params_raw = m.group(2).strip()
        ret = (m.group(3) or "").strip()
        if method_name in skip or method_name.startswith("_"):
            continue
        # Assume same object as any existing fn_obj_methods key, or use file stem
        stem = Path(filepath).stem
        if stem not in fn_obj_methods:
            fn_obj_methods[stem] = {}
        if method_name not in fn_obj_methods[stem]:
            params = split_params(params_raw)
            is_async = bool(re.search(r'\basync\b', src[max(0, m.start()-5):m.start()+20]))
            fn_obj_methods[stem][method_name] = {"params": params, "returns": ret, "async": is_async}

    for obj_name, methods in fn_obj_methods.items():
        # Map to the capitalised object name as a synthetic class
        synthetic = obj_name.capitalize()
        if synthetic not in result:
            result[synthetic] = {}
        for mname, mdata in methods.items():
            if mname not in result[synthetic]:
                result[synthetic][mname] = mdata

    return result

# ── Feature area sources ──────────────────────────────────────────────────────

FEATURE_SOURCES = {
    "ORM": {
        "Python": BASE / "tina4-python/tina4_python/orm/model.py",
        "PHP":    BASE / "tina4-php/Tina4/ORM.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/orm.rb",
        "Node":   BASE / "tina4-nodejs/packages/orm/src/baseModel.ts",
    },
    "Queue": {
        "Python": BASE / "tina4-python/tina4_python/queue/__init__.py",
        "PHP":    (BASE / "tina4-php/Tina4/Queue.php", "Queue"),
        "Ruby":   BASE / "tina4-ruby/lib/tina4/queue.rb",
        "Node":   (BASE / "tina4-nodejs/packages/core/src/queue.ts", "Queue"),
    },
    "Job": {
        "Python": BASE / "tina4-python/tina4_python/queue/job.py",
        "PHP":    BASE / "tina4-php/Tina4/Job.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/job.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/job.ts",
    },
    "Auth": {
        "Python": BASE / "tina4-python/tina4_python/auth/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Auth.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/auth.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/auth.ts",
    },
    "Database": {
        "Python": BASE / "tina4-python/tina4_python/database/connection.py",
        "PHP":    BASE / "tina4-php/Tina4/Database/Database.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/database.rb",
        "Node":   BASE / "tina4-nodejs/packages/orm/src/database.ts",
    },
    "Router": {
        "Python": BASE / "tina4-python/tina4_python/core/router.py",
        "PHP":    BASE / "tina4-php/Tina4/Router.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/router.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/router.ts",
    },
    "Session": {
        "Python": BASE / "tina4-python/tina4_python/session/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Session.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/session.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/session.ts",
    },
    "Migration": {
        "Python": BASE / "tina4-python/tina4_python/migration/runner.py",
        "PHP":    BASE / "tina4-php/Tina4/Migration.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/migration.rb",
        "Node":   BASE / "tina4-nodejs/packages/orm/src/migration.ts",
    },
    "MCP": {
        "Python": [BASE / "tina4-python/tina4_python/mcp/__init__.py",
                   BASE / "tina4-python/tina4_python/mcp/protocol.py"],
        "PHP":    BASE / "tina4-php/Tina4/MCP.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/mcp.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/mcp.ts",
    },
    "Frond": {
        "Python": BASE / "tina4-python/tina4_python/frond/engine.py",
        "PHP":    BASE / "tina4-php/Tina4/Frond.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/frond.rb",
        "Node":   BASE / "tina4-nodejs/packages/frond/src/engine.ts",
    },
    "GraphQL": {
        "Python": BASE / "tina4-python/tina4_python/graphql/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/GraphQL.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/graphql.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/graphql.ts",
    },
    "Api": {
        "Python": BASE / "tina4-python/tina4_python/api/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Api.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/api.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/api.ts",
    },
    "Cache": {
        "Python": BASE / "tina4-python/tina4_python/cache/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Cache.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/response_cache.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/cache.ts",
    },
    "Container": {
        "Python": BASE / "tina4-python/tina4_python/container/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Container.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/container.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/container.ts",
    },
    "Events": {
        "Python": BASE / "tina4-python/tina4_python/core/events.py",
        "PHP":    BASE / "tina4-php/Tina4/Events.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/events.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/events.ts",
    },
    "WebSocket": {
        "Python": BASE / "tina4-python/tina4_python/websocket/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/WebSocket.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/websocket.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/websocket.ts",
    },
    "WSDL": {
        "Python": BASE / "tina4-python/tina4_python/wsdl/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/WSDL.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/wsdl.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/wsdl.ts",
    },
    "Swagger": {
        "Python": BASE / "tina4-python/tina4_python/swagger/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Swagger.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/swagger.rb",
        "Node":   BASE / "tina4-nodejs/packages/swagger/src/generator.ts",
    },
    "I18n": {
        "Python": BASE / "tina4-python/tina4_python/i18n/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/I18n.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/localization.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/i18n.ts",
    },
    "Seeder": {
        "Python": BASE / "tina4-python/tina4_python/seeder/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/FakeData.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/seeder.rb",
        "Node":   [BASE / "tina4-nodejs/packages/core/src/fakeData.ts",
                   BASE / "tina4-nodejs/packages/orm/src/fakeData.ts",
                   BASE / "tina4-nodejs/packages/orm/src/seeder.ts"],
    },
    "QueryBuilder": {
        "Python": BASE / "tina4-python/tina4_python/query_builder/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/QueryBuilder.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/query_builder.rb",
        "Node":   BASE / "tina4-nodejs/packages/orm/src/queryBuilder.ts",
    },
    "Validator": {
        "Python": BASE / "tina4-python/tina4_python/validator/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Validator.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/validator.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/validator.ts",
    },
    "HtmlElement": {
        "Python": BASE / "tina4-python/tina4_python/HtmlElement.py",
        "PHP":    BASE / "tina4-php/Tina4/HtmlElement.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/html_element.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/htmlElement.ts",
    },
    "Testing": {
        "Python": BASE / "tina4-python/tina4_python/Testing.py",
        "PHP":    BASE / "tina4-php/Tina4/Testing.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/testing.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/testing.ts",
    },
    "Messenger": {
        "Python": BASE / "tina4-python/tina4_python/messenger/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Messenger.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/messenger.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/messenger.ts",
    },
    "Logger": {
        "Python": BASE / "tina4-python/tina4_python/debug/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/Log.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/log.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/logger.ts",
    },
    "AI": {
        "Python": BASE / "tina4-python/tina4_python/ai/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/AI.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/ai.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/ai.ts",
    },
    "Request": {
        "Python": BASE / "tina4-python/tina4_python/core/request.py",
        "PHP":    BASE / "tina4-php/Tina4/Request.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/request.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/request.ts",
    },
    "Response": {
        "Python": BASE / "tina4-python/tina4_python/core/response.py",
        "PHP":    BASE / "tina4-php/Tina4/Response.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/response.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/response.ts",
    },
    "Middleware": {
        "Python": BASE / "tina4-python/tina4_python/core/middleware.py",
        "PHP":    [
            BASE / "tina4-php/Tina4/Middleware.php",
            BASE / "tina4-php/Tina4/Middleware/CorsMiddleware.php",
            BASE / "tina4-php/Tina4/Middleware/CsrfMiddleware.php",
            BASE / "tina4-php/Tina4/Middleware/RateLimiter.php",
            BASE / "tina4-php/Tina4/Middleware/RequestLogger.php",
            BASE / "tina4-php/Tina4/Middleware/SecurityHeaders.php",
        ],
        "Ruby":   BASE / "tina4-ruby/lib/tina4/middleware.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/middleware.ts",
    },
    "AutoCrud": {
        "Python": BASE / "tina4-python/tina4_python/crud/__init__.py",
        "PHP":    BASE / "tina4-php/Tina4/AutoCrud.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/auto_crud.rb",
        "Node":   BASE / "tina4-nodejs/packages/orm/src/autoCrud.ts",
    },
    "SqlTranslation": {
        "Python": [
            BASE / "tina4-python/tina4_python/database/adapter.py",
            BASE / "tina4-python/tina4_python/core/cache.py",
        ],
        "PHP":    [
            BASE / "tina4-php/Tina4/SqlTranslation.php",
            BASE / "tina4-php/Tina4/QueryCache.php",
        ],
        "Ruby":   [
            BASE / "tina4-ruby/lib/tina4/sql_translation.rb",
            BASE / "tina4-ruby/lib/tina4/cache.rb",
        ],
        "Node":   BASE / "tina4-nodejs/packages/orm/src/sqlTranslation.ts",
    },
    "Metrics": {
        "Python": BASE / "tina4-python/tina4_python/core/server.py",
        "PHP":    BASE / "tina4-php/Tina4/Metrics.php",
        "Ruby":   BASE / "tina4-ruby/lib/tina4/metrics.rb",
        "Node":   BASE / "tina4-nodejs/packages/core/src/metrics.ts",
    },
}

EXTRACTORS = {
    "Python": extract_python_signatures,
    "PHP":    extract_php_signatures,
    "Ruby":   extract_ruby_signatures,
    "Node":   extract_ts_signatures,
}

LANGS = ["Python", "PHP", "Ruby", "Node"]

# ── Comparison logic ──────────────────────────────────────────────────────────

def normalise_type(t):
    """
    Normalise type strings to a canonical form for cross-language comparison.

    Key rules:
    - PHP `array<string, mixed>` / `array<string, *>` → `dict`  (associative = dict)
    - PHP bare `array` without generic → `list`                  (indexed = list)
    - Ruby `Hash` → `dict`
    - TypeScript `Record<*>` → `dict`
    - All framework Self/static/this → `Self`
    - Numeric types unified to `int`
    - Void/null unified to `None`
    """
    if not t:
        return ""
    t = t.strip()

    # PHP typed arrays: array<string, *> or array<int, *> → dict or list
    # array<string, X> is an associative array → dict
    t = re.sub(r'\barray<\s*string\s*,\s*[^>]+>', 'dict', t, flags=re.IGNORECASE)
    # array<int, X> is an indexed array → list[X] (preserve inner type for comparison)
    def _int_array_to_list(m):
        inner = m.group(1).strip()
        # Normalise the inner type (static→Self etc.) but avoid recursion for complex types
        inner = re.sub(r'\b(static|self|this)\b', 'Self', inner)
        inner = re.sub(r'\bBoolean\b', 'bool', inner, flags=re.IGNORECASE)
        inner = re.sub(r'\bInteger\b', 'int', inner, flags=re.IGNORECASE)
        inner = re.sub(r'\bString\b', 'str', inner, flags=re.IGNORECASE)
        inner = re.sub(r'\bnil\b', 'None', inner)
        inner = re.sub(r'\bnull\b', 'None', inner, flags=re.IGNORECASE)
        inner = re.sub(r'\bT\b', 'Self', inner)
        if inner.lower() in ('mixed', 'any', ''):
            return 'list'
        return f'list[{inner}]'
    t = re.sub(r'\barray<\s*int\s*,\s*([^>]+)>', _int_array_to_list, t, flags=re.IGNORECASE)
    # array{key: type, ...} (shape arrays) → dict
    t = re.sub(r'\barray\{[^}]+\}', 'dict', t, flags=re.IGNORECASE)
    # Generic array<X> without explicit key type → list
    t = re.sub(r'\barray<[^>]+>', 'list', t, flags=re.IGNORECASE)

    # PHP @return int|string|null style — keep as-is after other transforms

    # PHP nullable shorthand: ?Type → Type|None
    t = re.sub(r'^\?(\w[\w\\]*)', r'\1|None', t)

    # Framework Self/static/this
    t = re.sub(r'\b(static|self|this)\b', 'Self', t)

    # Collection types
    t = re.sub(r'\bHash\b', 'dict', t, flags=re.IGNORECASE)
    t = re.sub(r'\bRecord\b\s*(?:<[^>]*>)?', 'dict', t)
    t = re.sub(r'\bObject\b', 'dict', t)

    # Array/list types (bare, after generic forms already handled above)
    t = re.sub(r'\bArray\b', 'list', t, flags=re.IGNORECASE)
    t = re.sub(r'Model\[\]', 'list', t)
    t = re.sub(r'(\w+)\[\]', r'list[\1]', t)   # T[] → list[T]

    # Scalar types
    t = re.sub(r'\bBoolean\b', 'bool', t, flags=re.IGNORECASE)
    t = re.sub(r'\bInteger\b', 'int', t, flags=re.IGNORECASE)
    t = re.sub(r'\bString\b', 'str', t, flags=re.IGNORECASE)
    t = re.sub(r'\bnumber\b', 'int', t, flags=re.IGNORECASE)
    t = re.sub(r'\bfloat\b', 'float', t, flags=re.IGNORECASE)
    # false/true are specific boolean literals — treat as bool in type position
    t = re.sub(r'\bfalse\b', 'bool', t)
    t = re.sub(r'\btrue\b', 'bool', t)

    # Void/null
    t = re.sub(r'\bvoid\b', 'None', t, flags=re.IGNORECASE)
    t = re.sub(r'\bnull\b', 'None', t, flags=re.IGNORECASE)
    t = re.sub(r'\bnil\b', 'None', t)

    # Strip surrounding quotes from forward references ('ClassName' → ClassName)
    t = re.sub(r"^['\"](.+)['\"]$", r'\1', t)

    # Erase generic unknown params: list[unknown] → list
    t = re.sub(r'\blist\[unknown\]', 'list', t, flags=re.IGNORECASE)

    # object (PHP stdClass) → dict
    t = re.sub(r'\bobject\b', 'dict', t, flags=re.IGNORECASE)

    # ORM model references
    t = re.sub(r'\bModel\b', 'Self', t)
    t = re.sub(r'\bORM\b', 'Self', t)

    # Queue job references (cross-language: QueueJob/Job → dict)
    t = re.sub(r'\bQueueJob\b', 'dict', t)
    t = re.sub(r'\bJob\b', 'dict', t)

    # PHP list[list] == list[dict] (PHP uses arrays for both indexed and associative)
    t = re.sub(r'\blist\[list\]', 'list[dict]', t)

    # TypeScript generic T/R used for model return type → Self
    # (T/R extends BaseModel is TypeScript's equivalent of Python/Ruby Self)
    t = re.sub(r'\bT\b', 'Self', t)
    t = re.sub(r'\bR\b', 'Self', t)

    # TypeScript Promise<X> → X (async wrapper is semantically equivalent to X)
    # Handle nested generics (up to one level of < >)
    t = re.sub(r'\bPromise<([^<>]*(?:<[^<>]*>[^<>]*)*)>', r'\1', t)
    # Drop parameterisation from list[T] → list (cross-framework element types diverge
    # — PHP has no generics, Ruby untyped, Python/TS disagree on element type noise)
    t = re.sub(r'\blist\[[^\]]*\]', 'list', t)
    # dict[K, V] → dict
    t = re.sub(r'\bdict\[[^\]]*\]', 'dict', t)
    # Strip stray trailing `\n` artifacts from docblock extraction
    t = t.replace('\\n', '').strip()

    # Normalise whitespace and union spacing: "Self | false" == "Self|false"
    t = re.sub(r'\s*\|\s*', '|', t)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def clean_params(params):
    """Strip TS factory 'this' generic params, Ruby block params, and other noise."""
    cleaned = []
    for p in params:
        if p.startswith("**"):
            continue  # **kwargs not counted
        # Ruby/Python splat — only discard the conventional *args / *_args / *kwargs forms
        # (NOT *fields, *items, etc. which are semantically meaningful params).
        if re.match(r'^\*_?(args|kwargs)\b', p):
            continue
        # TypeScript/PHP variadic spread `...args: ...` — discard similarly
        if re.match(r'^\.\.\._?args\b', p.lstrip()):
            continue
        # Ruby block params (&block) are the idiomatic equivalent of a callback/handler
        # argument — normalise to "handler" so it compares against Python/Node's handler param.
        if p.startswith("&"):
            cleaned.append("handler")
            continue
        # Skip TypeScript generic class factory param — looks like:
        #   "new (...args: unknown[]) => T"  or  "unknown>) => T"
        # These appear in static methods on generic classes (e.g. BaseModel.find<T>)
        # They are NOT real user-facing parameters.
        stripped = p.strip()
        if re.search(r'\bnew\b.*=>', stripped) or re.match(r'unknown.*\)\s*=>', stripped):
            continue
        # Ruby named keyword args with literal defaults are often framework-internal options
        # (middleware: [], swagger_meta: {}, template: nil, include: nil, etc.) that don't
        # correspond to positional params in other frameworks. Suppress them UNLESS they are
        # known cross-framework API params (Queue, Auth, Database specifics).
        _RUBY_REAL_KWARGS = {
            # Queue real params present in all frameworks
            "max_retries", "delay_seconds", "batch_size", "iterations", "poll_interval",
            "priority", "id", "topic", "max_jobs",
            # Auth real params
            "secret", "algorithm", "expires_in",
            # Database real params
            "pk_column", "generator_name", "pool",
            # Api/HTTP real params — keyword args on get/post/put/patch/delete/send_request
            "params", "body", "content_type", "headers", "method",
        }
        kw_match = re.match(r'^(\w+):\s*', stripped)
        if kw_match:
            kw_name = kw_match.group(1)
            if kw_name not in _RUBY_REAL_KWARGS:
                # Suppress: Ruby framework option kwarg with literal default
                if re.search(r':\s*(\[\]|\{\}|nil\b|true\b|false\b|\d+|["\'])', stripped):
                    continue
        cleaned.append(p)
    return cleaned

def is_optional_param(p: str) -> bool:
    """Return True if param is optional (has a default value or TS ? suffix)."""
    s = p.strip()
    # TypeScript optional: foo? or foo?: Type
    if re.match(r'\w+\?', s):
        return True
    # Has an explicit default: foo = None, foo = [], foo = null, foo = 0, etc.
    # The `= ` part comes after the name (and optional type annotation)
    if ' = ' in s or s.endswith('=None') or s.endswith('= None'):
        return True
    # Ruby keyword arg with default: "foo: nil", "foo: 0", "foo: 1.0", "foo: true", etc.
    if re.match(r'\w+:\s*(nil\b|true\b|false\b|\d|["\'])', s):
        return True
    return False

def param_count(method):
    """Count required params only (exclude optional/defaulted ones)."""
    params = clean_params(method["params"])
    return len([p for p in params if not is_optional_param(p)])

def param_range(method):
    """Return (required_count, total_count) — the acceptable arity range for this method."""
    params = clean_params(method["params"])
    required = len([p for p in params if not is_optional_param(p)])
    total = len(params)
    return (required, total)

def param_ranges_compatible(methods):
    """
    Two methods are compatible if their (required, total) ranges overlap.
    E.g. Python (sql, style='?') -> (1, 2)  overlaps PHP (sql, style) -> (2, 2)
    at arity 2, so they're considered a match.
    """
    ranges = [param_range(m) for m in methods]
    if not ranges:
        return True
    lo = max(r[0] for r in ranges)
    hi = min(r[1] for r in ranges)
    return lo <= hi

def compare_returns(methods_by_lang):
    """Return (canonical_return, {lang: normalised_return}, has_mismatch)"""
    returns = {l: normalise_type(m["returns"]) for l, m in methods_by_lang.items() if m}
    non_empty = [v for v in returns.values() if v]
    if not non_empty:
        return "", returns, False
    # Only flag a mismatch when at least 2 frameworks have explicit (non-empty) return
    # type annotations that disagree. Untyped (empty) is compatible with anything.
    # Also treat "untyped" as compatible (Ruby/Python often lack explicit return types).
    # Wildcards: untyped (no annotation), mixed (PHP "any"), bare list (PHP array ambiguity)
    _WILDCARDS = {"untyped", "mixed", ""}
    typed = [v for v in non_empty if v not in _WILDCARDS]
    # Normalise PHP ambiguity: bare `list` (PHP `array`) is indistinguishable from `dict`
    # since PHP arrays serve both roles. Treat them as equivalent for parity.
    def _canon(v):
        # PHP arrays serve as both indexed lists and associative dicts — treat them
        # as equivalent at the type-comparison level. Applies to bare `list`,
        # `list|None`, etc., anywhere in the string.
        return re.sub(r'\blist\b', 'dict', v)
    unique = {_canon(v) for v in typed}
    has_mismatch = len(typed) >= 2 and len(unique) > 1
    canonical = max(non_empty, key=len)  # pick most informative
    return canonical, returns, has_mismatch

# ── Render markdown ───────────────────────────────────────────────────────────

def render_method_table(area, method_groups):
    """
    method_groups: {canonical_name: {lang: method_dict | None}}
    """
    lines = []
    lines.append(f"## {area}")
    lines.append("")

    # Header
    lines.append("| Method | Python | PHP | Ruby | Node | Return Match |")
    lines.append("|--------|--------|-----|------|------|:------------:|")

    for canon, by_lang in sorted(method_groups.items()):
        present = {l: by_lang.get(l) for l in LANGS}

        # Build per-lang signature cells
        cells = []
        for lang in LANGS:
            m = present.get(lang)
            if m is None:
                cells.append("—")
            else:
                p_count = param_count(m)
                ret = normalise_type(m["returns"])
                params_short = ", ".join(
                    re.sub(r':.*', '', p).split('=')[0].strip()
                    for p in clean_params(m["params"])
                )
                sig = f"`{params_short}`" if params_short else "`()`"
                cells.append(sig)

        # Return type comparison
        present_methods = {l: m for l, m in present.items() if m}
        _, ret_by_lang, ret_mismatch = compare_returns(present_methods)

        # Param count mismatch — ranges must overlap (defaults count as optional)
        param_mismatch = not param_ranges_compatible(list(present_methods.values()))

        # Missing frameworks
        missing = [l for l in LANGS if present.get(l) is None]

        if missing:
            status = f"⚠️ missing: {', '.join(missing)}"
        elif param_mismatch:
            status = "⚠️ param count differs"
        elif ret_mismatch:
            status = "ℹ️ return type differs"
        else:
            status = "✅"

        lines.append(f"| `{canon}` | {' | '.join(cells)} | {status} |")

    lines.append("")

    # Detail section for mismatches
    mismatches = []
    for canon, by_lang in sorted(method_groups.items()):
        present_methods = {l: m for l, m in by_lang.items() if m}
        missing = [l for l in LANGS if by_lang.get(l) is None]
        _, ret_by_lang, ret_mismatch = compare_returns(present_methods)
        counts = {l: param_count(m) for l, m in present_methods.items()}
        param_mismatch = not param_ranges_compatible(list(present_methods.values()))

        if missing or ret_mismatch or param_mismatch:
            mismatches.append((canon, by_lang, missing, ret_by_lang, ret_mismatch, counts, param_mismatch))

    if mismatches:
        lines.append("### Mismatch Details")
        lines.append("")
        for canon, by_lang, missing, ret_by_lang, ret_mismatch, counts, param_mismatch in mismatches:
            lines.append(f"#### `{canon}`")
            lines.append("")
            lines.append("| Framework | Signature | Return Type |")
            lines.append("|-----------|-----------|-------------|")
            for lang in LANGS:
                m = by_lang.get(lang)
                if m is None:
                    lines.append(f"| {lang} | — not implemented — | — |")
                else:
                    sig = ", ".join(m["params"]) if m["params"] else ""
                    ret = normalise_type(m["returns"]) or "untyped"
                    lines.append(f"| {lang} | `{sig}` | `{ret}` |")
            lines.append("")

    return "\n".join(lines)


# ── Module-level function extractor (fallback for non-class APIs) ─────────────

def _extract_module_functions(lang, path):
    """Extract top-level public functions as a flat method dict."""
    src = Path(path).read_text(encoding="utf-8", errors="ignore")
    methods = {}
    if lang == "Python":
        try:
            tree = ast.parse(src)
        except SyntaxError:
            return {}
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            args = node.args
            all_args = args.posonlyargs + args.args
            defaults_offset = len(all_args) - len(args.defaults)
            params = []
            for i, arg in enumerate(all_args):
                if arg.arg in ("self", "cls"):
                    continue
                params.append(py_param(arg, args.defaults, i - defaults_offset))
            returns = ""
            if node.returns:
                try:
                    returns = ast.unparse(node.returns)
                except Exception:
                    pass
            methods[node.name] = {"params": params, "returns": returns, "async": isinstance(node, ast.AsyncFunctionDef)}
    elif lang == "Node":
        # export function / export async function
        pattern = re.compile(
            r'^export\s+(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)\s*(?::\s*([\w<>\[\]|&?, ]+?))?'
            r'\s*(?:\{|$)',
            re.MULTILINE
        )
        for m in pattern.finditer(src):
            name = m.group(1)
            if name.startswith("_"):
                continue
            params = split_params(m.group(2))
            params = [p for p in params if not p.startswith('this:')]
            ret = (m.group(3) or "").strip()
            is_async = bool(re.search(rf'\bexport\s+async\s+function\s+{name}\b', src))
            methods[name] = {"params": params, "returns": ret, "async": is_async}
    return methods


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    all_sections = []
    summary_rows = []

    for area, sources in FEATURE_SOURCES.items():
        print(f"Processing {area}...")

        # Extract per language
        # sources values can be: Path | (Path, class_name)
        lang_data = {}  # lang -> {class: {method: {params, returns}}}
        lang_filter = {}  # lang -> class_name | None
        for lang, spec in sources.items():
            if isinstance(spec, tuple):
                path, class_name = spec
                lang_filter[lang] = class_name
                paths = [path]
            elif isinstance(spec, list):
                paths = spec
                class_name = None
                lang_filter[lang] = None
            else:
                paths = [spec]
                class_name = None
                lang_filter[lang] = None
            extractor = EXTRACTORS[lang]
            merged_data: dict = {}
            for path in paths:
                if not path.exists():
                    print(f"  {lang}: FILE NOT FOUND — {path}")
                    continue
                data = extractor(str(path))
                for cls, methods in data.items():
                    if cls not in merged_data:
                        merged_data[cls] = {}
                    merged_data[cls].update(methods)
            lang_data[lang] = merged_data
            total = sum(len(methods) for methods in merged_data.values())
            print(f"  {lang}: {len(merged_data)} classes, {total} methods")

        # Flatten: if a class_name filter is set, use only that class.
        # Otherwise merge all public classes (first-wins on name collision).
        # Falls back to module-level functions if no class found.
        flat = {}  # lang -> {method_name: {params, returns}}
        for lang, classes in lang_data.items():
            filter_cls = lang_filter.get(lang)
            path = sources.get(lang)
            path = path[0] if isinstance(path, tuple) else path
            if not classes:
                if path and path.exists():
                    flat[lang] = _extract_module_functions(lang, path)
                else:
                    flat[lang] = {}
                continue
            if filter_cls:
                # Use only the specified class; case-insensitive fallback
                matched = classes.get(filter_cls) or next(
                    (v for k, v in classes.items() if k.lower() == filter_cls.lower()), None
                )
                flat[lang] = matched or {}
            else:
                # Merge all classes, but prefer the primary class (named after the area)
                # over internal handler/adapter classes. Iterate primary-class-first so
                # that first-wins preserves the public API signature.
                area_lower = area.lower()
                # Sort so the class whose name best matches the area comes first
                def cls_priority(cls_name):
                    n = cls_name.lower()
                    if n == area_lower:
                        return 0
                    if n.startswith(area_lower) and not any(x in n for x in ('handler', 'adapter', 'backend', 'driver')):
                        return 1
                    if any(x in n for x in ('handler', 'adapter', 'backend', 'driver')):
                        return 3
                    return 2
                sorted_classes = sorted(classes.items(), key=lambda kv: cls_priority(kv[0]))
                merged = {}
                for _, methods in sorted_classes:
                    for name, sig in methods.items():
                        if name not in merged:
                            merged[name] = sig
                        else:
                            # Most-params-wins within a language's classes
                            old_count = len(merged[name].get("params", []))
                            new_count = len(sig.get("params", []))
                            if new_count > old_count:
                                merged[name] = sig
                flat[lang] = merged

        # Build canonical method groups
        # Map: canonical_snake_name -> {lang: method_dict | None}
        # Skip language-specific magic methods (PHP __magic, Ruby initialize, etc.)
        MAGIC_PREFIXES = ('__',)
        all_methods = defaultdict(dict)
        for lang, methods in flat.items():
            for name, sig in methods.items():
                if any(name.startswith(p) for p in MAGIC_PREFIXES):
                    continue
                # Strip Ruby/Python class-method prefix (self.create -> create)
                stripped_name = re.sub(r'^(?:self|cls)\.', '', name)
                canon = to_snake(stripped_name)
                # Most-params-wins: prefer the richer signature when multiple
                # classes define the same method name (e.g., GraphQLType.parse
                # over GraphQLParser.parse).
                existing = all_methods[canon].get(lang)
                if existing is None:
                    all_methods[canon][lang] = sig
                else:
                    old_count = len(existing.get("params", []))
                    new_count = len(sig.get("params", []))
                    if new_count > old_count:
                        all_methods[canon][lang] = sig

        # Fill missing
        for canon in all_methods:
            for lang in LANGS:
                if lang not in all_methods[canon]:
                    all_methods[canon][lang] = None

        # Noise filter: drop methods that exist in only 1 framework.
        # Single-framework methods are almost always language-internal helpers.
        all_methods = {
            canon: by_lang
            for canon, by_lang in all_methods.items()
            if sum(1 for m in by_lang.values() if m is not None) >= 2
        }

        # Count issues — mutually exclusive: missing > mismatch > ok
        total_methods = len(all_methods)
        missing_count = 0
        mismatch_count = 0
        ok_count = 0
        for canon, by_lang in all_methods.items():
            present = {l: m for l, m in by_lang.items() if m}
            if len(present) < len(LANGS):
                missing_count += 1
            else:
                _, _, ret_mismatch = compare_returns(present)
                # Use range-compatible check (honors optional/defaulted params)
                # so the summary matches the per-method ✅ / ⚠️ status column.
                param_mismatch = not param_ranges_compatible(list(present.values()))
                if param_mismatch:
                    # Real mismatch: param count/names differ
                    mismatch_count += 1
                else:
                    # OK even if only return-type annotation differs
                    ok_count += 1

        summary_rows.append((area, total_methods, ok_count, mismatch_count, missing_count))

        section = render_method_table(area, all_methods)
        all_sections.append(section)

    # Build document
    lines = [
        "# Tina4 Signature Parity Report",
        "",
        f"> Auto-generated on {date.today().isoformat()}",
        "",
        "Compares public method signatures (params + return types) across Python, PHP, Ruby, and Node.js.",
        "Methods are matched by normalised snake_case name. ✅ = full parity, ⚠️ = mismatch or missing.",
        "",
        "## Summary",
        "",
        "| Feature | Methods | ✅ Match | ⚠️ Mismatch | ⚠️ Missing |",
        "|---------|--------:|--------:|------------:|----------:|",
    ]
    for area, total, ok, mismatch, missing in summary_rows:
        lines.append(f"| {area} | {total} | {ok} | {mismatch} | {missing} |")

    lines.append("")
    lines.extend(all_sections)

    out = Path(__file__).parent / "SIGNATURE-PARITY.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {out}")
    print(f"Size: {out.stat().st_size:,} bytes")

    # Print summary
    print("\n── Summary ──────────────────────────────────────")
    print(f"{'Feature':<12} {'Total':>7} {'OK':>5} {'Mismatch':>9} {'Missing':>8}")
    print("-" * 46)
    for area, total, ok, mismatch, missing in summary_rows:
        print(f"{area:<12} {total:>7} {ok:>5} {mismatch:>9} {missing:>8}")


if __name__ == "__main__":
    main()
