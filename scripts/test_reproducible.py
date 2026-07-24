#!/usr/bin/env python3
"""Regression test: the PDF build must be byte-reproducible.

Builds a book twice from the same sources and asserts the two PDFs are
identical byte-for-byte. No mocks — this runs the real build_pdf.py over
real chapter markdown and hashes the real output files.

Why this exists: reportlab stamps a wall-clock /CreationDate, /ModDate and
document /ID into every PDF by default. That made every rebuild produce
seven byte-different books even with no content change, so the docs-site
mirror in .github/workflows/build-pdfs.yml pushed a commit (and triggered a
Jenkins deploy of tina4.com) on every run. build_pdf.py pins the timestamp
via reportlab's invariant flag. If a future reportlab release, or an edit to
build_pdf.py, reintroduces any wall-clock or environment-dependent value,
this test fails instead of the churn quietly coming back.

Usage:  python3 scripts/test_reproducible.py [book.yml ...]
Exit 0 = reproducible, 1 = not.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILDER = REPO_ROOT / "scripts" / "build_pdf.py"

# One representative book by default — the JavaScript book is the smallest,
# so the two builds stay quick. Pass explicit book.yml paths to widen it;
# CI passes every book.
DEFAULT_BOOKS = ["book-5-javascript/book.yml"]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _output_path(book_yml: Path) -> str:
    """Read the `output:` line out of a book.yml without importing the builder."""
    for line in book_yml.read_text(encoding="utf-8").splitlines():
        if line.startswith("output:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"no output: key in {book_yml}")


def _build(book_yml: Path, env: dict[str, str]) -> Path:
    """Run the real builder and return the PDF it wrote."""
    result = subprocess.run(
        [sys.executable, str(BUILDER), str(book_yml)],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"build failed for {book_yml}:\n{result.stdout}\n{result.stderr}")

    # build_pdf.py prints "  wrote <relative path>  (NN KB, N headings)"
    for line in result.stdout.splitlines():
        if "wrote " in line:
            rel = line.split("wrote ", 1)[1].split("  (")[0].strip()
            return REPO_ROOT / rel
    raise SystemExit(f"could not find output path in builder output:\n{result.stdout}")


def check(book_yml_rel: str) -> bool:
    book_yml = REPO_ROOT / book_yml_rel
    if not book_yml.exists():
        print(f"  SKIP {book_yml_rel} (not found)")
        return True

    env = dict(os.environ)
    env.pop("SOURCE_DATE_EPOCH", None)  # exercise the built-in invariant path

    # The PDFs are tracked in git, so snapshot the committed copy BEFORE the
    # first build overwrites it and put it back at the end — this test must
    # not dirty the working tree.
    target = REPO_ROOT / _output_path(book_yml)
    original = None
    if target.exists():
        original = Path(tempfile.mkdtemp()) / target.name
        shutil.copy2(target, original)

    first = _build(book_yml, env)
    hash_one = _sha256(first)

    # Sleep past a clock tick and shift the timezone. A build that leaks
    # wall-clock time or local TZ into the file cannot survive both.
    time.sleep(1.1)
    env["TZ"] = "America/Chicago" if env.get("TZ") != "America/Chicago" else "Asia/Tokyo"

    second = _build(book_yml, env)
    hash_two = _sha256(second)

    if original is not None:
        shutil.copy2(original, target)  # restore the committed bytes
        shutil.rmtree(original.parent, ignore_errors=True)

    if hash_one == hash_two:
        print(f"  PASS {book_yml_rel}  {hash_one[:16]}")
        return True

    print(f"  FAIL {book_yml_rel}")
    print(f"       build 1: {hash_one}")
    print(f"       build 2: {hash_two}")
    print("       The build is not reproducible - unchanged books will churn")
    print("       the docs site on every CI run. Check that build_pdf.py still")
    print("       sets reportlab.rl_config.invariant before building.")
    return False


def main(argv: list[str]) -> int:
    books = argv[1:] or DEFAULT_BOOKS
    print("Checking PDF build reproducibility (building each book twice)...")
    failures = [b for b in books if not check(b)]
    if failures:
        print(f"\n{len(failures)} of {len(books)} book(s) NOT reproducible")
        return 1
    print(f"\nAll {len(books)} book(s) reproducible")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
