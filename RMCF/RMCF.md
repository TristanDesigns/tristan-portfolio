# Rocky Mountain Cigar Festival — Style Reference

> Lime and gold marquee on a blacked-out room

**Theme:** dark

RMCF is a night-time festival system: a near-black room with lime-green ornament, burnished gold marks, and ash-grey type. It borrows its structure from three places at once. From **Volt** it takes the colour-block logic — whole sections flood one flat tone, with colour itself doing the dividing — and the ultra-heavy condensed display type set at a compressed line height so headlines stack like a marquee. From **Franky's** it takes the ticketed, printed-collateral texture: monospace micro-labels, a checkerboard band under the header, and small hard-edged chips that read like stubs and passes. From **Structured** it takes the restraint that keeps it from becoming a poster — hairline rules, small 9px radii on containers, generous quiet space, and a serif reserved for pull quotes. Lime is the loud voice, gold is the mark, ash is the reading voice, and everything sits on black.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Stage Black | `#0A0A0A` | `--color-stage-black` | Page ground. The room the whole system is staged in |
| Riser | `#141414` | `--color-riser` | Elevated panel one step off the ground — cards, fold bodies, media frames |
| Festival Lime | `#A8D24E` | `--color-festival-lime` | The signature. Ornament, display headlines, primary button fill, open-accordion mark. Sampled from the event's ornamental frame artwork |
| Lime Bright | `#C2E86A` | `--color-lime-bright` | Hover and focus lift for lime elements only. Never a fill on its own |
| Burnished Gold | `#C9A24B` | `--color-burnished-gold` | The mark colour — logo lockup, year badges, serif pull quotes, vendor and sponsor rules |
| Ash | `#C9C5BC` | `--color-ash` | Primary reading colour on black. Warm grey, never blue-grey |
| Ash Dim | `#8A867E` | `--color-ash-dim` | Secondary copy, captions, meta lines, timestamps |
| Bone | `#F2EFE6` | `--color-bone` | Highest-emphasis type — hero headline, numbers, anything that must out-read ash |
| Hairline | `rgba(242,239,230,0.16)` | `--color-hairline` | Every rule, card edge and divider. One border colour across the system |

## Tokens — Typography

### Anton — Display only. Uppercase, weight 400, `0.9` line height, `+0.01em` tracking. Headlines stack into a solid marquee block. This is the Volt inheritance and it is the loudest element in the system. · `--font-display`
- **Substitute:** Oswald, Archivo Black
- **Weights:** 400
- **Sizes:** 28, 36, 48, 64, 88
- **Line height:** 0.88–0.95
- **Role:** Hero headline, section headings, fold titles, stat values.

### Playfair Display — The serif counterpoint, reserved for pull quotes and a single editorial statement per section. Weight 500 at `-0.01em`, sentence case rather than caps. Used in gold, never lime. This is the Structured inheritance — it is what stops the page reading as a flyer. · `--font-editorial`
- **Substitute:** Lora, Spectral
- **Weights:** 400, 500
- **Sizes:** 22, 28, 34
- **Line height:** 1.15–1.3
- **Role:** Pull quotes, vendor callouts, one-line editorial statements.

### Inter — All body and interface text. Weight 400 for prose, 500 for buttons and labels. Set in ash on black at a comfortable measure. · `--font-body`
- **Substitute:** Söhne, Helvetica Now
- **Weights:** 400, 500
- **Sizes:** 13, 14, 15, 16, 17, 18
- **Line height:** 1.5–1.65
- **Role:** Body copy, buttons, navigation, card text, footer.

### VT323 — Ticket texture. Uppercase micro-labels only: year badges, lineup indices, pass tiers, image captions. `+0.08em` tracking at 13–15px. This is the Franky's inheritance and it must stay small and sparse — it is seasoning, not a body face. · `--font-ticket`
- **Substitute:** Silkscreen, IBM Plex Mono
- **Weights:** 400
- **Sizes:** 13, 14, 15
- **Letter spacing:** +0.08em, uppercase
- **Role:** Year badges, fold indices, pass/tier chips, photo captions.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| ticket | 13px | 1.2 | +0.08em | `--text-ticket` |
| caption | 14px | 1.4 | — | `--text-caption` |
| body | 17px | 1.6 | — | `--text-body` |
| lead | 18px | 1.55 | — | `--text-lead` |
| quote | 28px | 1.2 | -0.01em | `--text-quote` |
| h3 | 28px | 0.95 | +0.01em | `--text-h3` |
| h2 | clamp(30px, 4.5vw, 48px) | 0.92 | +0.01em | `--text-h2` |
| hero | clamp(44px, 7vw, 88px) | 0.88 | +0.01em | `--text-hero` |

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
| 36 | 36px | `--space-6` |
| 56 | 56px | `--space-7` |
| 80 | 80px | `--space-8` |
| 120 | 120px | `--space-9` |

