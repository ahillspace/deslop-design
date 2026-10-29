# Reading semantics and content equivalents

Use this reference when headings, reading order, links, alternatives, captions, tables, transcripts, or conversion between formats affect the artifact.
For widget behavior use [keyboard](keyboard.md); for standards-based findings use [accessibility](accessibility.md); for long-form argument use [documents](documents.md).

## Check structure independently of appearance

Read content in the reader's likely sequence, then inspect its semantic or document structure separately.
Trace the title, sections, figures, tables, notes, footnotes, sidebars, and ending.
Check that source or DOM order still communicates meaning when styling is removed or columns reflow.
Do not impose an inverted-pyramid order on narrative or technical material whose sequence carries meaning.

Inspect headings in source order and compare their levels with actual nesting.
Make the heading name its subject, finding, question, or action.
Do not demand exactly one `h1`, prohibit every skipped number as an automatic WCAG defect, or force a maximum depth; correct a level that misstates a real parent/child relationship.
Separate heading semantics from styling so a visual title remains a heading when restyled.

Inspect link names in context and, where useful, as a list without surrounding text.
The link should identify the destination or action at a useful level of detail; a repeated “Read more” needs programmatically available context to distinguish destinations.
These phrases are inspection cues, not categorical failures.
Check that link text matches the real destination, file type, and context change when those details affect the reader's choice.

## Match alternatives to the visual's function

Decide whether each image or figure is decorative, redundant, functional, informative, or complex.
For HTML images, leave decorative and redundant content out of the reading stream with an empty alternative; give a functional image the action or destination name when no adjacent control name already does so.
Describe an informative image by the detail relevant to the nearby content.
For a complex chart or diagram, provide a concise orientation and make essential values or relationships available in nearby text, a table, or a linked long description.
Do not guess an unexplained image's purpose.
If its meaning cannot be established, report that gap instead of inventing an alternative.

Use real text when an image of text can be replaced without losing its role.
For audio or synchronized media, inspect the actual words, speaker attribution, meaningful sounds, and relevant visual instructions.
Use the exact criterion and level for the media type before making a compliance claim.
Do not impose universal caption character counts, transcript form, or playback speed as WCAG law.

## Preserve data relationships

Use semantic tables for data relationships, not page layout.
Mark real header cells and associate them with values; use `scope` when it clarifies direction and explicit `id`/`headers` associations only for complex multi-level structures that need them.
A caption often helps identify a table but is not a universal conformance requirement.
Do not replace dense comparisons with cards if the reformatting breaks row/column relationships or hides exact values.
For a wide table, follow the responsive and keyboard routes as well as the data guide.

### Example: the chart and its caveat

If a chart's alternative says only “bar chart” while its conclusion depends on a partial final quarter, provide a concise text equivalent of the supported comparison and retain the partial-period note beside it.
Keep exact counts in a nearby table when the reader needs them.
If the evidence does not support a conclusion, describe the marks and scope instead of inventing a takeaway.

## Verify and report

Compare claims, values, units, quotes, links, caveats, definitions, and meaningful voice against the supplied source.
Read the heading outline, open links that changed, inspect alternatives beside their visuals, and navigate tables with their headers.
Check rendered or exported reading order and relevant responsive states when available.
Report source, render, keyboard, assistive-technology, and user evidence separately.
An HTML source check does not prove exported PDF order or assistive-technology announcements.
An automated scanner or a plausible visual layout does not establish accessible reading.
