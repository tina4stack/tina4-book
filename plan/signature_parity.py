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

# ── Name normalisation ────────────────────────────────────────────────────────

def to_snake(name):
    """Convert camelCase / PascalCase to snake_case for comparison."""
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    return s.lower().strip('?')

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
            is_async = isinstance(item, ast.AsyncFunctionDef)
            methods[name] = {
                "params": params,
                "returns": returns,
                "async": is_async,
            }
        if methods:
            result[node.name] = methods
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
            var_part = next((x for x in reversed(parts) if x.startswith("$")), None)
            if not var_part:
                continue
            type_parts = [x for x in parts if not x.startswith("$") and "=" not in x]
            type_hint = " ".join(type_parts) if type_parts else ""
            default_match = re.search(r'=\s*(.+)$', p)
            default = " = " + default_match.group(1).strip() if default_match else ""
            name_clean = var_part.lstrip("$")
            ann = f": {type_hint}" if type_hint else ""
            params.append(f"{name_clean}{ann}{default}")
        classes[owner][name] = {"params": params, "returns": ret, "async": False}
    for cls, methods in classes.items():
        if methods:
            result[cls] = methods
    return result

# ── Ruby extraction (regex, comments for types) ───────────────────────────────

def extract_ruby_signatures(filepath):
    src = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    result = {}
    # Find all class/module declarations and their positions (use innermost class only)
    decl_pattern = re.compile(r'^\s*class\s+([\w:]+)', re.MULTILINE)
    class_positions = [(m.group(1).split("::")[-1], m.end()) for m in decl_pattern.finditer(src)]
    if not class_positions:
        # Fall back to any module/class
        fallback = re.search(r'(?:class|module)\s+([\w:]+)', src)
        if not fallback:
            return result
        class_positions = [(fallback.group(1).split("::")[-1], fallback.end())]
    def _class_for_pos(pos):
        owner = class_positions[0][0]
        for name, cpos in class_positions:
            if cpos <= pos:
                owner = name
        return owner
    method_pattern = re.compile(
        r'^\s{0,12}def\s+((?:self\.)?\w+)\s*(\([^)]*\))?\s*(?:#\s*->\s*(.+))?',
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
    if not class_positions:
        return result
    def _class_for_pos(pos):
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
    pattern = re.compile(
        r'^\s{0,4}(?:(?:public|protected|private|static|async|override)\s+)*\*?\s*'
        r'([a-z]\w*)\s*(?:<[^>\n]*(?:>[^>\n]*)*>)?\s*\(([^)\n]*)\)\s*(?::\s*([\w<>\[\]|&?, ]+?))?'
        r'\s*(?:\{|;|$)',
        re.MULTILINE
    )
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
        params = [p.strip() for p in params_raw.split(",") if p.strip()]
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        owner = _class_for_pos(m.start())
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
        params_list = [p.strip() for p in params_raw.split(',') if p.strip()]
        params_list = [p for p in params_list if not p.startswith('this:')]
        # Try to get return type after the closing paren
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        classes[owner][name] = {"params": params_list, "returns": ret, "async": is_async}

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
        params_list = [p.strip() for p in params_raw.split(',') if p.strip()]
        # Strip 'this:' TypeScript fake parameter
        params_list = [p for p in params_list if not p.startswith('this:')]
        after = src[i+1:i+80].strip()
        ret_m = re.match(r':\s*([\w<>\[\]|&?, ]+?)\s*(?:\{|$)', after)
        ret = ret_m.group(1).strip() if ret_m else ""
        is_async = bool(re.search(r'\basync\b', src[line_start:m.start()]))
        classes[owner][name] = {"params": params_list, "returns": ret, "async": is_async}

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
            classes[owner][prop_name] = {"params": params, "returns": ret, "async": False}

    for cls, methods in classes.items():
        if methods:
            result[cls] = methods
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
        "Node":   BASE / "tina4-nodejs/packages/core/src/queue.ts",
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
        "Python": BASE / "tina4-python/tina4_python/mcp/__init__.py",
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

    # Queue job references (cross-language: QueueJob → dict)
    t = re.sub(r'\bQueueJob\b', 'dict', t)

    # TypeScript generic T/R used for model return type → Self
    # (T/R extends BaseModel is TypeScript's equivalent of Python/Ruby Self)
    t = re.sub(r'\bT\b', 'Self', t)
    t = re.sub(r'\bR\b', 'Self', t)

    # Normalise whitespace and union spacing: "Self | false" == "Self|false"
    t = re.sub(r'\s*\|\s*', '|', t)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def param_count(method):
    return len([p for p in method["params"] if not p.startswith("**")])

def compare_returns(methods_by_lang):
    """Return (canonical_return, {lang: normalised_return}, has_mismatch)"""
    returns = {l: normalise_type(m["returns"]) for l, m in methods_by_lang.items() if m}
    non_empty = [v for v in returns.values() if v]
    if not non_empty:
        return "", returns, False
    # Only flag a mismatch when at least 2 frameworks have explicit (non-empty) return
    # type annotations that disagree. Untyped (empty) is compatible with anything.
    unique = set(non_empty)
    has_mismatch = len(non_empty) >= 2 and len(unique) > 1
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
                    for p in m["params"]
                )
                sig = f"`{params_short}`" if params_short else "`()`"
                cells.append(sig)

        # Return type comparison
        present_methods = {l: m for l, m in present.items() if m}
        _, ret_by_lang, ret_mismatch = compare_returns(present_methods)

        # Param count mismatch
        counts = [param_count(m) for m in present_methods.values()]
        param_mismatch = len(set(counts)) > 1

        # Missing frameworks
        missing = [l for l in LANGS if present.get(l) is None]

        if missing:
            status = f"⚠️ missing: {', '.join(missing)}"
        elif ret_mismatch:
            status = "⚠️ return type differs"
        elif param_mismatch:
            status = "⚠️ param count differs"
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
        param_mismatch = len(set(counts.values())) > 1

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
            params = [p.strip() for p in m.group(2).split(",") if p.strip()]
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
            else:
                path, class_name = spec, None
                lang_filter[lang] = None
            if not path.exists():
                print(f"  {lang}: FILE NOT FOUND — {path}")
                lang_data[lang] = {}
                continue
            extractor = EXTRACTORS[lang]
            data = extractor(str(path))
            lang_data[lang] = data
            total = sum(len(methods) for methods in data.values())
            print(f"  {lang}: {len(data)} classes, {total} methods")

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
                merged = {}
                for methods in classes.values():
                    for name, sig in methods.items():
                        if name not in merged:
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
                canon = to_snake(name)
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
                counts = [param_count(m) for m in present.values()]
                if ret_mismatch or len(set(counts)) > 1:
                    mismatch_count += 1
                else:
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
