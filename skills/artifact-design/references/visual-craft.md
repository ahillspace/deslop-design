# Visual craft for screen and document artifacts

Use this reference for a visual audit or authorized visual redesign.
Treat hierarchy, composition, typography, color, density, affordance, and brand as connected choices that help a reader do the artifact's actual job.
For detailed format-specific print and reading-order work, also read [documents](documents.md).

## Observe before prescribing

Inspect the actual artifact across its relevant path, not only the opening screenshot.
Record version, viewport or page, theme, content, state, and evidence type.
Rendered output supports claims about what appeared in that render; source supports claims about declared structure and styles; neither alone proves behavior, semantics, or comprehension.
Mark observations, interpretations, and unknowns separately.

Start from the reader task, required content, actual behavior, supplied design rules, and available assets.
Classify design context as **established** (a current instruction or source), **inferred** (a repeated pattern supports a provisional direction), or **unknown** (evidence is missing, conflicting, or inaccessible).
Do not describe an inferred style as approved brand direction.
Do not infer identity from one isolated color, logo, corner radius, or screenshot.

## Audit the visual system as a whole

### Hierarchy and emphasis

Name what the reader needs to notice first, next, and later for this task.
Compare size, weight, contrast, position, spacing, grouping, imagery, shape, density, and motion as a combined signal.
Follow the actual reading path; do not impose an F-pattern, Z-pattern, top-left start, one dominant item, or fixed size ratio.
Check whether an emphasis is earned by its task importance and evidence, and whether required caveats, units, status, and recovery remain findable.
When styling cannot clarify the relationship, change grouping or order instead.

### Composition and spatial relationships

Map the full composition: main regions, shared edges, visual mass, repeated cadence, large gaps, narrow measures, and page or spread transitions.
Check balance without requiring symmetry; compare spacing within groups against the spacing between groups; let repeated content share a useful rhythm without making every interval identical.
Use alignment, proximity, common region, similarity, continuity, and figure-ground as cues that can reinforce or contradict one another.
Choose a content-fit grid: decide which items share an edge, which need a reading measure, which may span, and when an arrangement must reflow.
Use the lightest grouping cue that stays clear.
Add a boundary when a dense group or actionable unit needs one; do not put every item in a card.

### Typography and density

Inspect actual strings, font loading and fallback, glyph support, line breaks, optical weight, reading measure, leading, labels, numeric columns, and long or multilingual content when present.
Choose a small set of semantic type roles that fit the artifact; keep the established system when it works.
Treat a `ch` measure, type scale, ratio, and common spacing value as a starting point, not a standard.
Align figures with tabular numerals where repeated comparison benefits and the face supports them; preserve signs, decimals, units, dates, identifiers, and exact values.
Do not shrink essential type or remove specialist detail to fit a preferred desktop grid.

Judge density against the reader's task and experience, not a universal amount of content.
Remove duplication, irrelevant choices, and repeated setup only when they add no distinct meaning.
Keep useful expert material, exceptions, evidence, and controls visible.
Use a summary or disclosure only when readers can still reach the full basis and act without losing context.
Disclose a simplified view if it changes what is available; do not invent a "simple mode" by hiding evidence.

### Color and semantic roles

Map actual use to role: canvas, surface, primary and supporting text, border, link, action, focus, selection, status, chart series, or other established meaning.
Measure rendered foreground/background pairs when making a contrast claim; account for opacity, overlays, gradients, imagery, and theme state.
Do not promote an unmeasured screenshot sample to a ratio.
Use color with labels, shape, position, or text when meaning must survive color differences or forced colors.
For WCAG claims, load [accessibility](accessibility.md) and use its exact criterion, exception, and target.
Do not require dark mode or a complete tonal palette when the task does not call for them.

### Affordance and visual brand

