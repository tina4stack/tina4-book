# Next Session Plan

## Priority 1: Brand Update
Apply `BRAND-GUIDE.md` across all repos:
- "TINA4 — The Intelligent Native Application 4ramework"
- "Simple. Fast. Human."
- "Built for AI. Built for you."
- Replace all "This is not a framework" / "This Is Now A 4Framework"
- Update CLI banners, welcome pages, READMEs, test headers, package descriptions, skills

## Priority 2: REPL across all frameworks
Ruby has `tina4ruby console` (IRB). Add equivalent to:
- Python: `tina4python console` → drops into Python REPL with framework loaded
- PHP: `tina4php console` → drops into PsySH or similar with framework loaded
- Node: `tina4nodejs console` → drops into Node REPL with framework loaded
- Rust CLI: `tina4 console` → delegates to language-specific console

## Priority 3: Archive old repos
Archive these v2 split packages (all merged into tina4-php v3):
- tina4php-core, tina4php-database, tina4php-orm, tina4php-sqlite3
- tina4php-mysql, tina4php-postgresql, tina4php-firebird, tina4php-mssql
- tina4php-odbc, tina4php-mongodb, tina4php-pdo, tina4php-graphql
- tina4php-queue, tina4php-session, tina4php-env, tina4php-debug
- tina4php-localization, tina4php-reports, tina4php-shape

Archive these inactive/legacy repos:
- Faker, Jupyter-PHP, Jupyter-PHP-Installer, Magento-v2.x
- Pascal-gzip, d3-cloud, nusoap, preact, mORMot, co2-checker

Decide on: tina4-cms, tina4-module, tina4-store, tina4php-shopify, ThoughtDB, thought

## Priority 4: Fix cross-references (Phase 5)
Chapter numbers changed in the reshuffle. Grep all chapters for chapter references and update.

## Priority 5: VitePress template syntax
Apply HTML entity encoding (&#36; for $, &#123;&#123; for {{) to all template chapters across Python/PHP/Ruby/Node docs.

## Priority 6: Content review
Run content-writer skill on the 7 new chapters to check prose quality.

## Priority 7: Metrics test coverage
Investigate how metrics badges/colours work, fix test detection patterns.

## Priority 8: tina4js welcome page
Verify branded welcome page works with `tina4 init tina4js`.

## Priority 9: npm publish
Sync npm package version (root package.json) with releases.
