# Plan Folder — Tools

## `extract_api.py` — API Reference Extractor

Parses all 4 Tina4 framework codebases and generates a single comparative
`API-REFERENCE.md` listing every public class and its public methods, grouped
by feature area.

### Usage

```bash
cd /Users/andrevanzuydam/IdeaProjects/tina4-book/plan
uv run python extract_api.py
```

Re-run any time after code changes to refresh `API-REFERENCE.md`.

### What it extracts

| Framework | Language   | Parser           | Source directory                         |
|-----------|------------|------------------|------------------------------------------|
| Python    | Python     | `ast` module     | `tina4-python/tina4_python/`             |
| PHP       | PHP        | regex            | `tina4-php/Tina4/`                       |
| Ruby      | Ruby       | regex            | `tina4-ruby/lib/tina4/`                  |
| Node.js   | TypeScript | regex            | `tina4-nodejs/packages/`                 |

**Public** means:
- Python: methods not starting with `_` (dunder `__init__` excluded)
- PHP: methods declared `public` (private/protected excluded)
- Ruby: `def method_name` at class scope, excluding `initialize` and `_`-prefixed
- TypeScript: non-private methods on exported classes (`.d.ts` files excluded)

### Feature areas

Files are classified into areas by filename keyword matching:

| Area       | Keywords matched                         |
|------------|------------------------------------------|
| ORM        | `orm`, `model`, `base_model`             |
| Router     | `router`, `route`                        |
| Database   | `database`, `db`, `driver`               |
| Auth       | `auth`                                   |
| Queue      | `queue`                                  |
| Session    | `session`                                |
| Migration  | `migration`                              |
| GraphQL    | `graphql`                                |
| Cache      | `cache`                                  |
| WebSocket  | `websocket`, `ws`                        |
| Events     | `event`                                  |
| Template   | `template`, `frond`                      |
| Misc       | everything else                          |

### Output

`API-REFERENCE.md` — one table per class per framework, grouped by feature area.
Useful for spotting parity gaps: if a feature area shows entries for 3 frameworks
but not the 4th, that framework is missing the feature.

### Extending

To add a new feature area, append to the `FEATURE_MAP` list in `extract_api.py`
before the `("Misc", [])` catch-all entry:

```python
("NewArea", ["keyword1", "keyword2"]),
```