### Border Radius

| Element | Value |
|---------|-------|
| cards | 9px |
| media | 9px |
| icons | 9px |
| buttons | 22px |
| chips | 4px |

### Borders

| Name | Value | Token |
|------|-------|-------|
| hairline | 1px solid `rgba(242,239,230,0.16)` | `--border-thin` |
| lime rule | 1px solid `#A8D24E` | `--border-lime` |

### Shadows

None. See **Elevation**.

### Layout

- **Page max-width:** 1180px
- **Section gap:** 80–120px
- **Card padding:** 24–36px
- **Element gap:** 12–16px

## Components

### Lime Button — Primary
**Role:** Tickets, main conversion

Festival Lime fill, Stage Black label, no border, `22px` radius, `11px 22px` padding, Inter 500 at 15px. Lime on black is the highest-contrast pairing in the system — reserve it for the single most important action in a view.

### Ghost Button — Secondary
**Role:** Companion action

Transparent fill, ash label, `1px` hairline border, `22px` radius, same padding and type as primary. Never gold-filled — gold is a mark colour, not an action colour.

### Ticket Chip
**Role:** Year badge, pass tier, lineup index

VT323 uppercase at 13px with `+0.08em` tracking, `4px` radius — the only near-square corner in the system, deliberately, so it reads as a punched stub. Either a `1px` hairline outline with ash text, or a solid gold fill with black text for the current/featured item.

### Nav Bar
**Role:** The one persistent chrome on the page

Shared across all three case-study pages — same structure, same behaviour, same class names (`.pnav`, `.pnav-inner`, `.pnav-links`), only the skin changes. The `tristan` wordmark sits left, the page's section links right. **It is only present on the way up:** at rest when the page is at the top, it slides out of view on any downward scroll past the first 80px and returns on any upward scroll, with a 6px dead zone so a jittery trackpad never flickers it. Under 760px the links drop away and the wordmark stands alone. Section targets carry `scroll-margin-top` so a jump never lands under it.

Here it is a Stage Black bar with a hairline underneath, the wordmark in bone, and links as VT323 uppercase ticket text in ash that go lime on hover — the nav reads as a row of stubs. It is fixed rather than sticky because the hero is a full-viewport fixed video with nothing above it to displace.

### Checkerboard Band
**Role:** Header underline and major section break

A `16px` tall strip of alternating Stage Black and Festival Lime squares at `16px` pitch, sitting directly beneath the header and above the footer. The one piece of pure ornament in the system, and the clearest Franky's inheritance. Use it exactly twice per page — more and it becomes a pattern rather than a marker.

### Colour Room
**Role:** Full-bleed section ground

Most sections are Stage Black. A section may instead flood Festival Lime — in which case *all* type inside it flips to Stage Black — or Riser for a quieter panel. Never two consecutive non-black rooms, and never more than one lime room per page.

### Card
**Role:** Work tile, vendor card, role card

Riser fill, `9px` radius, `1px` hairline border, no shadow, 24–36px padding. Anton title, ash body, optional gold ticket chip. On a lime room, cards invert to Stage Black fill with a lime hairline.

### Pull Quote
**Role:** One editorial statement per section

Playfair Display 500 at 28px in Burnished Gold, sentence case, no quotation-mark ornament, no card — it sits directly on the black ground with a `1px` lime rule above it and 36px of clearance on both sides.

### Glance Stub
**Role:** The brief in three tiles, directly under the hero

The standard Card — Riser fill on the black stage, `1px` hairline, `9px` radius, 24px/26px padding — so the row uses the same surface as everything else on the page. Each opens with the same gold ticket tag the section heads use (*The job*, *The outcome*), then Inter 16.5px ash prose. The outcome stub inverts to Festival Lime with its tag flipped to Stage Black-on-lime and its line set in Anton uppercase at 22–28px — the one lime surface in the row. Two across, never more: the brief and the payoff. Nothing in the row introduces a face, a chip or a surface the rest of the page does not already use.

### Brand Kit
**Role:** The body of section 01, Brand identity

A four-column strip at 28px gaps, filling the section body on a Riser room: the lockup in a hairline 9px frame on Stage Black (200px), the palette as four 64px swatches in a 2×2 (150px), the typefaces as Anton 26px names over Inter 13px ash-dim notes between hairline rules, and the icon marks as Stage Black pills. Column labels (*Palette*, *Type*, *Icons*) are Inter 600 12px uppercase in ash-dim, one step quieter than the section's gold tag. Collapses to one column under 820px. No card chrome — it is section content, not a tile.

### Open Section Head
**Role:** Heading for a work section that is always visible

The fold head without the toggle: `[index] [title block]` in a two-column grid. Index is the ticket chip, title block is gold ticket chip, Anton title, optional one-line gist in ash-dim. The work follows after 44px. Every section on the page uses this head, 01 through 05.

