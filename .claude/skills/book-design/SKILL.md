---
name: book-design
description: Design and produce the Claude Code Field Manual e-book. Use when building any book page — cover, chapter opener, body page, playbook, appendix. Enforces the visual identity system, typography, spacing, icons, and illustration rules. Handles HTML page production with print-quality design.
allowedTools:
  - Bash
  - Read
  - Write
  - Edit
---

## Identity

This book is the **Claude Code Field Manual** — a practical guide for non-technical professionals. The design must feel premium, approachable, and distinctive. Not corporate. Not developer-bro. Not a whitepaper.

The visual identity is built on ONE repeatable motif: **the field guide metaphor**. Every visual element reinforces the idea that this is a trusted companion you take into unfamiliar territory — like a bird-watching field guide, but for building things with AI.

## The Signature System

### The Motif: Corner Brackets

Every page, every callout, every chapter opener uses **corner brackets** `⌜ ⌝ ⌞ ⌟` as the recurring structural element. They appear as:
- Decorative corners on chapter opener title frames
- Accent marks flanking section numbers
- Border treatment on callout boxes (top-left + bottom-right corners only, not full borders)
- The cover frame element

This single geometric motif creates recognition across every page. It says: "You're in the Field Manual."

### The Icon System

Eight custom SVG line icons replace emojis in callout boxes. All icons share:
- 24×24 viewBox
- 2px stroke weight
- Round linecap and linejoin
- Single color (inherits from callout title color via `currentColor`)
- No fill, stroke only

See `assets/icons/` for the SVG files. Icon assignments:
- `skull.svg` → I LEARNED THIS THE HARD WAY
- `stopwatch.svg` → SAVE YOURSELF 45 MINUTES
- `flame.svg` → THIS WILL BREAK THINGS
- `eye.svg` → REALITY CHECK
- `lightbulb.svg` → WORTH KNOWING
- `alert-triangle.svg` → DO NOT SKIP THIS
- `message-circle.svg` → JARGON BUSTER
- `clipboard.svg` → COPY THIS EXACTLY

### Difficulty Pips

Playbook difficulty uses filled/empty circles instead of star emojis:
- ⭐ → `●○○` (one filled, two empty)
- ⭐⭐ → `●●○`
- ⭐⭐⭐ → `●●●`

Rendered as small SVG circles, 8px diameter, 4px gap, filled circles use `--teal`.

## Page Types

### 1. Cover Page
- Dark background (`--ink-deep`)
- Corner bracket frame (thin lines, teal, inset 40px from edges)
- Title: Inter 54px/900, "Claude Code" in teal, rest in white
- Subtitle: Lora 16px/400, muted white
- Teal accent rule (60px wide, 3px)
- Meta line: author, playbook count, tagline
- Bottom: horizontal illustration band (max-height 280px, blended into background with gradient mask on top edge)
- Grid overlay (40px, 2.5% white opacity)

### 2. Chapter Opener (Dark Page)
- Dark background (`--ink-deep`)
- Corner bracket frame (same as cover, but smaller — inset 32px)
- Part number: Inter 12px/700, teal, 3px letter-spacing, uppercase
- Chapter title: Inter 38px/800, white
- Chapter description: Lora 16px, muted
- Contents list: Inter 12px, muted, teal dot bullets
- Illustration: positioned bottom-right, max 320px wide, masked into background with gradient
- NO floating images pasted onto the page. Illustrations must be COMPOSITED — gradients mask their edges into the background.

### 3. Body Page (White Page)
- White background
- Running header: left = "Part N — Chapter Name", right = "Claude Code Field Manual"
  - Inter 10px, uppercase, 1.5px letter-spacing, `--muted` color, 28px from top
- Content area: 672px wide (72px margins each side)
- Page number: centered bottom, Inter 11px, `--muted`, 28px from bottom
- Section divider: horizontal rule with centered teal diamond

### 4. Playbook Page
- Same as body page structure
- Project header: teal "PROJECT XX" label + difficulty pips
- Metadata table: Who / What you get / Tool / Time
- Tool tags: pill badges (teal bg for Cowork, purple bg for Claude Code Desktop)

### 5. Table of Contents
- Dark background
- Corner bracket frame
- Two-column layout: Parts on left, page numbers right
- Teal accent for current/active part
- Playbook entries indented with difficulty pips

## Typography

| Element | Font | Size | Weight | Line-height | Tracking | Color |
|---------|------|------|--------|-------------|----------|-------|
| Chapter title (dark) | Inter | 38px | 800 | 1.15 | -1px | white |
| H2 (body) | Inter | 24px | 800 | 1.25 | -0.5px | `--ink` |
| H3 (body) | Inter | 17px | 700 | 1.35 | 0 | `--ink` |
| Body text | Lora | 14px | 400 | 1.75 | 0 | `--text` |
| Callout title | Inter | 11px | 700 | 1 | 1.2px | callout accent |
| Callout body | Lora | 13px | 400 | 1.65 | 0 | `--text` |
| Code | JetBrains Mono | 12px | 400 | 1.7 | 0 | `#E2E8F0` on `--ink` |
| Running header | Inter | 10px | 500 | 1 | 1.5px | `--muted` |
| Page number | Inter | 11px | 500 | 1 | 0 | `--muted` |
| Table header | Inter | 11px | 600 | 1 | 0.8px | `--text-light` |
| Table body | Lora | 12.5px | 400 | 1.5 | 0 | `--text` |

