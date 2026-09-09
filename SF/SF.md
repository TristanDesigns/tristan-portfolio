# Smoker Friendly — Style Reference

> Flying Papers structure, Smoker Friendly colour

**Theme:** light

Smoker Friendly runs the Flying Papers skeleton — ultra-heavy condensed display type, flat surfaces, hairline-free 2px outlines, and fully-pill controls — but repainted in the brand's own retail palette rather than dusk violet. Electric cobalt is the stage: it floods hero and feature bands full-bleed, with warm paper cards floating on top. Anton sets every headline in tight uppercase, Inter carries body copy, and JetBrains Mono handles the small tracked labels that give the system its ticketed, signage-like texture. There is no elevation anywhere; separation comes from colour blocks, 2px outlines, and the 6px card radius. The retro aqua and warm coral accents keep the palette playful without softening the structural rigour.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Electric Cobalt | `#3B5BFF` | `--sf-cobalt` | Primary brand ground — full-bleed hero and feature bands, the surface the system is staged on |
| Cobalt Deep | `#1E39D6` | `--sf-cobalt-deep` | Pressed states, deeper band variant, gradient-free shading of the brand ground |
| Retro Aqua | `#6FD6E8` | `--sf-aqua` | Highlight fill — reserved for highlights, accordion markers, and calm tile fills |
| Warm Coral | `#FF5847` | `--sf-coral` | Warm accent band and card fill; the counterweight to cobalt |
| Bright Sun | `#FFC53D` | `--sf-yellow` | Third accent fill for tiles and tags in the rotation |
| Deep Navy Ink | `#101538` | `--sf-ink` | All primary text, 2px outlines, icon strokes. Never pure black — the navy keeps type on-brand |
| Warm Paper | `#FFF8F0` | `--sf-paper` | Card surfaces and light text on cobalt/ink grounds |
| White | `#FFFFFF` | `--sf-white` | Brightest card fill, used when paper reads too warm against a photo |
| Slate | `#3E4A70` | `--sf-slate` | Secondary body copy on light cards |
| Pale Periwinkle | `#C8D3F5` | `--sf-sky` | Footer body copy on ink, calm tile fills |
| Periwinkle Dim | `#8B99C9` | `--sf-sky-dim` | Footer meta, timestamps, lowest-emphasis text on dark grounds |

### Client Logo Palette — content, not chrome

| Name | Value | Token | Role |
|------|-------|-------|------|
| Client Navy | `#003DA6` | `--client-navy` | Appears inside reproduced client marks only |
| Client Red | `#EA0029` | `--client-red` | Appears inside reproduced client marks only |
| Client Gold | `#F5A800` | `--client-gold` | Appears inside reproduced client marks only |
| Client Grey | `#C1C5C8` | `--client-grey` | Appears inside reproduced client marks only |

## Tokens — Typography

### Anton — Display only. Every headline is uppercase Anton at weight 400 (the face carries its own weight — never bold it) with `.02em` tracking and a tight `0.88–1.0` line height so multi-line headlines stack into a solid block. This compression is the system's loudest gesture. · `--font-display`
- **Substitute:** Oswald, Archivo Black
- **Weights:** 400
- **Sizes:** 26, 32, 42, 56, 72
- **Line height:** 0.88–1.05
- **Letter spacing:** +0.02em
- **Role:** Display only — hero headline, section headings, fold titles, stat values.

### Inter — All body and UI text. Weight 400 for prose, 700 for buttons and emphasis. Kept at a normal reading measure to give the Anton headlines something quiet to sit against. · `--font-body`
- **Substitute:** Helvetica Now, Söhne
- **Weights:** 400, 700
- **Sizes:** 13, 14.5, 15, 16, 17, 18, 19
- **Line height:** 1.4–1.6
- **Role:** Body copy, buttons, navigation, card text, footer.