### Accordion Toggle
**Role:** Expand/collapse, kept in the system for the rare fold — the RMCF page itself has none

`52px` square, transparent fill, `1px` hairline border, `9px` radius. Star mark at `1.5px` hairline stroke, plus/minus at `2px` in bone. On open, the plus collapses to a minus and the star fills Festival Lime. No shadow, no press transform.

### Media Frame
**Role:** Photography and video container

`9px` radius, `1px` hairline border, no shadow. Images run at full saturation — the festival photography carries the colour and must not be tinted to match the palette.

### Footer
**Role:** Page-end block

Stage Black ground above a checkerboard band. Anton headline in bone, ash body, ash-dim meta, gold lockup, and a lime primary button.

## Do's and Don'ts

### Do
- Keep the page overwhelmingly black. Lime, gold and ash are marks *on* the room, not the room itself.
- Set every headline in Anton uppercase at a line height of 0.88–0.95 so multi-line headlines stack as one block.
- Use lime for a short list of jobs only: ornament, the primary button, the open-accordion mark, the outcome stub in the glance row, and the alternate campaign frames. Nothing else.
- Put the work first. Story, roles, process and stats live in the glance row as one of two stubs, never as a section between the reader and the work. The brand kit is the exception: it *is* work, so it leads as section 01.
- Use gold for marks and editorial voice — logo lockup, year badges, serif pull quotes — never as a button fill.
- Set body copy in ash `#C9C5BC`, not bone; reserve bone for headlines and numbers that must out-read the body.
- Keep every rule, card edge and divider on the single hairline value. One border colour, one weight.
- Keep VT323 sparse, uppercase and under 15px. It is ticket texture, not a body face.
- Let photography stay fully saturated inside its hairline frame.

### Don't
- Never put lime text on gold, or gold text on lime — the two accents are close in luminance and the pairing is unreadable.
- Never add a shadow, glow, or bevel. Elevation is one step of surface lightness plus a hairline.
- Never set Anton below 28px or above 0.95 line height; Inter handles everything smaller and the loose leading kills the marquee.
- Never use VT323 for a sentence, and never in lowercase.
- Never run two non-black colour rooms back to back, and never more than one lime room on a page.
- Never tint, duotone or desaturate the festival photography to match the palette.
- Never use a radius outside the set — `9px` containers, `22px` buttons, `4px` ticket chips.
- Never introduce a fourth hue. If something needs to stand apart, change its surface level or its type weight.
- Never run the page as a stack of folds — the RMCF page has none, and if one is ever unavoidable it goes last. Never a stats band, and never a pull quote that restates the paragraph beside it.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Stage Black | `#0A0A0A` | Page ground, the default for almost every section |
| 1 | Riser | `#141414` | Cards, fold bodies, media frames — one step up, no shadow |
| 2 | Lime Room | `#A8D24E` | A single full-bleed inverted section per page; all type inside flips to black |

## Elevation

Zero shadow. Depth is a two-step surface stack — Stage Black to Riser — plus a single hairline border. Nothing floats, nothing glows. If an element needs more presence, raise its type weight, give it a lime mark, or move it into the lime room; never reach for a shadow, and never use a coloured glow around lime elements.

## Imagery

Two modes. The first is festival photography — crowds, tents, vendor booths, cigar rollers, live music, opening-hour shots — presented full-bleed inside `9px`-radius hairline frames at full saturation and no overlay. This is the page's colour beyond the three accents, and it must not be graded to match the palette. The second is the event's own printed collateral: posters, sponsor cards, and confirmed-guest announcements built on black with ornamental lime frames and gold lockups. Reproduce these unaltered — they are the source the palette was sampled from. No stock imagery, no abstract decoration, no gradients or light leaks. Icons are hairline geometric marks at `1.5–2px` in bone or ash, matching the border weight.

## Layout

Centred 1180px column on a black ground, with the checkerboard band directly under the hero and again above the footer. The page is built work-first and reads in this order:

1. **Hero** — full-viewport video stage: gold year chip, Anton headline at up to 88px, a row of ticket chips that jump to each section, then a single line of lead copy in ash. The hero says what the job was in one sentence and nothing more.
2. **Glance row** — two stubs directly under the checkerboard band: *The job* and *The outcome*. The outcome stub is punched lime with black type; it is the one lime surface in the row and the loudest thing on the page after the hero. Two stubs, side by side, nothing else — this row replaces stats bands, story paragraphs and discipline lists. The disciplines are visible in the section headings below, so they are not listed twice.
3. **The work, open** — five numbered sections, each mono index, gold ticket tag, Anton title, an optional one-line gist, then the work itself at full width. No toggle, nothing to click. **01 is always Brand identity** — the lockup, palette, typefaces and icon marks the rest was built from — because the system is the first piece of work, not a footnote to it. Campaigns, Photography, Film and Evolution follow as 02–05. A gist earns its place only when it says something the title and the work do not.
4. **Footer** — the second checkerboard band, then the sign-off on black.

