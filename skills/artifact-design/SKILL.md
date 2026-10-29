---
name: artifact-design
description: Create or substantially redesign HTML reports, dashboards, explanatory pages, and landing pages with content-led structure and deliberate visual decisions. Skip backend work and small factual or style corrections.
---

# Artifact design

Make the artifact serve a particular reader and task, with useful words and a coherent visual system.
User and project requirements govern; preserve the established design system, then apply surface decisions and this guidance.
A missing design document does not mean a blank slate.
Scale the process to the change; do not make a small refinement into a branding exercise.

## Establish the material

Read the brief, implementation, representative content/data, components, assets, and existing design decisions.
Name the intended reader, their question or action, and the observable outcome.
Separate supplied facts, supported interpretation, illustrative material, and unknowns in a compact working note.
Track sources, dates, units, definitions, and caveats where claims depend on them.
Never invent customers, results, quotes, metrics, prices, availability, or capabilities to fill a layout.
Ask when missing facts change the goal; otherwise state a reversible assumption and proceed.
Keep unresolved proof visible in drafts and disclose it at delivery.

Choose guidance for the surface's job, rather than the product's industry.
Read only the relevant reference, combining them only for genuinely mixed surfaces:

- [Reports](references/reports.md): conclusions supported by evidence, comparisons, and methods.
- [Dashboards and internal tools](references/tools.md): repeated decisions and operations.
- [Editorial and explanations](references/editorial.md): sustained reading and understanding.
- [Landing pages](references/landing.md): a specific offer and an informed next action.
- [Copy](references/copy.md): load when forms, recovery, terminology, or persuasive claims need additional work.

Outline the information before styling it.
Draft actual headings, captions, controls, and representative long content early; start with the hardest table, figure, or state.
Give every section a reader purpose.

## Choose and implement

For an open direction, briefly compare up to three meaningfully different compositions if that helps resolve uncertainty.
Use relevant references when available, including quiet functional work rather than only galleries.
For each, record its URL/date or pin, audience and viewing conditions, the observed principle, why it works, its proposed application, and what must not transfer.
References inform decisions; they do not authorize copying identity, prose, layouts expressed as code, or assets.
Check individual asset terms and preserve creator, source, license, required credit, and modifications.
Prefer supplied or verified local assets; public visibility is not a reuse grant.

Choose the direction for reasons tied to the content and task.
Record only useful decisions: hierarchy, alignment/grid, density, type roles/measure/scale, color roles, spacing rhythm, media treatment, interaction states, and narrow-screen priorities.
Let a few related choices carry character while supporting content stays legible.
Fonts, cards, gradients, borders, motion, and familiar layouts are options, neither universal requirements nor universal defects.
A style label or random palette is not a rationale.

Use semantic HTML and the project's components/tokens.
Prefer native behavior; use an established accessible primitive for complex interaction when needed.
Do not introduce a framework for a simple document.
Preserve source detail and meaningful distinctions such as missing versus zero.
Implement applicable focus, hover, active, pending, disabled, empty, error, and success states, with truthful feedback.
Keep critical content and actions usable with keyboard, zoom, reduced motion, and narrow screens.

## Verify and deliver

Inspect the actual rendered artifact with available browser tooling after fonts and images settle.
Review desktop and mobile composition, long content, keyboard use, primary actions, relevant failure states, console/network errors, and available accessibility findings.
Check reflow at 320, 390, 768, and 1440 CSS px unless the target requires different sizes; intentional wide-table scrolling must remain usable.
If browser access is unavailable, label the result as source-checked with visual and interaction verification pending.

For a dedicated critique, optionally use [artifact-review](../artifact-review/SKILL.md); design does not depend on it.
Without it, rank observed defects by user impact, repair within scope, and recheck the touched views and behavior.
Stop after three repair rounds or the agreed budget; disclose unresolved blockers instead of calling an unfinished result complete.
Deliver the artifact, useful retained decisions, executed checks, and specific limitations without claiming professional equivalence.
