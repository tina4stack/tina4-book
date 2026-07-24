#!/usr/bin/env bash
# Regenerate every tina4-book PDF from source markdown.
#
# Dependencies: Python 3 + the pinned versions in scripts/requirements.txt
# (`pip3 install --user -r scripts/requirements.txt`). Use the pins: the
# build is byte-reproducible, and a different reportlab/pillow could make
# your local rebuild differ from CI's and churn all seven PDFs.
#
# Output: PDF files alongside each book's chapters/ directory. .gitignore
# ignores *.pdf broadly but un-ignores each book's release PDF, so those
# seven ARE committed - they're what the docs-site mirror ships to
# tina4.com. CI regenerates and commits them on any chapter change.
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
