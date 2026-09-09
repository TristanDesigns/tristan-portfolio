# US Display Group — Style Reference

> clinical blueprint on frosted paper

**Theme:** light

US Display Group is a monochromatic design-system workshop: pure white canvas, soft warm-gray surfaces, and large-radius cards floating on hairline borders. The interface is almost entirely achromatic — black text, white surfaces, gray secondary tones — with a single destructive red reserved for error states and nothing else. Typography leans on Geist's geometric neutrality with tight letter-spacing on display sizes, creating a quiet, code-adjacent feel that reads as developer infrastructure rather than consumer product.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Canvas | `#f5f5f5` | `--color-canvas` | Page background, muted surface fills, secondary buttons |
| Paper | `#ffffff` | `--color-paper` | Card surfaces, popover backgrounds, primary button fills |
| Surface Alt | `#fafafa` | `--color-surface-alt` | Sidebar background, subtle card variant, input resting state |
| Ink | `#0a0a0a` | `--color-ink` | Primary text, headings, button labels, icon strokes |
| Ink Soft | `#171717` | `--color-ink-soft` | Filled button backgrounds, secondary text on light surfaces |
| Mid Gray | `#737373` | `--color-mid-gray` | Muted body text, placeholder text, helper labels, icon fills at rest |
| Hairline | `#e5e5e5` | `--color-hairline` | Borders, input outlines, card edges, badge outlines |
| Ember | `#e7000b` | `--color-ember` | Red decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color |

## Tokens — Typography

### Geist — All interface text — body at 14px/400, headings ranging 24–48px/600, buttons at 13–14px/500. Geist's geometric letterforms and uniform stroke width create a developer-tool neutrality; weight 600 at 48px with -0.05em tracking produces tight, confident display headlines that feel engineered rather than editorial. · `--font-geist`
- **Substitute:** Inter
- **Weights:** 400, 500, 600
- **Sizes:** 12, 13, 14, 16, 18, 24, 30, 36, 48
- **Line height:** 1.10, 1.11, 1.20, 1.33, 1.43, 1.50, 1.56, 1.63, 2.00
- **Letter spacing:** -0.0500em at display (48px), -0.0250em at subheading (24–30px), 0.0500em at caption (12px uppercase). Tracking tightens aggressively at large sizes and loosens slightly at small uppercase labels.
- **OpenType features:** `"ss01" on, "cv11" on`
- **Role:** All interface text — body at 14px/400, headings ranging 24–48px/600, buttons at 13–14px/500.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.33 | 0.6px | `--text-caption` |
| body | 14px | 1.43 | — | `--text-body` |
| body-lg | 16px | 1.5 | — | `--text-body-lg` |
| subheading | 18px | 1.56 | — | `--text-subheading` |
| heading-sm | 24px | 1.33 | -0.6px | `--text-heading-sm` |
| heading | 30px | 1.2 | -0.75px | `--text-heading` |
| heading-lg | 36px | 1.11 | -0.9px | `--text-heading-lg` |
| display | 48px | 1.1 | -2.4px | `--text-display` |

## Tokens — Spacing & Shapes

**Base unit:** 4px

**Density:** compact

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 20 | 20px | `--spacing-20` |
| 24 | 24px | `--spacing-24` |
| 48 | 48px | `--spacing-48` |

### Border Radius

| Element | Value |
|---------|-------|
| cards | 24px |
| small | 6px |
| badges | 18px |
| inputs | 18px |
| nested | 10px |
| buttons | 18px |

### Shadows

| Name | Value | Token |
|------|-------|-------|
| subtle | `oklab(0.145 -0.00000143796 0.00000340492 / 0.05) 0px 0px 0px 1px, rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1) 0px 1px 2px -1px` | `--shadow-subtle` |
| subtle-2 | `lab(2.75381 0 0) 0px 0px 0px 0px` | `--shadow-subtle-2` |

### Layout

- **Page max-width:** 1280px
- **Section gap:** 48-80px
- **Card padding:** 20px
- **Element gap:** 8px

## Components

### Primary Filled Button
**Role:** High-emphasis action (Submit, Save, Create)

