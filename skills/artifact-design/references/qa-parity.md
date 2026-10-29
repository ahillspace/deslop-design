# Before-and-after parity and completion evidence

Use this reference for any authorized change to an existing artifact, especially a redesign, rewrite, data view, control, or document export.
For review-only work, use the same evidence model without modifying the source.

## Record what must survive

Before editing, identify the target revision and the facts and behavior in scope.
Create a compact comparison ledger for material content and claims: wording or value, units, denominator, date, attribution, citation or URL, qualification, and location.
Record required sections, legal text, meaningful visual relationships, controls, input rules, destinations, permissions, persisted data, and normal, empty, pending, error, success, retry, cancel, and undo states that the artifact supports.
Distinguish protected behavior from a behavior change the user authorized.

Do not treat a visual simplification as permission to remove expert detail, caveats, links, data, controls, or a supported route.
If content cannot fit the chosen layout, change the layout or present a complete alternative.
If parity cannot be confirmed, leave the claim or behavior intact and report the unresolved conflict.

## Match evidence to the claim

- **Source inspection** supports what files declare or contain; it does not prove rendered output or runtime behavior.
- **Rendered inspection** supports only the version, state, viewport, page, content, and theme actually opened.
- **Interaction check** supports only the action sequence actually exercised.
- **Keyboard or assistive-technology check** supports only its recorded path and environment.
- **Automated check** supports only the tool's stated scope and result; a clean scan proves neither conformance nor comprehension.
- **Print/export inspection** supports only the actual generated file and pages inspected.
- **User evidence** requires a real, authorized method and participants; an expert walkthrough is not user testing.

Keep these evidence classes separate in the delivery note.
Do not infer a backend result from a local prototype or an editable document source from a screenshot or fixed PDF.
If the browser, export, source, or state is unavailable, name the gap and what it prevents you from claiming.

## Compare and retest

After editing, repeat the content ledger and compare figures, units, dates, links, citations, quotations, qualifications, required sections, data transformations, and actions.
Inspect full relevant screen or document sequences, not only the opening view.
Render HTML at appropriate wide and narrow sizes; include long content, zoom, reduced motion, high contrast, or print when those conditions affect the change.
Walk the main task with the input methods and states that changed.
Check console and failed requests when relevant.
Repeat the exact view or sequence that revealed the defect, then check an adjacent state likely to regress.

For a factual or data change, trace source values and verify at least representative edge values, total or denominator, unit, and exception.
For a control change, check normal result, failure and recovery, repeated activation, and overlap/cancel where relevant.
For a document, inspect reading sequence, headings, figures, tables, captions, links, pagination, and exported order when available.
Use safe fixtures for error states; do not perform a real purchase, deletion, or other destructive action to manufacture evidence.

### Quantitative chart geometry

When a chart uses a numeric position scale, verify that ticks, marks, reference lines, and value labels use one data-to-position mapping and the same plot bounds.
For a linear 0-to-5 scale, check the expected normalized positions for 0, 2, 4, and 5: 0%, 40%, 80%, and 100%; a value of 4.6 maps to 92%.
At each relevant rendered width, record the domain, plot bounds, viewport, expected coordinates, measured coordinates, and any deviation.
Measure the mark endpoint, tick anchor, and reference line in CSS pixels from the rendered plot bounds, using browser geometry when available or a screenshot converted by its device scale factor.
Compare each coordinate with `x0 + ((v - dmin) / (dmax - dmin)) * (x1 - x0)` for a linear scale, allowing only the browser's subpixel rounding at the measured width.
Repeat after responsive reflow wherever the chart remains visible, because the absolute coordinates change while each value's normalized position must remain stable.
Inspect source or chart code for a shared domain and mapping, but do not treat that inspection as proof of rendered alignment.
Reconcile the plot against the exact-value table or source data, and state which rendered widths and geometry checks were actually inspected.

Report changed and preserved material, checks run, observed result, unresolved defects, and unverified areas.
A complete statement means only that named checks passed within their stated scope.
If a material blocker remains or an essential check is unknown, state its effect instead of claiming readiness.
