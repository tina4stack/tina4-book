#!/usr/bin/env python3
"""
Tina4 API Reference Extractor
Extracts public classes and methods from all 4 Tina4 frameworks and outputs
a comparative markdown reference to API-REFERENCE.md
"""

import ast
import re
import os
from datetime import date
from pathlib import Path
from collections import defaultdict

BASE = Path("/Users/andrevanzuydam/IdeaProjects")

SOURCES = {
    "Python": BASE / "tina4-python/tina4_python",
    "PHP":    BASE / "tina4-php/Tina4",
    "Ruby":   BASE / "tina4-ruby/lib/tina4",
    "Node":   BASE / "tina4-nodejs/packages",
}

FEATURE_MAP = [
    ("ORM",        ["orm", "model", "base_model", "basemodel"]),
    ("Router",     ["router", "route"]),
    ("Database",   ["database", "db", "driver"]),
    ("Auth",       ["auth"]),
    ("Queue",      ["queue"]),
    ("Session",    ["session"]),
    ("Migration",  ["migration"]),
    ("GraphQL",    ["graphql"]),
    ("MCP",        ["mcp"]),
    ("Frond",      ["frond"]),
    ("Cache",      ["cache"]),
    ("WebSocket",  ["websocket", "ws"]),
    ("Events",     ["event"]),
    ("Template",   ["template"]),
    ("Misc",       []),  # catch-all
]

def classify(path):
    """
    Map a source file path to a feature area using keyword matching.

    For files named __init__.py (Python packages), the parent directory name
    is used instead of the filename so that e.g. tina4_python/auth/__init__.py
    is classified as Auth rather than Misc.
    """
    p = Path(path)
    # Use parent folder name for Python __init__.py files
    stem = p.stem.lower()
    if stem == "__init__":
        stem = p.parent.name.lower()
    name = stem.replace("-", "_")
    for area, keywords in FEATURE_MAP[:-1]:
        if any(kw in name for kw in keywords):
            return area
    return "Misc"


# ── Python extraction ─────────────────────────────────────────────────────────

def extract_python(src_dir):
    """
    Parse Python source files using the `ast` module.

    Extracts all public ClassDef nodes and their public methods (FunctionDef /
    AsyncFunctionDef whose names do not start with '_', excluding __init__).
    Method signatures include type annotations and default values as written in
    the source.

    Returns a dict[area -> list[{class, file, methods}]].
    """
    results = defaultdict(list)
    for path in sorted(src_dir.rglob("*.py")):
        if "__pycache__" in str(path):
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        rel = path.relative_to(src_dir)
        area = classify(path)
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            if node.name.startswith("_"):
                continue
            methods = []
            for item in node.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if item.name.startswith("_") and item.name != "__init__":
                    continue
                if item.name == "__init__":
                    continue
                args = item.args
                params = []
                all_args = args.args + args.posonlyargs
                defaults_offset = len(all_args) - len(args.defaults)
                for i, arg in enumerate(all_args):
                    if arg.arg in ("self", "cls"):
                        continue
                    annotation = ""
                    if arg.annotation:
                        try:
                            annotation = ": " + ast.unparse(arg.annotation)
                        except Exception:
                            pass
                    default = ""
                    di = i - defaults_offset
                    if di >= 0 and di < len(args.defaults):
                        try:
                            default = "=" + ast.unparse(args.defaults[di])
                        except Exception:
                            pass
                    params.append(f"{arg.arg}{annotation}{default}")
                if args.vararg:
                    params.append(f"*{args.vararg.arg}")
                for kwarg in args.kwonlyargs:
                    params.append(kwarg.arg)
                if args.kwarg:
                    params.append(f"**{args.kwarg.arg}")
                prefix = "async " if isinstance(item, ast.AsyncFunctionDef) else ""
                methods.append(f"{prefix}{item.name}({', '.join(params)})")
            if methods:
                results[area].append({
                    "class": node.name,
                    "file": str(rel),
                    "methods": methods,
                })
    return results


# ── PHP extraction ────────────────────────────────────────────────────────────

def extract_php(src_dir):
    """
    Parse PHP source files using regex.

    Extracts class names and `public` (including `public static`) function
    signatures. `__construct` is excluded. Parameter type hints are stripped
    to keep signatures readable; default values are preserved.

    Returns a dict[area -> list[{class, file, methods}]].
    """
    results = defaultdict(list)
    for path in sorted(src_dir.rglob("*.php")):
        content = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(src_dir)
        area = classify(path)
        class_matches = re.findall(r'(?:^|\s)(?:abstract\s+)?class\s+(\w+)', content)
        if not class_matches:
            continue
        method_matches = re.findall(
            r'public(?:\s+static)?\s+function\s+(\w+)\s*\(([^)]*)\)',
            content
        )
        methods = []
        for name, params_raw in method_matches:
            if name == "__construct":
                continue
            # Clean up param types to just names
            params = []
            for p in params_raw.split(","):
                p = p.strip()
                if not p:
                    continue
                # strip type hints: keep $name and default
                parts = p.split()
                var_part = next((x for x in parts if x.startswith("$")), p)
                default_match = re.search(r'=\s*(.+)$', p)
                default = " = " + default_match.group(1).strip() if default_match else ""
                params.append(f"{var_part}{default}")
            methods.append(f"{name}({', '.join(params)})")
        if methods:
            results[area].append({
                "class": class_matches[0],
                "file": str(rel),
                "methods": methods,
            })
    return results


# ── Ruby extraction ───────────────────────────────────────────────────────────

