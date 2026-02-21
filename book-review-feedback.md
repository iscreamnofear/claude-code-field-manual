# The Claude Code Field Manual — Production Review

**Reviewer perspective:** Editor-in-chief / senior book designer with 15+ years at publishers like A Book Apart, Stripe Press, Intercom.

**File reviewed:** `book-complete.html` (1,663 lines, 42 numbered pages + front/back matter + 7 chapter openers)

---

## 1. EDITORIAL REVIEW

### Structure completeness

The manuscript covers the promised structure: 6 Parts, 10 Playbooks, and an Appendix with glossary, pricing, and links. All sections in the TOC are accounted for in the body content. Nothing is truncated mid-sentence.

**Missing content, however, is a real problem.** Several Parts have far too little body content for the page range implied by the TOC:

- **Part 1 ("What Is This Thing?")** — 1 body page. The TOC allocates pages 5–7 (3 pages). You have maybe 60% of what this section needs. The "What's the difference between Claude, Cowork, and Claude Code" section deserves a comparison table or visual breakdown, not just a jargon callout. Missing: a clearer explanation of the three products with a visual, and a "what you'll learn in each part" orientation.
- **Part 2 ("Start Here: Cowork")** — 2 body pages (numbered 8 and 10, page 9 is missing). Adequate but thin. The "Ten things Cowork is great at" list is a solid numbered list, but it reads as a wall of text. A table or visual grid would serve better.
- **Part 5 ("The Safety Stuff")** — 1 body page. For a section the TOC explicitly flags as "please don't skip this," one page feels underweight. The golden rules at the end are good, but they're crammed at the bottom with no breathing room.

### Voice and authenticity

The writing is strong. The author's voice is consistent, direct, and genuinely un-AI-like. Lines like "Claude responds to precision the way a dog responds to a thrown ball" and "six weeks of 'it's in the backlog'" sound like a real person who has used this tool and is frustrated by the right things. No paragraphs read as AI filler.

One exception: the legal disclaimer page (page 3) is boilerplate, which is fine for legal, but it's also a full dark page that adds visual weight without reader value. Consider making it a half-page at the bottom of the "What's Inside" page.

### Callout box content and type accuracy

Callout types are well-deployed overall. Specific notes:

- **All "Reality Check" callouts are correctly typed.** They provide grounding, deflating hype without being cynical. These are the best callouts in the book.
- **"Save Yourself 45 Minutes" on page 8** (Cowork section, "if you don't see the Cowork tab, update your app") — this is really a "Worth Knowing" or a plain tip. It doesn't save 45 minutes. Retype it.
- **"Worth Knowing" on page 5** (pricing info) — this is a duplicate of content already in the Appendix pricing table. Consider cutting it or making it a brief cross-reference: "See Appendix for full pricing."
- **"Copy This Exactly" callouts** are consistently excellent. The prompt templates are the single most valuable content in this book. They justify the download.

### Page flow and navigation

The reader always knows where they are, thanks to consistent running headers and the chapter opener → body page pattern. The chapter openers serve as effective section dividers.

**One flow problem:** Part 4 ("Talking to Claude") jumps from "Bad ask vs. good ask" on page 18 directly to "The five rules" on page 19, then to "How to give feedback mid-project" on page 20 (shown as 21). The pages labeled 18 and 19 are dense. Page 18 has two code blocks and a callout; page 19 has two callouts, a code block, and five H3s. The reader needs a breath. Split the five rules across two pages and give each rule an example.

### Running headers

Running headers are accurate on every page reviewed. The format is consistent: `Part X — Section Title` on the left, `Claude Code Field Manual` on the right. Playbook pages correctly use `Projects — The Playbooks`. Appendix pages correctly use `Appendix`. No errors found.

---

## 2. TYPOGRAPHIC HIERARCHY

### Font pairing assessment

**Inter / Lora / JetBrains Mono works.** It's a proven combination. Inter provides clean authority for headings, Lora provides warmth and readability for body text, JetBrains Mono gives code blocks instant recognition. No conflicts.

One concern: Lora at 14px renders with thin strokes on some screens at lower resolutions. At PDF zoom levels below 100%, body text could feel faint. Consider testing at 15px.

### Size and weight hierarchy

