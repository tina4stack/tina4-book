# Chapter Reshuffle Plan

## Overview

Restructure all 4 books (Python, PHP, Ruby, Node.js) + tina4-documentation from 30 chapters to 37 chapters. Add 7 missing feature chapters. Reorder by importance: core framework first, niche last. Update VitePress sidebar to show grouped sections.

## New Chapter Structure (37 chapters)

### Foundations (01-10)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 01 | Getting Started | 01 | Keep |
| 02 | Routing | 02 | Keep |
| 03 | Request & Response | 03 | Keep |
| 04 | Templates (Frond) | 04 | Keep |
| 05 | Database | 05 | Keep |
| 06 | ORM | 06 | Keep |
| 07 | Query Builder | 12 | Renumber |
| 08 | Authentication | 07 | Renumber |
| 09 | Sessions & Cookies | 09 | Keep |
| 10 | Middleware & Security | 08+10 | Merge |

### Building Apps (11-19)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 11 | Caching | 16 | Renumber |
| 12 | Queues | 13 | Renumber |
| 13 | Events | — | **WRITE NEW** |
| 14 | Localization | — | **WRITE NEW** |
| 15 | Logging | — | **WRITE NEW** |
| 16 | Email (Messenger) | 15 | Renumber |
| 17 | Frontend & HtmlElement | 17 | Update — add HtmlElement section |
| 18 | Testing | 19 | Renumber |
| 19 | Scaffolding | 26 | Renumber |

### APIs & Protocols (20-24)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 20 | Swagger / OpenAPI | 11 | Renumber |
| 21 | API Client | — | **WRITE NEW** |
| 22 | GraphQL | 18 | Renumber |
| 23 | WebSocket | 14 | Renumber |
| 24 | WSDL / SOAP | — | **WRITE NEW** |

### Advanced (25-28)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 25 | DI Container | — | **WRITE NEW** |
| 26 | Service Runner | — | **WRITE NEW** |
| 27 | MCP Dev Tools | 27 | Keep |
| 28 | Custom MCP Servers | 28 | Keep |

### Developer Tools (29-31)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 29 | Dev Tools & Metrics | 20 | Renumber |
| 30 | CLI | 21 | Renumber |
| 31 | Vibe Coding with AI | 24 | Renumber |

### Operations (32-34)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 32 | Environment Variables | 25 | Renumber |
| 33 | Deployment | 22 | Renumber |
| 34 | Complete App | 23 | Renumber |

### Releases (35)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 35 | Releases | 30 | Renumber — top-level, not buried |

### Appendix (36-37)
| New # | Chapter | Old # | Action |
|-------|---------|-------|--------|
| 36 | Upgrading from v2 | 29 | Renumber (PHP/Python only) |
| 37 | Feature List (44 features) | — | **WRITE NEW** — the 44-feature list with descriptions |

---

## Execution Plan

### Phase 1: Rename existing files (all 4 books + all 4 docs = 8 directories)

Old → New filename mapping:

```
01-getting-started.md     → 01-getting-started.md      (keep)
02-routing.md             → 02-routing.md               (keep)
03-request-response.md    → 03-request-response.md      (keep)
04-templates.md           → 04-templates.md              (keep)
05-database.md            → 05-database.md               (keep)
06-orm.md                 → 06-orm.md                    (keep)
07-authentication.md      → 08-authentication.md         (renumber)
08-middleware.md           → DELETE (merge into 10)
09-sessions-cookies.md    → 09-sessions-cookies.md       (keep)
10-security.md            → DELETE (merge into 10)
11-swagger.md             → 20-swagger.md                (renumber)
12-query-builder.md       → 07-query-builder.md          (renumber)
13-queues.md              → 12-queues.md                 (renumber)
14-websocket.md           → 23-websocket.md              (renumber)
15-email.md               → 16-email.md                  (renumber)
16-caching.md             → 11-caching.md                (renumber)
17-frontend.md            → 17-frontend.md               (keep, update)
18-graphql.md             → 22-graphql.md                (renumber)
19-testing.md             → 18-testing.md                (renumber)
20-dev-tools.md           → 29-dev-tools.md              (renumber)
21-cli.md                 → 30-cli.md                    (renumber)
22-deployment.md          → 33-deployment.md             (renumber)
23-complete-app.md        → 34-complete-app.md           (renumber)
24-vibe-coding-with-ai.md → 31-vibe-coding-with-ai.md   (renumber)
25-environment-variables.md → 32-environment-variables.md (renumber)
26-scaffolding.md         → 19-scaffolding.md            (renumber)
27-mcp-dev-tools.md       → 27-mcp-dev-tools.md         (keep)
28-custom-mcp-servers.md  → 28-custom-mcp-servers.md     (keep)
29-upgrading-from-v2.md   → 36-upgrading-from-v2.md     (renumber)
30-releases.md            → 35-releases.md               (renumber)
```

### Phase 2: Create merged chapter

- **10-middleware-security.md** — merge old 08-middleware.md + 10-security.md into one chapter

### Phase 3: Write 8 new chapters (× 4 languages = 32 files)

| Chapter | Content source | Estimated size |
|---------|---------------|----------------|
| 13-events.md | Events.on/emit/once/off, priority, async examples | ~150 lines |
| 14-localization.md | JSON locale files, switching, interpolation, fallback | ~120 lines |
| 15-logging.md | Log levels, rotation, JSON output, env vars | ~100 lines |
| 21-api-client.md | get/post/put/delete, auth headers, SSL, error handling | ~150 lines |
| 24-wsdl-soap.md | Service class, @wsdl_operation, auto WSDL, lifecycle hooks | ~150 lines |
| 25-di-container.md | register, singleton, get, has, reset | ~100 lines |
| 26-service-runner.md | Background services pattern, start/stop lifecycle | ~100 lines |
| 37-feature-list.md | 44 features with descriptions, parity table | ~200 lines |

### Phase 4: Update HtmlElement in chapter 17

- Add HtmlElement section to all 4 books' 17-frontend.md (currently only in Python)

### Phase 5: Fix cross-references

- Grep all chapters for `Chapter \d+` or `chapter-\d+` references and update numbers
- Grep for links like `(05-database.md)` and update filenames

### Phase 6: Update VitePress sidebar

File: `tina4-documentation/docs/.vitepress/config.mts`

Add section grouping:
```typescript
const SECTION_GROUPS = {
  'Foundations': [1, 10],
  'Building Apps': [11, 19],
  'APIs & Protocols': [20, 24],
  'Advanced': [25, 28],
  'Developer Tools': [29, 31],
  'Operations': [32, 34],
  'Releases': [35, 35],
  'Appendix': [36, 37],
};
```

### Phase 7: Update tina4-documentation

Mirror all changes from tina4-book to tina4-documentation/docs/{python,php,ruby,nodejs}/

---

## Execution order

1. Phase 1 in tina4-book (rename files in all 4 book dirs)
2. Phase 2 in tina4-book (merge middleware + security)
3. Phase 3 in tina4-book (write 32 new chapter files)
4. Phase 4 in tina4-book (update frontend chapter)
5. Phase 5 in tina4-book (fix cross-references)
6. Commit + push tina4-book
7. Phase 7: mirror to tina4-documentation
8. Phase 6: update VitePress sidebar
9. Commit + push tina4-documentation

---

## Notes

- Ruby and Node have no v2 → chapter 36 only applies to Python and PHP books
- Releases (35) is top-level, not buried in Reference
- Upgrading from v2 (36) is the very last content chapter
- Each new chapter needs language-specific code examples for all 4 frameworks
- The 44-feature list in chapter 37 should match the parity matrix
