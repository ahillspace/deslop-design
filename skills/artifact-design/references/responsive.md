# Responsive behavior and user scaling

Use this reference when screen content must remain useful across widths, zoom, orientation, text expansion, image conditions, or input contexts.
For print, use [documents](documents.md); for exact WCAG evidence, use [accessibility](accessibility.md).

## Inspect where the content fails

Map reading order, essential content and actions, controls, data views, media, captions, navigation, and relevant states.
Mark content that inherently needs two dimensions, such as a detailed table, separately from prose and controls.
Use rendered evidence at widths where the actual layout changes or fails.
The 1440, 768, 390, and 320 CSS-pixel checks in the main skill are useful sample points, not a required breakpoint scheme or a complete conformance test.
Inspect source to identify fixed dimensions, min-content overflow, clipping, nowrap labels, absolute positioning, hidden-only-at-mobile content, images without fit rules, sticky overlays, and columns that cannot collapse.
Source alone does not prove the rendered result.

Exercise browser zoom and text growth.
To claim WCAG 2.2 SC 1.4.10 Reflow, test the applicable criterion: vertically scrolling content must work at an equivalent 320 CSS-pixel width (often 1280 CSS pixels at 400% zoom); horizontally scrolling content is evaluated at an equivalent 256 CSS-pixel height.
Allow only content whose use or meaning requires two-dimensional layout, and keep that region contained so it does not force surrounding prose to scroll sideways.
A 200% enlargement check can expose defects but is not by itself the SC 1.4.10 test.

For WCAG 2.2 SC 1.4.12 Text Spacing, test the specified user overrides: line height at least 1.5 times font size, paragraph spacing at least 2 times font size, letter spacing at least 0.12 times font size, and word spacing at least 0.16 times font size.
The criterion tests tolerance of those user settings without loss of content or functionality; it does not require authors to use them as their default.
See the official [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow) and [Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing) explanations.

## Adapt from the task and content

Let text and media set their own height.
Start with flexible widths and wrapping, then introduce a breakpoint where content fit, comparison, hierarchy, or operation requires a different arrangement.
Do not choose breakpoints only by device labels.
Collapse columns when their labels or data become unusable; keep semantic and reading order clear.
Prioritize or disclose secondary content only if the same essential fact and action remain reachable.
Do not remove data, evidence, qualifications, navigation, or an action just to make a narrow screenshot look clean.

Use fixed or sticky elements only when they remain useful and do not cover content, focus, or controls at zoom.
Keep help and important actions available without hover, drag, multi-touch, long press, or precision timing as the only path.
Viewport width does not reliably reveal input capability; check touch, pointer, and keyboard as applicable.
Choose target area and spacing for the use context.
WCAG 2.2 SC 2.5.8 AA sets 24 by 24 CSS pixels subject to exceptions, including spacing; 44 by 44 is a useful design choice or the separate SC 2.5.5 AAA criterion, not a universal AA rule.

Constrain images to their layout and preserve subject, credit, caption, and meaning.
Use `srcset` and `sizes` when alternate resolutions of the same image match the context; use art direction when a different crop materially improves the narrow composition.
Check the actually selected source when asset loading matters.
Keep charts and tables faithful at every layout.
Use a local labeled and keyboard-reachable scroll region or a complete alternate presentation for content that genuinely requires two dimensions.

## Example: report table and fixed index

A report's narrative columns collapse on a phone, but the comparison table makes the whole page scroll sideways and a sticky index covers the focused heading at high zoom.
Keep every table row, header, unit, note, and source.
Let the narrative use a single column once it no longer fits, constrain horizontal scrolling to the labeled table region, and move the index into normal flow or a compact disclosure at the constrained effective width.
Test the actual reflow criterion, spacing overrides, table access, keyboard focus, and zoom.
If only a screenshot is available, report the visible overflow and leave interaction and keyboard behavior unverified.

## Verify and report

Check complete content and actions at relevant wide, intermediate, narrow, and enlarged states.
Include long labels, long words, data tables, menus, dialogs, sticky elements, error messages, and focus where they affect the work.
Repeat each changed task using its relevant input method.
Check print only when print or export is an intended route.
Report viewport, zoom, state, input method, observed result, standards applied, and unavailable checks.
Do not call a resized screenshot a responsive or accessibility pass.