Background #0a0a0a, text #fafafa, border none, radius 18px, padding 0px 12px (compact) or 8px 16px (comfortable), font 14px Geist weight 500. Height ≈ 36–40px. The dark-on-light inversion is the only chromatic interaction in the system; the fully rounded radius (18px on a ~36px height) produces perfect pill geometry.

### Secondary Ghost Button
**Role:** Low-emphasis action (Cancel, Back)

Background #f5f5f5, text #0a0a0a, no border, radius 18px, padding 0px 12px or 8px 16px, font 14px weight 500. Soft gray fill reads as a tonal sibling to the primary rather than a muted alternative — both buttons share shape and type, differing only in lightness.

### Outline Button
**Role:** Tertiary action with visible boundary

Background transparent, text #0a0a0a, border 1px solid #e5e5e5, radius 18px, padding 0px 12px or 8px 10px. The hairline border defines the shape without weight — preferred when the button sits inside a card or alongside filled controls.

### Card
**Role:** Content container for blocks, previews, dashboard panels

Background #ffffff, radius 24px, border 1px solid #e5e5e5, shadow oklab(0.145/.05) 0 0 0 1px + rgba(0,0,0,0.1) 0 1px 3px + rgba(0,0,0,0.1) 0 1px 2px -1px, padding 20px. The 1px hairline shadow stacks with a faint elevation layer — cards sit visually raised but remain flat and understated.

### Nested Card Header/Footer
**Role:** Header or footer strip inside a card

Asymmetric radius — top corners 24px on header, bottom corners 24px on footer. Padding 20px horizontal, transparent fill. Provides a subtle tonal band within card boundaries without introducing a new color.

### Input Field
**Role:** Text entry, search, form controls

Background #f5f5f5 (resting) or transparent (inline), text #0a0a0a, border none at rest with 1px #e5e5e5 on focus, radius 18px, padding 8px 10px, font 14px weight 400. The soft gray fill differentiates the input from the card surface beneath it; focus replaces the fill with a 1px ring.

### Badge — Solid
**Role:** Tag, status pill, counter

Background #171717, text #fafafa, radius 18px, padding 2px 8px, font 12px weight 500. Pill-shaped at 18px radius — the minimum height creates a capsule tag.

### Badge — Soft
**Role:** Neutral label, category tag

Background #f5f5f5, text #171717, radius 18px, padding 2px 8px, font 12px weight 500. Same capsule geometry as solid badge, tonal variant.

### Badge — Outline
**Role:** Subtle tag with no fill

Transparent background, text #0a0a0a, radius 18px, padding 2px 8px. The lightest-weight tag — used when the label is informational rather than categorical.

### Sidebar Surface
**Role:** Left navigation panel

Background #fafafa, full-height, contained width. Sits one tonal step off the canvas (#f5f5f5) so the navigation reads as a distinct layer without introducing a divider line.

### Breadcrumb Trail
**Role:** Hierarchical path indicator

Inline text with chevron separators, font 14px weight 400, color #737373 for separators and #0a0a0a for the current segment. No background, no borders — purely typographic hierarchy.

### Stat Block
**Role:** Large numeric metric display

Label in 12–14px uppercase #737373, value in 30–48px weight 600 #0a0a0a with tight tracking. Progress bar or comparison text in 14px #737373. The block relies on typographic scale alone — no card chrome — to establish the metric.

### Search Trigger
**Role:** Command palette / search input

Background #f5f5f5, text #737373, radius 18px, padding 8px 10px, with a keyboard shortcut indicator (e.g., ⌘K) right-aligned. Functions as both a button and an input affordance.

### Destructive Action
**Role:** Delete, remove, revoke — error-adjacent interactions

Text or icon in #e7000b against the monochromatic palette. The red is the only chromatic hue in the system and appears exclusively in destructive or error contexts — it never decorates.

### Nav Bar
**Role:** The one persistent chrome on the page

Shared across all three case-study pages — same structure, same behaviour, same class names (`.pnav`, `.pnav-links`), only the skin changes. The `tristan` wordmark sits left, the page's section links right. **It is only present on the way up:** at rest when the page is at the top, it slides out of view on any downward scroll past the first 80px and returns on any upward scroll, with a 6px dead zone so a jittery trackpad never flickers it. Under 760px the links drop away and the wordmark stands alone. Section targets carry `scroll-margin-top` so a jump never lands under it.