- **H2 (24px/800)** — Strong, clear, good. The -0.5px letter-spacing tightens it nicely.
- **H3 (17px/700)** — This is the weak link. At 17px bold, H3s are too close to body text (14px/400) in visual weight. The 7px size jump isn't enough when the body text is a serif (Lora) and the heading is a sans (Inter) — the serif's x-height and stroke contrast make 14px Lora feel bigger than it is. **Fix: Bump H3 to 18px or add a teal accent (color, left border, or small teal pip) to differentiate.**
- **Body text (14px Lora/1.75 line-height)** — Comfortable for sustained screen reading at 100% zoom. The 1.75 line-height is generous and appropriate. This is well-calibrated.
- **Callout titles (11px/700 uppercase, 1.2px letter-spacing)** — Readable at full zoom. At 75% zoom (common for PDFs), they'll be strained. **Bump to 11.5px or 12px.** The letter-spacing helps, but the titles need to survive zoom.
- **Callout body text (13px Lora/1.65)** — Slightly small. The jump from 14px body to 13px callout is noticeable but not problematic. This is fine.

### Spacing

- **Paragraph spacing (12px margin-bottom)** — Tight but workable. Paragraphs followed by callouts get 24px of callout margin, which provides relief. Consecutive paragraphs could use 14–16px margin-bottom.
- **H2 margin (32px top, 14px bottom)** — Good top spacing. The 14px bottom margin is too tight — when an H2 is followed by a paragraph, there's barely more space below the heading than between body paragraphs. **Bump H2 margin-bottom to 18–20px.**
- **H3 margin (24px top, 8px bottom)** — 8px bottom margin makes the H3 hug its following paragraph. This is intentional for tight binding, but it reads as cramped. **Bump to 10–12px.**

### Consistency

Type sizes are consistent throughout. I found no deviations from the defined system. The inline styles on some pages (e.g., `style="margin-top: 8px;"` on nearly every first H2) are a CSS smell but don't affect rendering consistency.

---

## 3. LAYOUT & SPACING

### Margins

72px margins on an 816px page = 672px content width. This is generous and appropriate for a single-column PDF read on screen. It feels premium, not wasteful. Do not reduce.

### Content density

**Uneven density is the biggest layout issue.** Some pages are packed (page 19 with five H3s, two callouts, and a code block), while others have significant whitespace at the bottom (page 30, Competitive Intel Tracker). The playbook pages are particularly inconsistent — some playbooks get two full pages (Playbook 01: pages 26–27), while most get a fraction of a shared page.

- **Pages 18–19:** Too dense. The five prompt rules on page 19 need more vertical space.
- **Page 23 (Safety golden rules):** Content ends mid-page. This is the end of Part 5, and it trails off.
- **Pages 33–34:** Playbooks 07 and 08 share a page. They're brief, which is fine, but the visual rhythm breaks because Playbook 01 got two pages and these get half a page each.

### Callout and table integration

Callouts feel well-integrated. The 24px vertical margin keeps them from crowding surrounding text. The left-icon + body layout reads cleanly.

Tables are clean and legible. The mode table on page 13 (dark header, light rows) is the best-designed table element in the book.

**Code blocks** interrupt the reading flow slightly. The full-bleed dark background on code blocks creates a stark contrast that makes the eye jump. Consider adding 4px of border-radius on the inner code-body as well, or reducing the code-body padding from the current value to tighten the block visually.

### Vertical rhythm

The spacing scale is roughly: 8, 12, 14, 20, 24, 32, 48px. It's close to a consistent scale but isn't strictly following one. The divider element (diamond + line) at 32px vertical margin provides good section separation. The issue is that some elements use 20px (code blocks, tables) while others use 24px (callouts), creating micro-inconsistencies. Standardize around: 12, 16, 24, 32, 48.

### Playbook metadata stack

The playbook structure (Project label + pips → H2 title → italic subtitle → metadata table → prompt callout → notes) stacks well on pages 26–27 (Playbook 01). It feels designed. But when compressed (playbooks 07–10), the metadata table + brief content feels skeletal. Those playbooks need either more content or a different layout (e.g., two-column cards).

---

## 4. DESIGN SYSTEM CONSISTENCY

### Corner bracket motif

The corner brackets work on dark pages (cover, chapter openers) where they frame the content and echo a "targeting" or "field manual" aesthetic. They reinforce the book's title metaphor. On the cover, the teal bracket corners at 0.4 opacity are subtle and effective.

**Concern:** The brackets don't appear on white body pages. This is fine — body pages shouldn't be over-decorated — but it means the motif disappears for long stretches (up to 10+ pages). Consider adding a very subtle bracket or bracket fragment to the page number area or running header to maintain the thread.

### Callout type differentiation

Eight callout types, each with distinct background + border color:

