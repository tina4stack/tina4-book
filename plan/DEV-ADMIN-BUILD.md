# Tina4 Dev Admin — Unified SPA Build Plan

> **Created:** 2026-04-05 | **Repo:** tina4stack/tina4-dev-admin
> **Stack:** tina4-js + Vite | **Output:** single `tina4-dev-admin.js` bundle
> **Ships with:** all 4 frameworks (pre-built JS committed to each repo)

---

## Phase 1: Project Setup

- [ ] Init tina4-js + Vite project in `tina4-dev-admin/`
- [ ] Configure Vite for single-file IIFE bundle output
- [ ] Set up theme system — CSS variables from `data-framework` attribute
- [ ] Framework colors: Python #3b82f6, PHP #8b5cf6, Ruby #ef4444, Node #22c55e
- [ ] Create `api.ts` — fetch wrapper for `/__dev/api/*` endpoints
- [ ] Create `app.ts` — entry point, tab router, theme init
- [ ] Create minimal HTML test shell for local development

## Phase 2: Core UI Components

- [ ] `TabBar` — tab navigation with active state, badge counts
- [ ] `DataTable` — reusable sortable table component
- [ ] `Badge` — status badges (pending/completed/failed/reserved/auth/open)
- [ ] `Modal` — reusable modal dialog
- [ ] `CodeBlock` — syntax-highlighted code display
- [ ] `FilterBar` — filter buttons with active state
- [ ] `MetricCard` — system info card (label + value)
- [ ] `EmptyState` — "No data" placeholder

## Phase 3: Tab Components (14 tabs)

### Group A — Data Display (simple tables)

- [ ] **Routes** — table of method, path, auth, handler. Badge colors per HTTP method. Link to open route.
  - API: `GET /__dev/api/routes`

- [ ] **Requests** — HTTP request log with method, path, status, duration, size. Clear button.
  - API: `GET /__dev/api/requests`, `POST /__dev/api/requests/clear`

- [ ] **Messages** — application log with level badges, search, category filter.
  - API: `GET /__dev/api/messages`, `GET /__dev/api/messages/search`, `POST /__dev/api/messages/clear`

- [ ] **WebSockets** — active connections table with ID, path, IP, connected time. Disconnect button.
  - API: `GET /__dev/api/websockets`, `POST /__dev/api/websockets/disconnect`

### Group B — Interactive Panels

- [ ] **Queue** — jobs table with status filter (pending/completed/failed/reserved). Replay, retry, purge actions. Stats bar.
  - API: `GET /__dev/api/queue`, `POST /__dev/api/queue/retry`, `POST /__dev/api/queue/purge`, `POST /__dev/api/queue/replay`

- [ ] **Mailbox** — inbox/sent toggle. Message list with read modal. Seed and clear buttons.
  - API: `GET /__dev/api/mailbox`, `GET /__dev/api/mailbox/read`, `POST /__dev/api/mailbox/seed`, `POST /__dev/api/mailbox/clear`

- [ ] **Errors** — exception list with traceback. Resolve/clear actions. "Ask Tina4" button opens chat with error context.
  - API: `GET /__dev/api/broken`, `POST /__dev/api/broken/resolve`, `POST /__dev/api/broken/clear`

### Group C — Database & Tools

- [ ] **Database** — SQL query editor (textarea + Ctrl+Enter). Results table. Table browser sidebar. Paste data modal. Seed with fake data.
  - API: `POST /__dev/api/query`, `GET /__dev/api/tables`, `GET /__dev/api/table`, `POST /__dev/api/seed`

- [ ] **Connections** — database connection builder. Driver selector (SQLite/Postgres/MySQL/MSSQL/Firebird/MongoDB/ODBC). Dynamic form fields per driver. Test + save to .env.
  - API: `GET /__dev/api/connections`, `POST /__dev/api/connections/test`, `POST /__dev/api/connections/save`

- [ ] **Tools** — tool runner buttons: Carbon benchmark, test suite, route analyzer, migrations, seeders, AI detection. Output display.
  - API: `POST /__dev/api/tool`

### Group D — Visualization

- [ ] **Metrics** — quick stats grid (files, LOC, classes, functions, routes, templates). Bubble chart (SVG) — circle size = LOC, color = complexity. Click drill-down for per-file detail.
  - API: `GET /__dev/api/metrics`, `GET /__dev/api/metrics/full`, `GET /__dev/api/metrics/file`

- [ ] **System** — metric cards: uptime, memory, framework version, Python/PHP/Ruby/Node version, DB status, platform, CPU. Live timestamp.
  - API: `GET /__dev/api/system`

### Group E — AI Chat

- [ ] **Chat (Code With Me)** — message history, input field, provider config (TINA4_AI_URL). MCP tool execution. File change badges. Undo button. Offline fallback.
  - API: `POST /__dev/api/chat`, `POST /__dev/api/chat/undo`

## Phase 4: Chat / Code With Me Enhancement

