# Data displays and evidence integrity

Use this reference when charts, tables, metrics, comparisons, or data-dependent claims influence what a reader concludes or does.
Combine it with the report or tool genre and with documents, visual craft, accessibility, and QA references as needed.

## Trace the displayed claim

For each important display, record its location and state, question, data source, period and population, fields and units, denominator, aggregation or transformation, missing and excluded values, uncertainty, caption, and apparent reader task.
Trace displayed values to supplied data or code when available.
Reconcile enough source values to catch plausible transcription or transformation errors, including an endpoint, a range limit, and a highlighted exception where available.
Check totals, percentages, time range, denominator, units, and definitions across the title, axis, legend, caption, and underlying source.
Mark an untraceable value unknown; do not certify it from a screenshot.

Separate what the data show, what the author infers, and what action is requested.
Keep a limitation beside the claim it changes.
Do not invent a series, denominator, trend, causal explanation, method, uncertainty, population, or user need.
Clearly mark synthetic examples as synthetic.

## Choose and check an encoding

Pick the simplest display that answers the real comparison.
Bars or dot plots can compare a small set of categories; bar length normally needs a truthful zero baseline, while a labeled dot plot can show a narrow range without implying magnitude from zero.
Lines suit ordered continuous change; points or bars can suit sparse discrete periods.
Show distributions with their spread and relevant sample size rather than hiding variation behind one average.
Use a scatterplot for the relationship between two quantitative fields; add size only when a third quantity is meaningful and comparable.
Use stacked bars when totals matter, and 100% stacks only when shares matter and the lost total remains available where needed.
Use pie or donut slices only for a small set of mutually exclusive parts of one whole when those comparisons are useful.
Use a labeled table or ordered heat map for two categorical dimensions; provide exact values when decisions depend on them.
These are starting choices, not compulsory mappings.

Check which visual channel carries each value.
Position and length are generally easier to compare precisely than area, volume, angle, or color intensity.
Keep encodings and series order consistent across related views.
Show units, denominator, time or population scope, reference line, source, and missingness where readers need them.
Use labels, line style, pattern, or direct values alongside color when color alone would carry meaning.
Do not use an unlabeled axis, truncated baseline, decorative trend, or selective range to imply more change or certainty than the data supports.

Use a semantic table for exact records and multi-attribute comparison.
Give headers meaningful scope and associate them with values; align numeric material where it aids row comparison; preserve missing, zero, not applicable, and excluded as distinct states.
For a wide table, use a clearly named and keyboard-reachable local scroll region or an equivalent narrow presentation when it preserves every row and column relationship.
Do not create a page-wide overflow or hide evidence on small screens.

## Example: do not turn mismatch into delay

Suppose source data shows differing statuses in 11 of 18 reviewed requests, flags four possible duplicates that have not been verified, and contains no delay measurement.
A heading such as “61% were delayed” changes the meaning of the denominator and invents an outcome.
Use “Statuses differed in 11 of 18 reviewed requests,” keep the duplicate caveat and missing delay measure beside it, and label any proposed follow-up as a test.
Use a chart only if its encoding clarifies a comparison present in the source.
This example is synthetic and must not be copied as evidence.

## Preserve and verify

Before editing, record the source fields, transformed values, filters, exclusions, units, dates, caveats, captions, links, and interactive behavior that must survive.
After editing, compare the displayed values and labels against the same source and repeat the relevant state, filter, sort, and viewport checks.
Check that chart and table encodings tell the same story, highlighted values are correct, missingness remains visible, and exact data remain reachable.
Report whether checks used source data/code, rendered output, interaction, or only supplied images.
Do not claim that a clean plot, automated lint, or expert inspection proves the data or interpretation are correct.