| Type | Color | Distinguishable? |
|------|-------|-------------------|
| Hard Way (purple) | ✓ Distinct | Yes — the robot icon + purple is unique |
| Time Saver (amber) | ✓ Distinct | Yes |
| Danger (red) | ✓ Distinct | Yes — the flame icon sells it |
| Reality Check (green) | ⚠️ Overlap | Shares green-bg with "Copy Exact" |
| Worth Knowing (blue) | ⚠️ Overlap | Shares blue-bg with "Jargon Buster" |
| Don't Skip (teal) | ✓ Distinct | Yes |
| Jargon Buster (blue) | ⚠️ Overlap | Same blue-bg as "Worth Knowing" |
| Copy Exact (green) | ⚠️ Overlap | Same green-bg as "Reality Check" |

**Problem: Four callout types share only two background colors.** "Worth Knowing" and "Jargon Buster" are both blue. "Reality Check" and "Copy Exact" are both green. At a glance (which is how readers scan callouts), you can't tell them apart. The titles help, but the colors should be doing that work.

**Fix:** Give "Jargon Buster" a distinct color (a warm gray, or desaturated indigo like `#EDE9FE`). Give "Copy Exact" a distinct treatment — a dashed or double border, or a different background (pale teal vs. pale green).

### Difficulty pips

The pips (`●●○`) at 8px with 1.5px teal borders read clearly at 100% zoom. At smaller sizes, the hollow pips might be hard to distinguish from filled ones. Consider increasing pip size to 10px or using a filled-but-lighter color for empty pips instead of just a border.

### Teal accent