Make navigation look navigable, actions look actionable, selection and status distinguishable, and static labels look static.
Use links for destinations and buttons for actions; keep contextual controls near the content they affect.
Use a visible label for important actions when an icon alone cannot name the result.
Size the interactive hit area, not just its glyph, and leave enough space to avoid neighboring activation.
Separate a usability preference from a WCAG requirement; see [responsive behavior](responsive.md) and [accessibility](accessibility.md) for exact target-size rules.

Recover visual intent from relevant project guidance, tokens, components, current surfaces, content conventions, and real assets.
Prefer explicit current decisions over isolated implementation accidents.
When no direction exists, choose a specific, coherent, reversible direction from subject, task, content, and available assets.
State what informed it and what it changes.
Outside references may suggest a quality to adapt; do not clone their signature layouts, assets, or distinctive treatment.
Check image rights and provenance before using an asset as evidence or brand expression.

When a direction needs explanation, connect a small set of concrete qualities to the evidence and to decisions in type, color roles, composition, image treatment, density, and interaction.
Terms such as “warm,” “precise,” or “quiet” are useful only when the reference or artifact shows what they mean in this context.
Do not impose a fixed number of mood words, references, anti-references, colors, or principles.
Use the task, medium, content, audience evidence, and situation to decide which visual traits matter.
Treat voice as evidence from relevant copy samples or stated guidance; use [copy](copy.md) when words will change.
Treat a reference's observed treatment as a trace of that artifact, not an instruction to reproduce it.
For a borrowed idea, name the transferable quality, the local reason it fits, and the product-specific detail that should not transfer.
When token use is part of the reasoning, record semantic role, current value, intended use, theme/state, and a justified exception; see [tokens](tokens.md).

## Three contextual construction studies

These examples show how to turn a visual direction into working structure and values.
They are trial settings for the described content, not defaults or standards.

### Pair a reading measure with a nearby annotation

For a field report with one short method note beside each section, keep prose and its note in the same semantic section.
The asymmetric desktop grid gives the main reading column room while keeping the note attached to its subject.
Because the note follows the prose in source order, stacking at a narrow width keeps the relationship and reading order intact.

~~~html
<section class="reading-pair" aria-labelledby="station-heading">
  <div class="reading-copy">
    <h2 id="station-heading">North channel reading</h2>
    <p>The sample measured 4.6 mg/L nitrate-N on 4 April.</p>
  </div>
  <aside class="reading-note" aria-label="Sampling note">
    The comparison limit is 4.0 mg/L nitrate-N.
  </aside>
</section>
~~~

~~~css
.reading-pair {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(13rem, 17rem);
  justify-content: space-between;
  align-items: start;
  gap: clamp(2rem, 5vw, 4.5rem);
}

.reading-copy { min-width: 0; max-width: 64ch; }

.reading-note {
  border-inline-start: 2px solid var(--rule);
  padding-inline-start: 1rem;
  font-size: .875rem;
  line-height: 1.45;
}

@media (max-width: 56rem) {
  .reading-pair { grid-template-columns: minmax(0, 1fr); gap: 1rem; }
  .reading-note { margin-inline-start: 1rem; }
}
~~~

Try the breakpoint against the actual longest heading and note at the target widths.
At 320 CSS pixels, confirm the note follows its own section and the page does not gain horizontal scrolling.
If a note qualifies a whole table or chart instead of one prose section, place it with that object and use the relevant [document](documents.md) guidance.

### Trial an optical type hierarchy against real text

For a roughly 700-word station report headed “North channel readings after the spring sampling round,” a useful first browser trial is a 42-52px display heading, a 19px deck, 17px body copy at about 1.6 line height, and 14px labels at about 1.3 line height.
On a 390px phone, check that this title breaks naturally within about 17 characters per line and the body measure is close to 60-64 characters per line on a wide screen.
At 768px and 1440px, verify the deck remains subordinate and the heading does not leave a short stranded word.
Adjust these trial values to the actual title, glyph shapes, font loading, and reading context.