Here it is a `#ffffff` bar over the canvas with a 1px `#e5e5e5` rule beneath and no shadow — the same hairline separation every card uses. Wordmark in `#0a0a0a`; links in Geist 14px/500 `#737373`, going `#0a0a0a` on hover. Sticky rather than fixed, so it holds its place in the flow above the hero.

### Fold Demo
**Role:** The hero's right-hand column — a carton that folds from flat dieline to finished box

The one piece of motion in the system, and the page's thesis made touchable: the hero headline says "turning flat art into physical displays", so the hero shows exactly that happening. It lives in a standard Card (white, 1px hairline, 24px radius, whisper shadow) split into a scene and a control strip.

**Scene.** A #fafafa ground carrying a 26px #e5e5e5 grid — a cutting mat, and the only patterned surface in the system. Inside it every panel of the carton is a plain div hinged off its neighbour in the order a real carton folds: front → sides → back → glue flap, with tuck, dust and bottom flaps hanging off their own panels. One progress value drives every hinge, each one lagging the last by its depth in that chain, so the box assembles outward from the front rather than snapping shut at once. CSS 3D transforms only — no WebGL, no 3D library, nothing fetched from a CDN.

**Face shading.** Faces are tinted by which way they end up pointing, on a neutral ramp that never leaves the greyscale: front `#ffffff`, sides `#f1f1f1`, back `#f7f7f7`, bottom flaps `#efefef`, top flaps and glue `#e9e9e9`, all edged in a `#d4d4d4` hairline. Flat, that shading reads as a colour-coded dieline proof; folded, it reads as light falling on a solid. This is the one place a shade outside the four surface tokens is allowed, because it is describing an object rather than a UI surface.

**Labels.** Panel names (FRONT, BACK, L, R, TUCK, BOTTOM) in Geist 9px/500 uppercase `#737373`, fading out over the first fifth of the fold — they belong to the drawing, not to the finished box.

**Control strip.** A hairline-topped white bar: `Flat`, a range input, `Folded`, and a tabular percentage. The track is a 2px `#e5e5e5` rule; the thumb is a 14px `#0a0a0a` dot. It folds itself once, 2.4s, the first time it scrolls into view, then hands control to the reader. Under `prefers-reduced-motion` it starts folded and never animates.

## Do's and Don'ts

### Do
- Use #0a0a0a on #ffffff for filled buttons — the dark inversion is the only primary action treatment.
- Maintain 18px radius on all buttons, inputs, and badges for perfect pill geometry; use 24px radius only on cards.
- Set display headlines at 48px/600 with -0.0500em tracking — Geist's geometric weight at this size with aggressive tightening produces the engineered headline voice.
- Reserve #e7000b exclusively for destructive states; never use it for decoration, branding, or non-error emphasis.
- Stack card shadows as 1px hairline + 1px + 2px offset — the combined effect is a barely-perceptible elevation that reads as 'card' without drama.
- Use #f5f5f5 for secondary surfaces and inputs; use #fafafa for sidebar and subtle card variants — the three-tone surface stack (canvas → soft → paper) creates layering without borders.
- Put the work first. Story, roles, process and stats belong in the single brief block under the hero — glance tiles above, nested accordions below — never as page sections between the reader and the work.

### Don't
- Do not introduce chromatic brand colors beyond #e7000b — the monochromatic palette is the system.
- Do not use border-radius values other than 18px (interactive) or 24px (containers); avoid square corners on any element.
- Do not skip the 1px hairline border on cards — the shadow alone does not define the card edge in this system.
- Do not set body text below 14px or above #737373 lightness — the type scale is deliberately compact.
- Do not put a work section behind an accordion, and do not add a stats band. The only folds on the page are the three small ones inside the brief.
- Do not apply gradients, colored shadows, or accent fills — every surface is a solid tone.
- Do not use letter-spacing wider than 0.05em or tighter than -0.05em; tracking outside this range breaks the typographic system.
- Do not mix filled and outline buttons of the same size in a single row without visual rhythm — alternate ghost or secondary variants.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#f5f5f5` | Page background, broadest layer |
| 1 | Sidebar | `#fafafa` | Navigation surface, one step lighter than canvas |
| 2 | Card | `#ffffff` | Primary content container, brightest surface |
| 3 | Input Fill | `#f5f5f5` | Resting input field, matches canvas tone for subtle differentiation |