def extract_ruby(src_dir):
    """
    Parse Ruby source files using regex.

    Extracts the first class/module name per file and all `def` methods at
    class scope (up to 4 spaces of indentation). `initialize` and methods
    starting with `_` are excluded. Both instance methods (`def foo`) and
    class methods (`def self.foo`) are captured.

    Returns a dict[area -> list[{class, file, methods}]].
    """
    results = defaultdict(list)
    for path in sorted(src_dir.rglob("*.rb")):
        content = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(src_dir)
        area = classify(path)
        # Find module/class name
        class_match = re.search(r'(?:class|module)\s+([\w:]+)', content)
        if not class_match:
            continue
        class_name = class_match.group(1).split("::")[-1]
        # Find public methods (def ... or def self....)
        method_matches = re.findall(
            r'^\s{0,4}def\s+((?:self\.)?\w+)\s*[\(\n]([^)]*\))?',
            content, re.MULTILINE
        )
        # Also find attr_accessor / attr_reader exposed as API
        methods = []
        seen = set()
        for name, params_raw in method_matches:
            if name in ("initialize", "method_missing") or name.startswith("_"):
                continue
            if name in seen:
                continue
            seen.add(name)
            params = ""
            if params_raw:
                params = params_raw.strip().rstrip(")")
            methods.append(f"{name}({params})" if params else f"{name}")
        if methods:
            results[area].append({
                "class": class_name,
                "file": str(rel),
                "methods": methods,
            })
    return results


# ── TypeScript extraction ─────────────────────────────────────────────────────

def extract_typescript(src_dir):
    """
    Parse TypeScript source files using regex.

    Extracts exported class names and public/static/async method signatures.
    `.d.ts` declaration files and `node_modules` are skipped. Private methods
    and constructor are excluded. Parameter lists longer than 60 characters
    are truncated with `...` for readability.

    Returns a dict[area -> list[{class, file, methods}]].
    """
    results = defaultdict(list)
    for path in sorted(src_dir.rglob("*.ts")):
        if "node_modules" in str(path) or ".d.ts" in path.name:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(src_dir)
        area = classify(path)
        class_matches = re.findall(
            r'export\s+(?:abstract\s+)?class\s+(\w+)', content
        )
        if not class_matches:
            continue
        # Public methods: lines that have a method-like signature
        # Match: (public )?(static )?(async )?methodName(params): returnType
        method_matches = re.findall(
            r'^\s{0,4}(?:public\s+)?(?:static\s+)?(?:async\s+)?'
            r'([a-z]\w*)\s*[<(]([^)]*)\)',
            content, re.MULTILINE
        )
        methods = []
        seen = set()
        skip = {"constructor", "if", "for", "while", "switch", "catch", "return"}
        for name, params_raw in method_matches:
            if name in skip or name in seen:
                continue
            if name.startswith("_"):
                continue
            seen.add(name)
            # Shorten params: keep first 60 chars
            params = params_raw.strip()
            if len(params) > 60:
                params = params[:57] + "..."
            methods.append(f"{name}({params})")
        if methods:
            results[area].append({
                "class": class_matches[0],
                "file": str(rel),
                "methods": methods,
            })
    return results


# ── Render markdown ───────────────────────────────────────────────────────────

def render_markdown(all_data):
    """
    Render the extracted API data as a markdown document.

    Feature areas are output in the order defined by FEATURE_MAP. Within each
    area, frameworks appear in Python → PHP → Ruby → Node order. Each class
    gets its own table of method signatures.
    """
    lines = [
        "# Tina4 API Reference",
        "",
        f"> Auto-generated on {date.today().isoformat()}",
        "",
        "This document lists all public classes and methods extracted from the 4 Tina4 framework implementations.",
        "",
    ]

    # Collect all feature areas that have data
    all_areas = set()
    for lang_data in all_data.values():
        all_areas.update(lang_data.keys())

    area_order = [a for a, _ in FEATURE_MAP if a in all_areas]

    for area in area_order:
        has_any = any(area in lang_data for lang_data in all_data.values())
        if not has_any:
            continue
        lines.append(f"## {area}")
        lines.append("")

        for lang in ["Python", "PHP", "Ruby", "Node"]:
            entries = all_data.get(lang, {}).get(area, [])
            if not entries:
                continue
            for entry in entries:
                lines.append(f"### {lang} — `{entry['class']}` (`{entry['file']}`)")
                lines.append("")
                lines.append("| Method | ")
                lines.append("|--------|")
                for m in entry["methods"]:
                    lines.append(f"| `{m}` |")
                lines.append("")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Extracting Python...")
    python_data = extract_python(SOURCES["Python"])
    print(f"  Found {sum(len(v) for v in python_data.values())} classes")

    print("Extracting PHP...")
    php_data = extract_php(SOURCES["PHP"])
    print(f"  Found {sum(len(v) for v in php_data.values())} classes")

    print("Extracting Ruby...")
    ruby_data = extract_ruby(SOURCES["Ruby"])
    print(f"  Found {sum(len(v) for v in ruby_data.values())} classes")

    print("Extracting Node.js (TypeScript)...")
    node_data = extract_typescript(SOURCES["Node"])
    print(f"  Found {sum(len(v) for v in node_data.values())} classes")

    all_data = {
        "Python": python_data,
        "PHP":    php_data,
        "Ruby":   ruby_data,
        "Node":   node_data,
    }

    md = render_markdown(all_data)
    out = Path(__file__).parent / "API-REFERENCE.md"
    out.write_text(md, encoding="utf-8")
    print(f"\nWrote {out}")
    print(f"Size: {len(md):,} bytes")


if __name__ == "__main__":
    main()
