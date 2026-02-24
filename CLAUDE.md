# Claude Code Field Manual — Project Context

## Current Version
- **Version**: See `VERSION` file (currently v1.0.0)
- **Release date**: 2026-02-23
- **Changelog**: See `CHANGELOG.md`
- **All deliverables**: See `DELIVERABLES.md`

## What This Project Is
"Ofir's Claude Code Field Manual" — a free e-book teaching non-developers (marketing, sales, ops, revops) how to build real tools with Claude Code. Written by Ofir Bloch, SVP Corporate Marketing.

## Deployed Assets
- **Website**: https://manual.ofirbloch.com (GitHub Pages from `docs/`)
- **PDF**: 92 pages, landscape format (960x540, 16:9), ~19MB
- **PDF location**: `docs/Claude_Code_Field_Manual.pdf`
- **Landing page**: `docs/index.html`

## Repository Structure
- `design/` — Source HTML files for book and social assets
  - `book-landscape.html` — Current book source (landscape, generates 92-page PDF)
  - `book-complete-v2.html` — Legacy portrait version (72 pages, superseded)
  - `linkedin-carousel.html` — 9-slide LinkedIn carousel
  - `cover-v2.html`, `body-v2.html` — Cover and body page sources
- `docs/` — GitHub Pages deployment directory (this is what's live)
- `landing/` — Landing page source (mirrored to `docs/`)
- `outputs/illustrations/` — Book illustrations and persona source art
- `Final Manual/` — Original manuscript (`.docx`)
- `Raw Research/` — Research materials

## Technical Notes
- **Trailing space in path**: Working dir is `/Users/I754414/Downloads/Claude Code Manual /` — always quote paths
- **PDF generation**: Chrome headless print: `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=OUTPUT URL`
- **Page sizing**: Landscape uses `@page { size: 960px 540px; margin: 0; }`
- **Page overflow**: Use `overflow: hidden` on `.page` divs; split content rather than shrink
- **After page splits**: Update ALL subsequent page numbers + TOC references
- **Design spec**: See `.claude/skills/book-design/SKILL.md` for typography/color/spacing rules
- **Analytics**: Umami Analytics (website ID: a87a3b4e-5f12-4149-8660-a4b44c40100a)

## Versioning Rules
- Uses semantic versioning (major.minor.patch)
- Every release: update `VERSION`, `CHANGELOG.md`, `DELIVERABLES.md`, create git tag
- See `DELIVERABLES.md` for the monthly update checklist
- Git tags: `git tag -a vX.Y.Z -m "description"` then push

## Repos
- **Source**: `iscreamnofear/claude-code-field-manual`
- **Pages**: deployed from `docs/` directory via GitHub Pages