## Elevation

- **Card:** `0 0 0 1px rgba(23,23,23,0.05), 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)`
- **Button (filled):** `none — relies on tonal contrast, not shadow`
- **Input (focus):** `1px solid #e5e5e5 ring, no offset shadow`

## Imagery

Minimal imagery — the system is almost entirely UI. No hero photography, no illustrations, no decorative graphics. The single exception is the hero's **Fold Demo**: a carton built from live DOM panels rather than a picture of one, which earns its place because it is the subject of the page rather than decoration around it. Product showcases are rendered as component mockups (cards, inputs, buttons) in a grid, serving as both documentation and visual content. Icons are thin-stroke geometric marks (likely Lucide-derived) at 1.5–2px stroke weight in #0a0a0a or #737373, used sparingly as functional cues. The visual language IS the UI components themselves — the page functions as a living style guide where every visible element is a design token made visible.

## Layout

The page is built work-first and reads in this order:

1. **Hero** — a two-column split: headline, lede and buttons on the left, the **Fold Demo** card filling the right, collapsing to one column under 860px.
2. **The brief** — a three-tile glance row (*The job*, *What I touched*, *The pipeline*) over three nested sub-accordions carrying the long version (*The story*, *Roles*, *Pipeline*). Everything descriptive is consolidated in this one block, summary above and detail one click below — it is not a page section the reader has to get through, and it is not numbered.
3. **The work, open** — numbered sections with no toggle: **01 Case study**, **02 More work**. The head is `[index] [tag, title, gist]` and the work follows at full width.
4. **Footer** — the dark inversion.

There is no stat band, and no work sits behind an accordion. The only folds on the page are the three small ones inside the brief. Below the hero: a centered max-width 1280px column on the #f5f5f5 canvas, with 48–80px between major sections and a compact 8px element gap inside components. Cards sit in even grids at 20px padding, each defined by its 1px hairline and whisper-quiet shadow rather than by spacing alone. Navigation is a #fafafa sidebar sitting one tonal step off the canvas with no divider rule. Content hierarchy is carried entirely by type scale and tonal surface stacking — there are no colored section bands, no full-bleed breakouts, and no dividers between blocks.

## Agent Prompt Guide

**Quick Color Reference**
- Canvas/background: #f5f5f5
- Card/surface: #ffffff
- Primary text: #0a0a0a
- Muted text: #737373
- Border: #e5e5e5
- primary action: #171717 (filled action)
- Destructive: #e7000b

**Example Component Prompts**