There are no folds on the page. If one is ever unavoidable it goes last, and there is only ever one.

Media sits in hairline frames, either full-width or as a grid. Sections alternate Stage Black and Riser rooms, separated by 80–120px.

## Agent Prompt Guide

**Quick Color Reference**
- Page ground: `#0A0A0A`
- Panel: `#141414`
- Body text: `#C9C5BC`
- High-emphasis text: `#F2EFE6`
- Muted text: `#8A867E`
- Border: `rgba(242,239,230,0.16)`
- Accent / primary action: `#A8D24E` lime with `#0A0A0A` label
- Mark / editorial: `#C9A24B` gold

**Example Component Prompts**

1. **Hero** — Full-bleed `#0A0A0A`. Gold ticket chip in VT323 13px uppercase `+0.08em`, 4px radius, 1px `#C9A24B` outline. Headline in Anton 400 uppercase `clamp(44px,7vw,88px)`, line-height 0.88, `#F2EFE6`. Row of ticket chips beneath. Lead copy in Inter 400 18px `#C9C5BC`, max-width 68ch. Primary button `#A8D24E` fill, `#0A0A0A` label, 22px radius, 11px/22px padding.

2. **Checkerboard band** — Full-width strip 16px tall directly beneath the header: `repeating-conic-gradient` alternating `#0A0A0A` and `#A8D24E` at a 16px pitch. Exactly two per page — header and footer.

3. **Fold section head** — Grid of `[index] [title block] [toggle]`. Index in VT323 13px uppercase, transparent, 1px hairline, 4px radius. Title block: gold ticket chip, then Anton 400 uppercase `clamp(30px,4.5vw,48px)` at 0.92 line-height in `#F2EFE6`, then gist in Inter 15px `#8A867E`. Toggle: 52px square, transparent, 1px hairline border, 9px radius, star at 1.5px stroke plus a 2px plus/minus in `#F2EFE6`; star fills `#A8D24E` when open.

4. **Pull quote** — No card. A 1px `#A8D24E` rule, 24px gap, then Playfair Display 500 at 28px in `#C9A24B`, sentence case, max-width 46ch, 36px clearance left and right. Nothing else in the band.

5. **Work card** — `#141414` fill, 9px radius, 1px hairline border, 28px padding, no shadow. Media at 9px radius full saturation, Anton 28px uppercase title in `#F2EFE6`, Inter 15px body in `#C9C5BC`, optional gold ticket chip at the foot.

6. **Glance row** — Two-column grid, 24px gap, on the `#0A0A0A` stage. Each stub `#141414` fill, 1px hairline, 9px radius, 24px/26px padding. Gold ticket tag as label (VT323 15px uppercase, `#C9A24B` fill, `#0A0A0A` text, 4px radius), body in Inter 16.5px `#C9C5BC` at 1.55. The second stub fills `#A8D24E` with every line in `#0A0A0A` (tag flips to `#0A0A0A` fill with `#A8D24E` text), body set in Anton uppercase `clamp(22px,2.2vw,28px)` at 1.05. Collapses to one column under 820px.

7. **Open section head** — Two-column grid `[index] [title block]`, 26px gap, no toggle. Index and title block exactly as the fold head. The work follows after 44px, full width.

8. **Brand kit (section 01 body)** — On a `#141414` room, a grid `200px 150px 1.3fr 1fr` at 28px gap: lockup in a 1px hairline 9px frame on `#0A0A0A`; *Palette* as four 64px swatches wrapping 2×2; *Type* as two rows of Anton 26px uppercase `#F2EFE6` over Inter 13px `#8A867E`, hairline rule above each and below the last; *Icons* as `#0A0A0A` pills with `#F2EFE6` text and a hairline border. Column labels Inter 600 12px uppercase `+0.08em` `#8A867E`.

## Where the three sources land

| Inherited from | What it contributes |
|---|---|
| **Volt** | Colour-room sections, colour as the divider instead of rules, Anton display compressed to 0.88–0.95 leading, pill buttons, zero elevation |
| **Franky's** | Ticket texture — VT323 uppercase micro-labels, the checkerboard band, 4px punched-stub chips, printed-collateral feel |
| **Structured** | Restraint — a single hairline border colour, 9px container radii, generous 80–120px section gaps, and Playfair Display reserved for one editorial line per section |

When the three conflict, resolve in this order: **Volt sets the structure** (how sections are grounded and divided), **Structured sets the detail** (borders, radii, spacing, quiet), and **Franky's sets the seasoning** (chips, checkerboard, mono labels). Franky's never wins an argument about layout, and Volt never wins one about border weight.
