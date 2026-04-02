# Chapter Reshuffle Plan

## New Chapter Structure (36 chapters, 7 new)

### Foundations (1-10)
| # | Chapter | Source | Status |
|---|---------|--------|--------|
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
| # | Chapter | Source | Status |
|---|---------|--------|--------|
| 11 | Caching | 16 | Renumber |
| 12 | Queues | 13 | Renumber |
| 13 | Events | — | **NEW** |
| 14 | Localization | — | **NEW** |
| 15 | Logging | — | **NEW** |
| 16 | Email | 15 | Renumber |
| 17 | Frontend & HtmlElement | 17 | Update (add HtmlElement) |
| 18 | Testing | 19 | Renumber |
| 19 | Scaffolding | 26 | Renumber |

### APIs (20-24)
| # | Chapter | Source | Status |
|---|---------|--------|--------|
| 20 | Swagger / OpenAPI | 11 | Renumber |
| 21 | API Client | — | **NEW** |
| 22 | GraphQL | 18 | Renumber |
| 23 | WebSocket | 14 | Renumber |
| 24 | WSDL / SOAP | — | **NEW** |

### Advanced (25-28)
| # | Chapter | Source | Status |
|---|---------|--------|--------|
| 25 | DI Container | — | **NEW** |
| 26 | Service Runner | — | **NEW** |
| 27 | MCP Dev Tools | 27 | Keep |
| 28 | Custom MCP Servers | 28 | Keep |

### Developer Tools (29-31)
| # | Chapter | Source | Status |
|---|---------|--------|--------|
| 29 | Dev Tools & Metrics | 20 | Renumber |
| 30 | CLI | 21 | Renumber |
| 31 | Vibe Coding with AI | 24 | Renumber |

### Reference (32-36)
| # | Chapter | Source | Status |
|---|---------|--------|--------|
| 32 | Environment Variables | 25 | Renumber |
| 33 | Deployment | 22 | Renumber |
| 34 | Complete App | 23 | Renumber |
| 35 | Upgrading from v2 | 29 | Renumber (PHP/Python only) |
| 36 | Releases | 30 | Renumber |

## Files to update
- 4 books × 36 chapters = rename/renumber files
- 4 docs × 36 chapters = rename/renumber files
- VitePress sidebar config: docs/.vitepress/config.mts
- Cross-references within chapters
- 7 new chapters to write (all 4 languages each = 28 new files)

## New chapters content needed
1. **Events** — on/emit/once/off, priority, async, use cases
2. **Localization** — JSON files, locale switching, interpolation, fallback
3. **Logging** — levels, rotation, JSON output, env vars
4. **API Client** — get/post/put/delete, auth, headers, SSL, error handling
5. **WSDL/SOAP** — service class, @wsdl_operation, auto WSDL generation
6. **DI Container** — register, singleton, get, has, reset
7. **Service Runner** — background services pattern

## VitePress sidebar groups
```
Foundations
Building Apps
APIs
Advanced
Developer Tools
Reference
```