### JetBrains Mono — Micro-labels only: eyebrows, tags, section indices, captions. Uppercase at 12px with `+0.05em` tracking. This is what makes the system read as signage and ticketing rather than as a generic bold-sans layout. · `--font-mono`
- **Substitute:** IBM Plex Mono, Space Mono
- **Weights:** 400, 600
- **Sizes:** 11, 12, 13
- **Letter spacing:** +0.05em, uppercase
- **Role:** Eyebrow tags, category labels, fold numbers, image captions.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| micro | 12px | 1.2 | +0.05em | `--text-micro` |
| label | 13px | 1.3 | +0.05em | `--text-label` |
| body-sm | 15px | 1.5 | — | `--text-sm` |
| body | 17px | 1.55 | — | `--text-base` |
| lead | 19px | 1.5 | — | `--text-lead` |
| h3 | 26px | 1.05 | +0.02em | `--text-h3` |
| h2 | clamp(28px, 4vw, 42px) | 0.95 | +0.02em | `--text-h2` |
| hero | clamp(40px, 6vw, 72px) | 0.88 | +0.02em | `--text-hero` |

## Tokens — Spacing & Shapes

**Base unit:** 4px

**Density:** comfortable

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--space-1` |
| 8 | 8px | `--space-2` |
| 12 | 12px | `--space-3` |
| 16 | 16px | `--space-4` |
| 24 | 24px | `--space-5` |
| 32 | 32px | `--space-6` |
| 48 | 48px | `--space-7` |
| 72 | 72px | `--space-8` |
| 96 | 96px | `--space-9` |

### Border Radius

| Element | Value |
|---------|-------|
| cards | 6px |
| media | 6px |
| icons | 6px |
| buttons | 100px |
| tags | 100px |

### Borders

| Name | Value | Token |
|------|-------|-------|
| standard | 2px solid `#101538` | `--border-width` |
| inset | 2px solid `#101538` | `--border-width-sm` |

### Shadows

None. The system has zero elevation — see **Elevation** below.

### Layout

- **Page max-width:** 1180px
- **Section gap:** 72–96px
- **Card padding:** 24–32px
- **Element gap:** 12–16px

## Components

### Pill Button — Primary
**Role:** Main action

Warm paper fill (`#FFF8F0`), ink text (`#101538`), no border, `100px` radius, `12px 17px` padding, Inter 700 at 16px with `+0.05em` tracking. Sits on the cobalt ground where the paper fill reads as an inversion of the band.

### Pill Button — Secondary
**Role:** Companion action

Transparent fill, `2px` solid outline, `100px` radius, same padding and type as primary. On cobalt the outline and label are warm paper; on paper grounds both switch to ink.

### Eyebrow Tag
**Role:** Section or category label above a headline

Transparent fill, `1px` solid `currentColor`, `100px` radius, JetBrains Mono 12px uppercase with `+0.05em` tracking. Never filled — the outline keeps it subordinate to the Anton headline beneath it.

### Card
**Role:** Content container, work tile, role card

Warm paper or white fill, `6px` radius, no border and no shadow — the fill alone separates it from the coloured band. When a card sits on a paper ground rather than a colour band, add the `2px` ink outline to restore the edge.

### Colour Band Section
**Role:** Full-bleed section ground

One flat colour per band, edge to edge, no gradient and no divider rule between bands — the colour change *is* the division. Rotation: cobalt → paper → coral → paper → aqua. Never place two chromatic bands adjacent without a paper band between them.

### Nav Bar
**Role:** The one persistent chrome on the page

Shared across all three case-study pages — same structure, same behaviour, same class names (`.pnav`, `.pnav-links`), only the skin changes. The `tristan` wordmark sits left, the page's section links right. **It is only present on the way up:** at rest when the page is at the top, it slides out of view on any downward scroll past the first 80px and returns on any upward scroll, with a 6px dead zone so a jittery trackpad never flickers it. Under 760px the links drop away and the wordmark stands alone. Section targets carry `scroll-margin-top` so a jump never lands under it.

Here it is a deep navy ink band with a `2px` ink rule beneath, the wordmark in warm paper, and links in JetBrains Mono uppercase each preceded by a star bullet. Sticky rather than fixed, so it holds its place in the flow beneath the hero band.

### Glance Row
**Role:** The brief, in two cards, directly under the hero

