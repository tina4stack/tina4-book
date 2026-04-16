#!/usr/bin/env bash
# Regenerate every tina4-book PDF from source markdown.
#
# Dependencies: Python 3 + reportlab (`pip3 install --user reportlab`).
# Output: PDF files alongside each book's chapters/ directory. PDFs are
# gitignored; regenerate whenever chapter content changes.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build_pdf.py \
  book-0-understanding/book.yml \
  book-1-python/book.yml \
  book-2-php/book.yml \
  book-3-ruby/book.yml \
  book-4-nodejs/book.yml \
  book-5-javascript/book.yml \
  book-6-delphi/book.yml

echo
echo "Generated:"
find . -maxdepth 2 -name '*.pdf' -not -path './node_modules/*' -type f \
  -exec ls -lh {} \; \
  | awk '{printf "  %6s  %s\n", $5, $9}' \
  | sort -k2