~~~css
.report-title {
  max-width: 17ch;
  font: 700 clamp(2.625rem, 2rem + 2vw, 3.25rem)/1.05 Georgia, "Times New Roman", serif;
  letter-spacing: -.025em;
}

.report-deck {
  max-width: 54ch;
  font: 400 1.1875rem/1.45 system-ui, sans-serif;
}

.report-body {
  max-width: 64ch;
  font: 400 1.0625rem/1.6 Georgia, "Times New Roman", serif;
}

.report-label {
  font: 650 .875rem/1.3 system-ui, sans-serif;
  letter-spacing: .03em;
}

.measurement { font-variant-numeric: lining-nums tabular-nums; }
~~~

The Georgia stack is a dependency-free trial, not a required face.
Inspect the loaded face and its glyph coverage, then check title shapes and alignment with actual names, dates, decimals, minus signs, and units.
Keep tabular numerals only where aligned comparison helps, and confirm the loaded face supports the feature; do not force it across prose.

### Build a small semantic palette from measured pairs

For a quiet field report, this sample assigns a warm canvas, dark reading ink, restrained green action, and a separate warning surface.
The listed WCAG contrast ratios are calculated from the opaque sRGB hex pairs shown; measure the rendered foreground and background again if opacity, overlays, images, or theme changes apply.

| Role | Foreground | Background | Sample contrast |
|---|---|---|---:|
| Body text | `#202B39` | `#F7F4EC` | 13.03:1 |
| Supporting text | `#536270` | `#F7F4EC` | 5.71:1 |
| Link and focus | `#1D5D52` | `#F7F4EC` | 6.97:1 |
| Action label | `#FFFFFF` | `#1D5D52` | 7.66:1 |
| Warning text | `#7A2E00` | `#FBE8D8` | 7.95:1 |

Carry meaning in text, position, shape, or an icon as well as color.
For example, label the warning and keep the relevant reading beside it rather than relying on the orange surface alone.
Check component boundaries, focus visibility, links, charts, and forced-colors behavior in context; the example ratios do not verify those details.
Use the exact criterion and exception from [accessibility](accessibility.md) when making a conformance claim.

## Turn findings into a repair

For a craft finding, report `location / viewport or page and state / visible evidence / likely mechanism / reader consequence / specific remedy / confidence`.
Distinguish a visible mismatch from a predicted user effect.
Say what works and should survive.
Rank by task failure, misleading emphasis or evidence, access barrier, substantial friction, then local polish.
Do not score taste or report a checklist percentage.

For an authorized redesign, make the smallest coherent change that resolves the diagnosed mechanism.
Tie type, color roles, density, composition, imagery, and interaction emphasis together for an explainable reason.
Every chart, photograph, diagram, timeline, table, annotation, and typographic device must clarify actual content, evidence, sequence, comparison, or action.
Use a visual device because it serves this material, not to satisfy a recipe.

### Example: an evidence table

Suppose a report gives every row of a 12-location table a strong fill, while two incomplete readings are called out in a remote footnote.
The repeated fill no longer distinguishes a useful status, and the remote note leaves readers to infer which values are incomplete.

Keep the 12 rows and all supplied values.
Return ordinary rows to a quieter treatment, label the two incomplete readings in their cells, and move the qualification beside the table heading or caption.
At desktop and narrow widths, verify the labels remain associated with each value and the meaning remains clear without color.
This example shows a proposed repair, not measured reader behavior.

## Finish with evidence

Reinspect the full relevant path, including long content, middle and end sections, exceptional states, adjacent viewports, enlargement, and print when applicable.
Confirm hierarchy, grouping, alignment, wrapping, crop, contrast, and reflow in the rendered output where available.
Confirm keyboard, state, or semantic behavior only through those checks, not a screenshot.
Compare protected content and behavior with the source using [QA parity](qa-parity.md).
Report source, rendered, interaction, automated, and user evidence separately.
Leave unavailable checks explicitly unverified with their practical consequence.