Two cards side by side on a banded paper section — the only place on the page where the job is described rather than shown. The first is the standard Card (white, `2px` ink outline, no shadow, 26/28px padding) carrying an eyebrow tag and a single paragraph at body-large. The second inverts to Signal Coral with its line set in Anton uppercase at pull-quote size — the outcome, and the loudest thing on the page after the hero. On coral the type is **ink, not white**: the page already pairs coral with ink on every button, and white on this coral is only 3.1:1. Its tag flips to a white fill with an ink label. Two across, never three; if a fact does not fit in one of the two, it belongs in a work section or nowhere.

### Open Section Head
**Role:** Heading for a work section — every section on the page uses this

The fold head with the toggle removed: a two-column grid of `[mono index] [title block]`, 22/26px gaps. The title block is an eyebrow tag, an Anton uppercase title, then an optional one-line gist in the section's muted tone. The work follows after 44px at full width. A gist earns its place only when it says something the title and the work do not.

### Accordion Toggle
**Role:** Expand/collapse control — now used only by the "+ More" panel in Selected Work

`52px` square, white fill, `2px` ink outline, `6px` radius, no shadow and no transform on press. Contains a star mark at `2.5px` stroke plus a `3px` plus/minus stroke; the plus collapses to a minus on open and the star fills with Bright Sun. Nothing else on the page hides behind a toggle.

### Fold Index
**Role:** Numeric marker beside a section heading

White fill, `2px` ink outline, `6px` radius, JetBrains Mono 13px. No rotation, no shadow — flat and square to the grid.

### Footer
**Role:** Page-end contact block

Deep navy ink ground, warm paper headline, pale periwinkle body copy, periwinkle-dim meta line above a `2px` paper rule.

## Do's and Don'ts

### Do
- Set every headline in Anton uppercase at weight 400 with `+0.02em` tracking and a line height at or below 1.0 so multi-line headlines stack solid.
- Use `#101538` rather than black for all text, outlines and icon strokes — the navy is what keeps the system on-brand at body size.
- Keep the two radii absolute: `6px` on every rectangular surface, `100px` on every button and tag. Nothing in between.
- Let flat colour bands do the dividing. Change ground colour at the section break instead of drawing a rule.
- Reserve JetBrains Mono for uppercase micro-labels only — eyebrows, indices, captions, tags.
- Give buttons and tags horizontal padding of at least half their height so the pill curve never crowds the label.
- Use `2px` outlines consistently; this system has one border weight.
- Put the work first. Story, roles and stats belong in the two-card glance row under the hero, never as a section the reader has to get past.

### Don't
- Never apply a drop shadow, inner shadow, or offset "sticker" shadow to any element — the system is flat and separation comes from colour and outline.
- Never bold Anton or set it at a line height above 1.05; both destroy the stacked-block effect.
- Never use Anton below 26px — it is a display face only, and Inter handles everything smaller.
- Never place a chromatic band directly against another chromatic band; a paper band must separate them.
- Never introduce a hue outside the palette. The client logo colours are content that appears inside reproduced marks, not chrome to design with.
- Never use a gradient. Every surface is one flat tone.
- Never mix radius values — a `12px` or `24px` corner anywhere breaks the two-shape rule.
- Never run the page as a stack of accordions. One toggle survives — the "+ More" banners panel — and everything else is open.
- Never set white type on Signal Coral. Coral takes ink, the same as the buttons do.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Brand Band | `#3B5BFF` | Full-bleed hero and feature grounds |
| 1 | Paper | `#FFF8F0` | Alternating section ground and card fill |
| 2 | White | `#FFFFFF` | Brightest card fill, used over photography |
| 3 | Ink | `#101538` | Footer and inverse panels |

## Elevation

Zero. No drop shadows, no offset shadows, no blur, no inner glow. Depth is communicated by flat colour change, the `2px` ink outline, and the `6px` radius alone. If an element needs to feel lifted, change its fill or give it an outline — never add a shadow.

## Imagery

Photography is retail-real: in-store displays, event signage, product shots, and printed collateral, shown full-bleed inside `6px`-radius frames with no border and no shadow. Images are never desaturated, tinted, duotoned, or overlaid — the work's own colour is the point, and it sits against the flat brand bands unmodified. Icons are drawn, not geometric: hand-weighted arrows and star marks at `2.5–3px` stroke in ink, matching the outline weight of the surrounding components. No stock photography, no lifestyle imagery, no abstract decoration.

