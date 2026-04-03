# Tina4 Brand Guide

## The Name

**TINA4** — **T**he **I**ntelligent **N**ative **A**pplication **4**ramework

## The Tagline

**Simple. Fast. Human.**

## The Subtitle

**The Intelligent Native Application 4ramework**

## The Philosophy

Most frameworks are designed for humans. Tina4 is designed for both — the human developer and the AI assistant working alongside them.

- **Intelligent** — the framework understands AI. CLAUDE.md ships with every project. AI tools know the conventions, the structure, the API. No guessing.
- **Native** — zero runtime dependencies. Built from scratch in each language using only the standard library. Not a wrapper. Not a port. Native.
- **Application** — this builds real production applications. Routing, ORM, auth, queues, WebSocket, email, GraphQL — 44 features, all included.
- **4ramework** — four languages (Python, PHP, Ruby, Node.js), one API. Learn once, build anywhere. The "4" is both the number and "for" — a framework *for* developers.

## The Differentiator

> The framework that gets out of the way — for humans AND for AI.

Consistent conventions mean the AI never guesses wrong. Zero dependencies mean the AI never picks the wrong package. Convention over configuration means the AI always knows where things go. One CLAUDE.md file means the AI has complete framework knowledge from the first prompt.

## Usage Rules

### Always use
- "TINA4" or "Tina4" (capitalised)
- "The Intelligent Native Application 4ramework" (full subtitle)
- "Simple. Fast. Human." (tagline)
- "Built for AI. Built for you." (closing line)

### In code banners (CLI, welcome pages, server startup)
```
Tina4 {Language} v{version} — The Intelligent Native Application 4ramework
```

### In README headers
```markdown
<h3 align="center">The Intelligent Native Application 4ramework</h3>
```

### In package descriptions
```
Tina4 for {Language} — The Intelligent Native Application 4ramework
```

### In test file headers
```
Tina4 — The Intelligent Native Application 4ramework
```

### Never use
- "This is not a framework" (retired)
- "This Is Now A 4Framework" (retired)
- "not a 4ramework" (retired)

## Where to Apply

### Code (server banners, welcome pages, CLI output)
- tina4-python: `server.py` banner, welcome page HTML
- tina4-php: `bin/tina4php` banner, `Server.php` welcome page, all test file headers
- tina4-ruby: `tina4.rb` banner, `rack_app.rb` welcome page
- tina4-nodejs: `server.ts` banner + welcome page, `bin.ts` help, `init.ts` scaffold, `package.json` descriptions

### READMEs
- tina4-python/README.md
- tina4-php/README.md (if exists)
- tina4-ruby/README.md
- tina4-nodejs/README.md
- tina4-js/readme.md
- tina4/README.md (Rust CLI)

### Documentation
- tina4-book/book-0-understanding/ (philosophy chapter)
- tina4-documentation/docs/general/ (what is tina4, index)
- tina4-documentation/docs/.vitepress/config.mts (site description)
- tina4-documentation/docs/index.md (landing page tagline)

### Skills (CLAUDE.md / AI context)
- All 4 frameworks' `.claude/skills/tina4-maintainer/SKILL.md`
- All 4 frameworks' `.claude/skills/tina4-developer/SKILL.md`
- All 4 frameworks' `CLAUDE.md`

### Rust CLI
- tina4/src/init.rs (scaffold welcome pages)
- tina4/Cargo.toml (description)
