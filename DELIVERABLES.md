# Deliverables Inventory

Current version: **v1.0.0** (see `VERSION` file)
Last updated: 2026-02-24

---

## Production Assets (Live)

| # | Deliverable | Location | Status | Details |
|---|-------------|----------|--------|---------|
| 1 | **PDF (landscape)** | `docs/Claude_Code_Field_Manual.pdf` | Live | 92 pages, 960x540, ~19MB |
| 2 | **Landing page** | `docs/index.html` → manual.ofirbloch.com | Live | Mobile-first, book mockup hero |
| 3 | **CNAME** | `docs/CNAME` | Live | manual.ofirbloch.com |
| 4 | **Persona cards** | `docs/images/personas/` | Live | 4 PNGs: marketer, ops, sales, revops |
| 5 | **Author headshot** | `docs/ofir-headshot.png` | Live | Used in landing page author section |

## Source Files

| # | Deliverable | Location | Details |
|---|-------------|----------|---------|
| 6 | **Book HTML (landscape)** | `design/book-landscape.html` | Source for PDF generation |
| 7 | **Book HTML (portrait, legacy)** | `design/book-complete-v2.html` | 72-page portrait version (superseded) |
| 8 | **Cover design** | `design/cover-v2.html` | Cover page source |
| 9 | **Body pages** | `design/body-v2.html` | Body page source |
| 10 | **Landing page source** | `landing/index.html` | Mirrors `docs/index.html` |

## Social Media Assets

| # | Deliverable | Location | Status | Details |
|---|-------------|----------|--------|---------|
| 11 | **LinkedIn carousel** | `design/linkedin-carousel.html` | Needs update | 9 slides, 1080x1080. **Page count says 72 — needs update to 92** |
| 12 | **LinkedIn carousel PDF** | `design/linkedin-carousel.pdf` | Needs update | Exported version of carousel |
| 13 | **LinkedIn post copy** | Not saved | Missing | Post copy was created in a session but never committed. Needs recreation |

## Illustrations

| # | Deliverable | Location | Details |
|---|-------------|----------|---------|
| 14 | Cover hero | `outputs/illustrations/cover_hero.png` | Main cover illustration |
| 15 | Cover hero (wide) | `outputs/illustrations/cover_hero_wide.png` | Wide variant |
| 16 | Chapter: What Is It | `outputs/illustrations/chapter_part1_whatisit.png` | |
| 17 | Chapter: Cowork | `outputs/illustrations/chapter_part2_cowork.png` | |
| 18 | Chapter: Desktop | `outputs/illustrations/chapter_part3_desktop.png` | |
| 19 | Chapter: Prompting | `outputs/illustrations/chapter_part4_prompting.png` | |
| 20 | Chapter: Safety | `outputs/illustrations/chapter_part5_safety.png` | |
| 21 | Chapter: Troubleshoot | `outputs/illustrations/chapter_part6_troubleshoot.png` | |
| 22 | Playbooks | `outputs/illustrations/chapter_playbooks.png` | |
| 23 | Persona: Marketer | `outputs/illustrations/persona_marketer.png` | Source illustration |
| 24 | Persona: Ops | `outputs/illustrations/persona_ops.png` | Source illustration |
| 25 | Persona: Sales | `outputs/illustrations/persona_sales.png` | Source illustration |

## Strategy & Planning Docs

| # | Deliverable | Location | Details |
|---|-------------|----------|---------|
| 26 | LinkedIn plan | `LinkedIn_Plan_Final_Merged_5K_Sprint.md` | Sprint to 5K followers strategy |
| 27 | Project brief | `BRIEF.md` | Original design brief |
| 28 | Book review feedback | `book-review-feedback.md` | Editorial review notes |

---

## Known Issues

- [ ] LinkedIn carousel shows "72 pages" in 3 places — needs update to 92
- [ ] LinkedIn post copy was never saved to repo — needs recreation
- [ ] LinkedIn plan doc references "40 pages" — outdated, informational only

---

## Monthly Update Checklist

When releasing a new version:

1. **Bump version**: Update `VERSION` file (major.minor.patch)
2. **Update content**: Edit `design/book-landscape.html`
3. **Regenerate PDF**: Chrome headless print → `docs/Claude_Code_Field_Manual.pdf`
4. **Update landing page**: If page count or content structure changed, update `docs/index.html`
5. **Update carousel**: If page count changed, update `design/linkedin-carousel.html` and re-export PDF
6. **Write changelog**: Add entry to `CHANGELOG.md`
7. **Update this file**: Update deliverable statuses and details
8. **Git tag**: `git tag -a vX.Y.Z -m "description"` and push
9. **Social**: Create new LinkedIn post for the update

### Version bump guide
- **Major** (1.0→2.0): New edition, significant content overhaul, format change
- **Minor** (1.0→1.1): New playbooks, new chapters, new deliverables
- **Patch** (1.0.0→1.0.1): Typo fixes, image swaps, minor corrections