- [ ] Configurable LLM endpoint: `TINA4_AI_URL`, `TINA4_AI_KEY`, `TINA4_AI_MODEL`
- [ ] Auto-detect Anthropic vs OpenAI-compatible API format from URL
- [ ] Backward compat with `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`
- [ ] System prompt with project context (routes, tables, templates, models)
- [ ] MCP tool definitions sent as LLM tools (file_read, file_write, file_list, database_query, etc.)
- [ ] Tool execution loop — handle tool_use responses, execute via MCP functions, send results back
- [ ] Auto-write files immediately (vibe coding), hot-reload picks up changes
- [ ] Undo support — snapshot files before writing, revert on undo
- [ ] File change badges in chat (show which files were created/modified)
- [ ] Offline fallback — regex-based answers when no API key set

## Phase 5: Toolbar

- [ ] Fixed toolbar at bottom of every page (injected by backend)
- [ ] Shows: request method, path, route count, framework version
- [ ] "Dashboard" button opens dev admin in overlay iframe
- [ ] Version check indicator
- [ ] Close button

## Phase 6: Build & Deploy

- [ ] Vite config for single IIFE bundle (`tina4-dev-admin.js`)
- [ ] `npm run build` produces `dist/tina4-dev-admin.js`
- [ ] `npm run deploy` script copies bundle to all 4 frameworks:
  - `tina4-python/tina4_python/public/js/tina4-dev-admin.js`
  - `tina4-php/src/public/js/tina4-dev-admin.js`
  - `tina4-ruby/lib/tina4/public/js/tina4-dev-admin.js`
  - `tina4-nodejs/packages/core/public/js/tina4-dev-admin.js`
- [ ] Each framework's `render_dashboard()` becomes minimal HTML shell (~10 lines)
- [ ] Delete ~2,500 lines inline HTML/CSS/JS from each framework (~10,000 lines removed total)
- [ ] Pre-built bundle committed to each framework repo

## Phase 7: Backend API Parity Check

- [ ] Verify all 32+ API endpoints return identical JSON format across all 4 frameworks
- [ ] Document any endpoint differences
- [ ] Fix any response format mismatches

## Phase 8: Testing

- [ ] Dev admin loads in all 4 frameworks
- [ ] All 14 tabs render and load data
- [ ] Framework color scheme applies correctly
- [ ] Chat works with Claude, OpenAI, and Ollama
- [ ] Code With Me creates files via MCP tools
- [ ] Undo reverts file changes
- [ ] Toolbar injection works on user pages
- [ ] Hot-reload works after file changes
- [ ] All 4 framework test suites pass (no regressions)

---

## API Endpoint Reference

| Endpoint | Method | Tab | Purpose |
|----------|--------|-----|---------|
| `/__dev/api/status` | GET | (global) | System status |
| `/__dev/api/routes` | GET | Routes | List routes |
| `/__dev/api/queue` | GET | Queue | List jobs |
| `/__dev/api/queue/retry` | POST | Queue | Retry failed |
| `/__dev/api/queue/purge` | POST | Queue | Purge by status |
| `/__dev/api/queue/replay` | POST | Queue | Replay job |
| `/__dev/api/mailbox` | GET | Mailbox | List messages |
| `/__dev/api/mailbox/read` | GET | Mailbox | Read message |
| `/__dev/api/mailbox/seed` | POST | Mailbox | Seed test data |
| `/__dev/api/mailbox/clear` | POST | Mailbox | Clear mailbox |
| `/__dev/api/messages` | GET | Messages | App log |
| `/__dev/api/messages/search` | GET | Messages | Search log |
| `/__dev/api/messages/clear` | POST | Messages | Clear log |
| `/__dev/api/query` | POST | Database | Execute SQL/GraphQL |
| `/__dev/api/tables` | GET | Database | List tables |
| `/__dev/api/table` | GET | Database | Table columns |
| `/__dev/api/seed` | POST | Database | Seed with fake data |
| `/__dev/api/requests` | GET | Requests | HTTP request log |
| `/__dev/api/requests/clear` | POST | Requests | Clear request log |
| `/__dev/api/broken` | GET | Errors | Exception list |
| `/__dev/api/broken/resolve` | POST | Errors | Mark resolved |
| `/__dev/api/broken/clear` | POST | Errors | Clear errors |
| `/__dev/api/websockets` | GET | WebSockets | Active connections |
| `/__dev/api/websockets/disconnect` | POST | WebSockets | Disconnect client |
| `/__dev/api/system` | GET | System | System info |
| `/__dev/api/chat` | POST | Chat | AI chat + MCP tools |
| `/__dev/api/chat/undo` | POST | Chat | Undo last file change |
| `/__dev/api/tool` | POST | Tools | Run dev tool |
| `/__dev/api/connections` | GET | Connections | Current DB config |
| `/__dev/api/connections/test` | POST | Connections | Test connection |
| `/__dev/api/connections/save` | POST | Connections | Save to .env |
| `/__dev/api/gallery` | GET | (Tools) | List examples |
| `/__dev/api/gallery/deploy` | POST | (Tools) | Deploy example |
| `/__dev/api/mtime` | GET | (toolbar) | File mtime for reload |
| `/__dev/api/version-check` | GET | (toolbar) | Check latest version |
| `/__dev/api/metrics` | GET | Metrics | Quick stats |
| `/__dev/api/metrics/full` | GET | Metrics | Full analysis |
| `/__dev/api/metrics/file` | GET | Metrics | Per-file detail |