## Color System

### Light pages (body)
| Token | Hex | Purpose |
|-------|-----|---------|
| `--ink` | #1B2332 | Headings, strong emphasis |
| `--text` | #2D3748 | Body text |
| `--text-light` | #4A5568 | Secondary text, table headers |
| `--muted` | #A0AEC0 | Running headers, page numbers, captions |
| `--rule` | #E2E8F0 | Dividers, table borders |
| `--bg` | #F7FAFC | Page background (subtle warmth vs pure white) |

### Dark pages (cover, chapter openers)
| Token | Hex | Purpose |
|-------|-----|---------|
| `--ink-deep` | #0F1520 | Background |
| Grid lines | rgba(255,255,255,0.025) | Subtle structure |
| Glows | teal 15% / purple 12% opacity | Ambient depth |

### Callout accent colors (border + title)
| Callout | Accent | Background |
|---------|--------|------------|
| HARD WAY | #553C9A | #FAF5FF |
| TIMESAVER | #B7791F | #FFFFF0 |
| DANGER | #C53030 | #FFF5F5 |
| REALITY | #276749 | #F0FFF4 |
| WORTH KNOWING | #2B6CB0 | #EBF8FF |
| DO NOT SKIP | #0987A0 | #E6FFFA |
| JARGON | #2B6CB0 | #EBF8FF |
| COPY THIS | #276749 | #F0FFF4 |

### Accent
| Token | Hex | Purpose |
|-------|-----|---------|
| `--teal` | #0987A0 | Primary accent. Links, highlights, "Claude Code" in title, corner brackets, difficulty pips |

## Spacing Scale (8px base)

4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 · 64 · 72

### Application
- Page margin horizontal: 72px
- Page margin top: 64px
- Page margin bottom: 56px
- H2 top margin: 32px
- H3 top margin: 24px
- Paragraph spacing: 12px
- Callout padding: 20px vertical, 24px horizontal
- Callout margin: 24px vertical
- Code block margin: 20px vertical
- Code block padding: 20px 24px

## Callout Box Rendering

```
┌─ corner bracket (top-left only, teal accent color, 12px arms)
│
│  [SVG ICON 20px]  CALLOUT TITLE (Inter 11px/700, uppercase, 1.2px tracking)
│
│  Callout body text (Lora 13px/400, --text color)
│  Can be multiple lines.
│
│                                          corner bracket (bottom-right only) ─┘
```

- Background: callout-specific bg color
- Border: NONE (no full border, no left accent bar)
- Corner brackets: 2px stroke, 12px arm length, callout accent color, top-left and bottom-right only
- Icon: SVG from icon set, sized 20px, callout accent color
- Radius: 6px on the background shape

## Code Block Rendering

```
╭─── ● ● ●  ─────────────────────────── filename.ext ───╮
│                                                          │
│  code content here                                       │
│  with syntax highlighting                                │
│                                                          │
╰──────────────────────────────────────────────────────────╯
```

- Background: `--ink` (#1B2332)
- Border-radius: 8px
- Title bar: `--ink-deep`, 3 colored dots (red/yellow/green), filename right-aligned
- Content: JetBrains Mono 12px, `#E2E8F0` base, syntax colors:
  - Comment: #718096
  - String: #68D391
  - Keyword: #B794F4
  - Flag: #63B3ED

## Illustration Integration Rules

1. NEVER paste a raw image onto a page. Always composite:
   - Gradient mask on at least one edge (fade into background)
   - Consistent border-radius (12px)
   - Brightness/contrast filter: brightness(1.03) contrast(1.02)
2. Chapter opener illustrations: bottom-right, max 320px wide, gradient mask on top and left edges
3. Cover illustration: horizontal band, gradient mask on top edge, max 280px tall
4. Body page illustrations: centered, max 500px wide, subtle drop shadow
5. All illustrations must use the same Nano Banana prompt style suffix:
   "Clean-line isometric style, minimal detail, 2-3 tone block shading, teal (#0987A0) and purple (#553C9A) accents on dark navy (#0F1520) background. No text, no watermark, no words."

## Quality Checklist (Run After Every Page)

- [ ] Margins match spec (72px horizontal, 64px top, 56px bottom)
- [ ] Running header present and correctly formatted
- [ ] Page number present and centered
- [ ] Typography matches scale (no ad-hoc sizes)
- [ ] Corner bracket motif present where required
- [ ] Callout boxes use SVG icons, not emojis
- [ ] Callout boxes use corner bracket treatment, not left border
- [ ] Code blocks have title bar with dots
- [ ] All colors from the defined palette (no ad-hoc colors)
- [ ] Spacing follows 8px scale
- [ ] Illustrations composited with gradient masks