## Layout

Centred 1180px column with full-bleed colour bands breaking out to the viewport edge. The rhythm is band → paper → band, with 72–96px of vertical space between sections and no divider rules. The page is built work-first and reads in this order:

1. **Hero** — a two-column split on the cobalt band: eyebrow tag, Anton headline with the pressable number highlights, lede and pill buttons on the left, the work collage on the right.
2. **Glance row** — two cards on a banded paper section, *The job* and *The outcome*. This replaces the stat row and the three-paragraph story section; everything descriptive lives here.
3. **The work, open** — three numbered sections, each a mono index, eyebrow tag, Anton title and optional one-line gist, then the work at full width. **01 is Visual identity** — the brand system the rest was built on — followed by **02 What I did** and **03 Selected work**. No toggles.
4. **Footer** — a full-bleed ink band with centred type.

The one thing still behind a click is the "+ More" card at the end of Selected Work, which folds out into the web banners, register ads and store signage. That is the exception, not the pattern: never run the page as a stack of accordions, and never put a stat row or a story section between the reader and the work.

## Agent Prompt Guide

**Quick Color Reference**
- Brand ground: `#3B5BFF`
- Page/card surface: `#FFF8F0`
- Text and outlines: `#101538`
- Secondary text: `#3E4A70`
- Accents: `#6FD6E8` aqua, `#FF5847` coral, `#FFC53D` sun
- Primary action: `#FFF8F0` fill with `#101538` label

**Example Component Prompts**

1. **Hero band** — Full-bleed `#3B5BFF`. Eyebrow tag in JetBrains Mono 12px uppercase, `+0.05em`, transparent with a 1px `currentColor` outline at 100px radius. Headline in Anton 400 uppercase, `clamp(40px,6vw,72px)`, line-height 0.88, `+0.02em`, colour `#FFF8F0`. Sub-copy in Inter 400 19px at 90% opacity. Two pill buttons: primary `#FFF8F0` fill with `#101538` text, secondary transparent with a 2px `#FFF8F0` outline; both 100px radius, 12px/17px padding, Inter 700 16px `+0.05em`.

2. **Work card** — `#FFF8F0` fill, 6px radius, no border, no shadow. Image fills the top at 6px radius. Below it, Anton 26px uppercase title, Inter 15px `#3E4A70` body, and a JetBrains Mono 12px uppercase tag with a 1px outline at 100px radius.

3. **Stat row** — Four tiles, fills rotating aqua → coral → sun → white, 6px radius, 2px `#101538` outline, 24px padding. Value in Anton 400 at 42px `#101538`; label beneath in JetBrains Mono 12px uppercase `+0.05em`.

4. **Accordion head** — Grid of `[mono index] [title block] [toggle]`. Index: white fill, 2px ink outline, 6px radius, JetBrains Mono 13px. Title: eyebrow tag, then Anton 400 `clamp(28px,4vw,42px)` uppercase at line-height 0.95. Toggle: 52px square, white fill, 2px ink outline, 6px radius, star mark plus a plus/minus stroke, no shadow and no press transform.

5. **Footer** — Full-bleed `#101538`. Anton uppercase headline in `#FFF8F0`, body in `#C8D3F5`, meta line in `#8B99C9` above a 2px `#FFF8F0` rule. Pill buttons follow the primary/secondary pattern with paper and ink swapped.

## Relationship to Flying Papers

This is Flying Papers' **structure** with Smoker Friendly's **colour**. Everything shape- and type-related is inherited: Anton over Inter over JetBrains Mono, the `6px`/`100px` two-radius rule, the flat 2px outlines, zero elevation, and colour blocks as dividers. Everything chromatic is replaced: the dusk violet stage becomes electric cobalt, bone white becomes warm paper, hi-vis yellow becomes bright sun, and the muted sage/blush/amber tints become the retail aqua, coral and sun. If a decision is about *shape, weight or spacing*, follow Flying Papers. If it is about *hue*, follow the palette above.