1. Create a dashboard stat card: white (#ffffff) background, 24px radius, 1px solid #e5e5e5 border, shadow 0 0 0 1px rgba(23,23,23,0.05) + 0 1px 3px rgba(0,0,0,0.1) + 0 1px 2px -1px rgba(0,0,0,0.1), 20px padding. Label in 12px uppercase #737373, value in 36px Geist weight 600 #0a0a0a with -0.025em tracking.

2. Create a filled dark button: background #0a0a0a, text #fafafa, no border, 18px radius, padding 0px 12px, font 14px Geist weight 500. Height 36px. No shadow — tonal contrast only.

3. Create a ghost secondary button: background #f5f5f5, text #0a0a0a, no border, 18px radius, padding 0px 12px, font 14px weight 500. Same dimensions as the filled button for visual parity.

4. Create an input field: background #f5f5f5, text #0a0a0a, placeholder #737373, no border at rest, 18px radius, padding 8px 10px, font 14px weight 400. On focus: 1px solid #e5e5e5 ring with no offset.

5. Create a badge tag: background #171717, text #fafafa, 18px radius (full pill), padding 2px 8px, font 12px Geist weight 500.

## Design Philosophy

Built on three principles visible in every token: (1) achromatic by default — color is absence, not expression; (2) radius defines hierarchy — 18px for interactive elements, 24px for containers, never anything in between; (3) elevation is whisper-quiet — the card shadow is barely perceptible, relying on 1px hairlines and tonal contrast rather than dramatic drop shadows. The system is designed to be copied, modified, and owned — every value is explicit, every token is simple, and nothing is locked behind abstraction.

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors */
  --color-canvas: #f5f5f5;
  --color-paper: #ffffff;
  --color-surface-alt: #fafafa;
  --color-ink: #0a0a0a;
  --color-ink-soft: #171717;
  --color-mid-gray: #737373;
  --color-hairline: #e5e5e5;
  --color-ember: #e7000b;

  /* Typography — Font Families */
  --font-geist: 'Geist', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  /* Typography — Scale */
  --text-caption: 12px;
  --leading-caption: 1.33;
  --tracking-caption: 0.6px;
  --text-body: 14px;
  --leading-body: 1.43;
  --text-body-lg: 16px;
  --leading-body-lg: 1.5;
  --text-subheading: 18px;
  --leading-subheading: 1.56;
  --text-heading-sm: 24px;
  --leading-heading-sm: 1.33;
  --tracking-heading-sm: -0.6px;
  --text-heading: 30px;
  --leading-heading: 1.2;
  --tracking-heading: -0.75px;
  --text-heading-lg: 36px;
  --leading-heading-lg: 1.11;
  --tracking-heading-lg: -0.9px;
  --text-display: 48px;
  --leading-display: 1.1;
  --tracking-display: -2.4px;

  /* Typography — Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;

  /* Spacing */
  --spacing-unit: 4px;
  --spacing-4: 4px;
  --spacing-8: 8px;
  --spacing-12: 12px;
  --spacing-16: 16px;
  --spacing-20: 20px;
  --spacing-24: 24px;
  --spacing-48: 48px;

  /* Layout */
  --page-max-width: 1280px;
  --section-gap: 48-80px;
  --card-padding: 20px;
  --element-gap: 8px;

  /* Border Radius */
  --radius-md: 6px;
  --radius-lg: 10px;
  --radius-xl: 14px;
  --radius-2xl: 18px;
  --radius-3xl: 24px;

  /* Named Radii */
  --radius-cards: 24px;
  --radius-small: 6px;
  --radius-badges: 18px;
  --radius-inputs: 18px;
  --radius-nested: 10px;
  --radius-buttons: 18px;

  /* Shadows */
  --shadow-subtle: oklab(0.145 -0.00000143796 0.00000340492 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px;
  --shadow-subtle-2: lab(2.75381 0 0) 0px 0px 0px 0px;

  /* Surfaces */
  --surface-canvas: #f5f5f5;
  --surface-sidebar: #fafafa;
  --surface-card: #ffffff;
  --surface-input-fill: #f5f5f5;
}
```

### Tailwind v4

```css
@theme {
  /* Colors */
  --color-canvas: #f5f5f5;
  --color-paper: #ffffff;
  --color-surface-alt: #fafafa;
  --color-ink: #0a0a0a;
  --color-ink-soft: #171717;
  --color-mid-gray: #737373;
  --color-hairline: #e5e5e5;
  --color-ember: #e7000b;

  /* Typography */
  --font-geist: 'Geist', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  /* Typography — Scale */
  --text-caption: 12px;
  --leading-caption: 1.33;
  --tracking-caption: 0.6px;
  --text-body: 14px;
  --leading-body: 1.43;
  --text-body-lg: 16px;
  --leading-body-lg: 1.5;
  --text-subheading: 18px;
  --leading-subheading: 1.56;
  --text-heading-sm: 24px;
  --leading-heading-sm: 1.33;
  --tracking-heading-sm: -0.6px;
  --text-heading: 30px;
  --leading-heading: 1.2;
  --tracking-heading: -0.75px;
  --text-heading-lg: 36px;
  --leading-heading-lg: 1.11;
  --tracking-heading-lg: -0.9px;
  --text-display: 48px;
  --leading-display: 1.1;
  --tracking-display: -2.4px;

  /* Spacing */
  --spacing-4: 4px;
  --spacing-8: 8px;
  --spacing-12: 12px;
  --spacing-16: 16px;
  --spacing-20: 20px;
  --spacing-24: 24px;
  --spacing-48: 48px;

  /* Border Radius */
  --radius-md: 6px;
  --radius-lg: 10px;
  --radius-xl: 14px;
  --radius-2xl: 18px;
  --radius-3xl: 24px;

  /* Shadows */
  --shadow-subtle: oklab(0.145 -0.00000143796 0.00000340492 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px;
  --shadow-subtle-2: lab(2.75381 0 0) 0px 0px 0px 0px;
}
```