Teal (#0987A0) is doing the right amount of work. It marks: corner brackets, part labels, TOC numbers, callout type "Don't Skip This," tags, pips, divider diamonds, and the cover title. It's the connective tissue of the design system. It's not overused.

One note: teal serves as both the brand accent AND the color for the "Don't Skip This" callout type AND the "Cowork" tags. This creates a slight semantic collision — teal means "identity" in some places and "warning/importance" in others. Not a dealbreaker, but be aware.

### Dark-to-white transitions

The dark chapter opener → white body page transition is intentional and effective. The chapter openers create a visual "reset" that signals new territory. The grid pattern on dark pages unifies them as a family. These transitions work.

---

## 5. ILLUSTRATION INTEGRATION

All illustrations are referenced as external files (`../outputs/illustrations/`) and are not embedded in the HTML file I reviewed, so I cannot assess visual quality, composition, or style consistency of the actual images. Here's what I can assess from the CSS and integration code:

### Integration approach

- **Chapter openers:** Illustrations are positioned absolutely, right-shifted by -100px, at 18% opacity with 50% desaturation. A left-to-right gradient mask fades them into the dark background. This is a sound compositing approach — it ensures the illustration never competes with the text.
- **Cover:** Dual illustration treatment: atmospheric background at 8% opacity with blur and desaturation, plus a bottom strip at 22% opacity with top/side gradient masks. The layering is sophisticated.

### Whether illustrations add value

Based on placement alone, the chapter opener illustrations are decorative, not informational. They add texture and professionalism to what would otherwise be plain dark pages with text. That's a valid purpose for an e-book. Removing them would make the chapter openers feel bare.

**Assessment (without seeing the actual images):** If the illustrations are thematically relevant (e.g., a dashboard for the Playbooks opener, a shield for Safety), they add moderate value. If they're generic AI-generated art, they'll read as decoration and could undermine the book's credibility. The CSS treatment (heavy desaturation + low opacity) will flatten most illustration details, which masks quality issues but also reduces their impact.

---

## 6. COVER ASSESSMENT

### Would I screenshot this cover?

Based on the code: conditionally yes. The layout is strong. The title hierarchy (The / Claude Code / Field Manual) reads well on three lines. The 62px/900-weight title with -3px letter-spacing is commanding. The teal "Claude Code" pop works. The subtitle at 40% white opacity is readable without competing.

**What holds it back:** The meta line at the bottom ("Ofir Bloch · 10 Project Playbooks · Zero Code Required") is at 30% opacity — too faint. It's valuable information (author credibility, content preview, accessibility signal) that's being hidden. Bump to 45–50%.

The edition tag ("February 2026 Edition") at 10px/0.7 opacity is nearly invisible. It's fine if this is intentional (subtle dating), but if it's meant to signal freshness, it needs to be more visible.

### Title hierarchy

Works. "The" sets up the title. "Claude Code" in teal creates the product anchor. "Field Manual" in white completes the genre signal. The three-line break at 62px reads cleanly.

### Competitive positioning

As a lead-gen asset, this cover competes well. It's in the top quartile of what I see in B2B tech e-books. The dark background + single accent color + clean typography approach echoes Stripe Press and Intercom's style guides, which is the right reference class.

**What could elevate it:** A "Version 1.0" or edition marker that's more prominent. A one-line authority statement like "From [Company/Author Title]" if the author has relevant credentials. Lead-gen assets benefit from credibility signals on the cover.

---

## 7. PRINT / PDF READINESS

### Page breaks

Every page uses `page-break-after: always`, which is correct. The `@page` rule sets 816×1056px with 0 margins, relying on the page content padding instead. This should render correctly in most Print-to-PDF engines.

### Potential break issues

- **Page 19 (Five Rules):** If rendered with any height variance, the five H3 sections + callout + code block could overflow. Test this page specifically.
- **Page 23 (Golden Rules):** Content ends mid-page with significant whitespace below. Not a break issue, but a visual issue in PDF.
- **Playbook pages (30–36):** Multiple playbooks start mid-page. None of them would break awkwardly because the page-break-after:always on the `.page` div prevents it, but the visual result is uneven page fill.

### Widows and orphans

No traditional widow/orphan issues because each `.page` div is a fixed-size container with page-break-after. Text doesn't flow between pages — it's manually laid out per page. This means: **if content overflows a page, it will be clipped rather than flowing to the next page.** This is a significant risk for the dense pages (18, 19, 23, 26).

### Page numbering

**This has significant errors.**

The page numbers shown on body pages don't account for chapter openers. Here's what I found:

- Body pages are numbered: 5, 8, 10, 12, 13, 15, 16, 18, 19, 21, 23, 26, 27 (implied), 28, 29, 30, 31 (implied), 32, 33 (implied), 34, 35 (implied), 36, 37, 39, 40, 41, 42.
- Missing sequential numbers: 6, 7, 9, 11, 14, 17, 20, 22, 24, 25, 27, 31, 33, 35, 38.
- Some gaps are chapter openers (which occupy a physical page without a visible number). But the TOC claims Part 1 runs from page 5 to page 7. There's no page 6 or page 7 in the body content.

**The page numbering system needs a full reconciliation pass.** Either: (a) add the missing pages of content, or (b) renumber all pages sequentially so each chapter opener counts as a numbered page, and body pages follow consecutively.

---

## 8. TOP 10 SPECIFIC FIXES (Priority-ranked)

### 1. Reconcile page numbering across the entire book
**What:** Page numbers skip (5 → 8 → 10 → 12...) without corresponding content pages. TOC references pages that don't exist as body pages.  
**Where:** Entire book, starting from page 5.  
**How:** Either add the missing content pages (6, 7, 9, 11, 14, etc.) or renumber everything sequentially. Each chapter opener should increment the page count. If the opener for Part 2 is physical page 7, the next body page should be 8. Update the TOC to match.  
**Why:** A lead-gen asset with wrong page numbers signals sloppy production. This is the highest-impact fix because it affects trust.

### 2. Differentiate the four overlapping callout colors
**What:** "Worth Knowing" and "Jargon Buster" share identical blue backgrounds. "Reality Check" and "Copy Exact" share identical green backgrounds.  
**Where:** CSS callout definitions (lines 257–264) and all instances throughout the book.  
**How:** Change `.callout.jargon` background to `#F0EDFF` (soft indigo) with border color `#6B5CE7`. Change `.callout.copyexact` background to `#E6FFFA` (the existing teal-bg) with border color `var(--teal)` and add `border-style: dashed` to the left edge to visually distinguish it.  
**Why:** Readers scan callouts by color. Four types sharing two colors defeats the purpose of having distinct types. This is the biggest design system flaw.

### 3. Increase H3 differentiation from body text
**What:** H3 at 17px/700 Inter doesn't create enough separation from 14px/400 Lora body text. The different font families mask the problem at first glance, but sustained reading blurs the hierarchy.  
**Where:** CSS line 228 (`h3` rule). Affects every page with H3s (pages 18–19 especially).  
**How:** Change H3 to `font: 700 18px/1.35 var(--font-heading); color: var(--teal);` — adding the teal color creates an instant visual anchor that differentiates from both H2 (black) and body (dark gray).  
**Why:** Typographic hierarchy is the foundation of scanability. When readers flip through the PDF, H3s should register immediately as sub-sections.

### 4. Add missing content to Part 1
**What:** Part 1 has only 1 body page of content. The TOC implies 3 pages. The section needs a visual comparison of Claude / Cowork / Claude Code and a clearer setup for what follows.  
**Where:** After page 5 (Part 1 body).  
**How:** Add a comparison table or diagram showing the three tools (Claude Chat → Cowork → Claude Code Desktop) with columns for: what it does, what it can't do, who it's for. Add a "What you'll learn in this guide" section with brief 1-line descriptions per Part. This brings Part 1 to 2–3 pages and anchors the reader before they dive in.  
**Why:** Part 1 is the reader's first content experience after the cover and TOC. If it feels thin, the reader questions whether the rest of the guide will deliver.

### 5. Increase callout title font size from 11px to 12px
**What:** Callout titles at 11px uppercase are strained at common PDF zoom levels (75%, 80%).  
**Where:** CSS line 254 (`.callout-title`).  
**How:** Change to `font: 700 12px/1 var(--font-heading); letter-spacing: 1px;` — slightly reduce letter-spacing to compensate for the size increase so the titles don't feel too spread.  
**Why:** Callouts are the book's signature element. Their titles need to be instantly readable at any zoom level. Going from 11px to 12px costs nothing in layout but gains significant readability.

### 6. Fix H2 bottom margin (too tight)
**What:** H2 has 14px bottom margin. When followed by a paragraph, there's barely more space below the heading than between consecutive body paragraphs (12px).  
**Where:** CSS line 226 (`h2` rule).  
**How:** Change margin from `32px 0 14px` to `32px 0 20px`.  
**Why:** Headings need clear separation from the text they introduce. The current 14px makes H2s feel glued to their first paragraph, reducing scanability.

### 7. Rebalance playbook page density
**What:** Playbook 01 gets ~2 pages with a full walkthrough. Playbooks 04, 06, 07, 08, 09, 10 get half a page each. The inconsistency is jarring.  
**Where:** Pages 29–36 (the playbook body pages).  
**How:** For the brief playbooks, add a "What happens next" paragraph (2–3 sentences) and a "Copy This Exactly" prompt callout to each one, matching the Playbook 01 structure. Each playbook should have: metadata table + starter prompt + one callout + brief "what to expect." This brings them to roughly ¾ page each.  
**Why:** The playbooks are the book's marquee content (featured on the cover as "10 Project Playbooks"). If 6 of them look skeletal compared to the first, the reader feels shortchanged.

### 8. Boost cover metadata opacity
**What:** The author name, playbook count, and "Zero Code Required" text on the cover are at 30% white opacity — nearly invisible.  
**Where:** Cover HTML (line 94, `.cover-meta`).  
**How:** Change `color: rgba(255,255,255,0.30)` to `rgba(255,255,255,0.50)`. Change the `.author` class from `0.50` to `0.65`.  
**Why:** These are the three strongest selling signals on the cover: the author (credibility), "10 Project Playbooks" (concrete value), "Zero Code Required" (accessibility). Hiding them undermines the cover's job as a lead-gen asset.

### 9. Add corner bracket fragment to body page footers
**What:** The corner bracket motif disappears entirely on white body pages, creating a visual disconnect between chapter openers and content pages.  
**Where:** Page footer area (`.page-num` or a new element adjacent to it).  
**How:** Add two small bracket marks (8px × 8px, 0.15 opacity teal) flanking the page number — top-left corner bracket to the left of the number, bottom-right corner bracket to the right. Subtle enough to not distract, present enough to maintain identity.  
**Why:** Design systems need continuous threads. The bracket motif is the book's visual identity; it should be present (even faintly) on every page.

### 10. Eliminate the full-page legal disclaimer
**What:** The legal disclaimer occupies an entire dark page (page 3), adding unnecessary weight to the front matter.  
**Where:** Page 3 (lines 372–382).  
**How:** Move the disclaimer text to the bottom third of the "What's Inside" page (page 2), set in 11px at 25% opacity. This frees up a full page and gets the reader to the TOC faster.  
**Why:** Every page between the cover and the content is friction for a lead-gen asset. Legal needs to exist, but it doesn't need a throne. Stripe Press and A Book Apart both tuck legal into colophon-style micro-sections.

---

## Summary verdict

This is a solid 7/10 e-book that could be 9/10 with these fixes. The writing is excellent — genuine, practical, zero AI-filler smell. The design system is 80% there, with the callout color overlap and page numbering being the two structural issues that need addressing before production.

The strongest elements: the voice, the "Copy This Exactly" callouts, the cover composition, the chapter opener dark-page treatment, and the overall typography choices.

The weakest elements: page numbering inconsistency, thin content in several Parts, and the playbook density imbalance.

Fix the top 5 items on the list above, and this ships as a genuinely premium lead-gen asset.
