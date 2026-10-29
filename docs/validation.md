# Validation record

This record separates package correctness, author practice, and evidence that has not been collected.
Checks below name the snapshot or fixture they cover because package work continued after earlier trials.
Four independent forward tasks were completed on snapshot `b577bf8`.
The report task exposed a quantitative chart-alignment defect, which led to shared mapping and rendered-coordinate guidance in `3a669ce`.
A fresh report task then exercised that exact updated snapshot from the raw prompt and fixtures without receiving the earlier output or defect diagnosis.
The outcomes and evidence limits are recorded below.
No independent human scores, blinded comparison, professional-equivalence result, or large paid benchmark is claimed.

## Repeatable package checks

Run from the repository root with Python 3.10+ and a POSIX shell:

```bash
python3 scripts/check_package.py
```

The checker resolves explicit local Markdown links and heading fragments in the package.
It executes both README installation snippets in temporary projects with spaces in their paths, checks complete copies including the package license, resolves installed references, and verifies that a second installation refuses without overwriting files.
It reports entry word counts without treating wording or exact headings as evidence of model behavior.
The pull request workflow runs this network-free check.
The local result below is separate from the delivery pipeline's CI result.

Earlier package checks passed with 35 local links and both documented installation paths, including overwrite refusal.
The checker initially detected that a README shell block used a fence style its parser did not recognize; the parser was updated to handle both supported fence styles and the real installation checks passed.
The current package check passed with 137 local links and both documented installation paths, including overwrite refusal.
Both current entrypoints passed the skill-creator `quick_validate.py` check.
`git diff --cached --check` passed on the candidate tree.

Codex CLI discovered both enabled skills from a temporary project's `.agents/skills` directory through its app-server `skills/list` interface.
This confirms discovery, not an autonomous skill invocation or automatic-selection outcome.
Claude Code's `.claude/skills` layout was checked against its official documentation and exercised by the install test; live discovery and invocation were not run.
Other Markdown-capable agents can read the entry file and relative references, but their automatic discovery has not been tested.

## Description and scope inspection

These are routing judgments, not measured automatic-selection accuracy.

| Request | Intended routing |
|---|---|
| Build a sourced sampling report from a CSV and methods note | Design; reports reference |
| Redesign a dispatch list within the existing product system | Design; tools reference |
| Explain threshold comparisons in a long illustrated page | Design; editorial reference |
| Build a ceramics-course page from confirmed terms | Design; landing reference and copy when needed |
| Review an existing page on mobile; do not edit | Review only |
| Repair the keyboard and overflow issues in this HTML tool | Review with bounded relevant repair |
| Correct the spelling of a station name | Ordinary narrow edit; skip design process |
| Optimize a database query with no UI change | Neither skill |

Review's description covers newly built artifacts so a substantive build can receive a final critique.
The design skill includes completion checks and does not require review to be invoked.
Both folders must be installed together because review uses the shared classification and routing reference in artifact-design.

## Earlier author-run practice trial

Four small HTML artifacts were built in isolated scratch space from explicit illustrative briefs, using the package's process and the relevant genre guidance.
The author both produced and reviewed them in the current working context; this was not an independent or blinded forward test.
There were no competing arms, fresh evaluator contexts, external images, or model-based scores.

| Fixture | Behavior exercised |
|---|---|
| Sampling report | A qualified finding, four-station table, missing reading, units, threshold comparison, methods, and explicit absence of trend or health inference |
| Dispatch tool | Inherited compact system, local site and status filtering, current result count, no matches, reset, missing owner, stale fixture notice, and no invented persistence |
| Explanation | A sustained reading column, arithmetic diagram and caption, ordered reasoning, section anchors, source footnote, and return path |
| Ceramics landing page | Hypothetical exact terms, no invented testimonials or imagery, native form validation, and explicit local-only enquiry feedback |

The earlier browser trial used Chromium 154 through an isolated Chrome DevTools session.
All four fixtures were checked at 1440, 768, 390, and 320 CSS pixels; no unintended page overflow was observed.
Eight full-page desktop and phone captures were visually inspected, including opening, middle, and ending content.
The tool fixture's large introduction delayed job rows on phones, so one repair batch reduced its heading and spacing and added overdue and unassigned counts derived from the visible rows.
The affected tool was recaptured at desktop and phone widths and rechecked at all four sizes.
This was a fixture correction, not a new universal rule in the skill.

Fifteen browser assertions passed for search, no-match, reset, visible keyboard focus, status filtering, active-scope summary, combined filters, article anchors and footnote return, landing action destination, email validation, keyboard form submission with truthful local-only feedback, and report-table keyboard focus.
Console inspection found no messages, and network inspection showed only successful local document loads.
No automated accessibility scanner or screen reader was used, and browser zoom was not tested.
No live backend or destructive operation was exercised.

## Strengthened author-run checks

The copy reference applies the heading test to the previously observed phrases “Give the work a reason” and “Check the real thing,” with the actual section subjects beside them.
It also contains two difficult illustrative passages based on an 18-ticket sample, 11 missing update dates, four possible duplicates, and an exact quote.
Their edits retain the writer's personal aside, correct an unverified duplicate claim, preserve the count and quote, identify interpretation as uncertain, and frame a proposed follow-up as untested.
This checks that the examples encode useful repair principles; it is not evidence that another agent applied the skill successfully.

The shipped CSS and JavaScript recipes were embedded in a temporary local repair-queue page and exercised in isolated Chromium.
At 1440, 768, 390, and 320 CSS pixels, the page had no horizontal overflow and its two-column content reflowed to one column on narrow screens.
Keyboard focus reached the urgent-only control, Enter changed its pressed state, and a polite status message reported the two matching records.
The normal-motion session revealed passive content after scrolling and restored its observer after a back-forward cache navigation.
In a separate session launched with Chromium's reduced-motion preference, the recipe skipped its motion-ready state, kept content visible, and left the keyboard filter working.
Sampled foreground and focus colors exceeded the relevant WCAG 2.2 contrast thresholds in this fixture.
These observations apply only to this prototype and do not constitute an accessibility audit.

A skill-only snapshot at commit `7637b40` was prepared for a fresh interactive build task and a report-revision task with source data.
Those briefs and fixtures contain no target copy, style preference, conclusion, or expected answer.

## Earlier independent forward-use trial

This trial evaluated the prior snapshot at commit `7637b40`, not the current compiler candidate.
It does not verify the expanded route, document references, or positive craft recipes described in this revision.

An independent evaluator used snapshot `7637b40` for both fresh tasks and completed them without discovery questions.
The build matched all eight supplied repair records, implemented search, priority and status filters, empty states, and a page-local ready action, and disclosed its assumed eligibility rule.
The revision kept the supplied type and color tokens and exact quote, corrected unsupported claims, and did not infer cause from the sample.

The evaluator inspected both rendered pages at 1440, 768, 390, and 320 CSS pixels.
The first build render exposed overflow from the reset badge, urgent cards that were too narrow at 768px, and lost focus when a filtered record disappeared; the evaluator fixed and retested each issue in the fixture output.
Keyboard filtering and focus recovery worked, local state reset after reload, sampled contrast ratios exceeded the applicable text thresholds, and the final console and network checks showed no errors or external requests.
This is evidence of bounded successful use on these two briefs, not an independent human preference study or a comparison with other skills.

The evaluator read all seven artifact-design references despite receiving single-surface tasks.
The design router was made more explicit after this trial, and the copy reference also changed after the snapshot.
Neither post-snapshot instruction change was evaluated by this run, so selective loading and the final copy reference remain unverified in forward use.
Neither output used animation, so this pass provides no motion evidence.
The separate author-run recipe check above exercises reduced motion and interaction but does not replace that missing forward-use evidence.

Actual browser zoom, screen-reader use, and physical-device behavior were not verified.
No repository test suite or comparative benchmark was run.
The earlier four-fixture trial and the separate motion check remain author-run evidence only.

## Original forward tasks at `b577bf8`

All four tasks used the same frozen skill snapshot and separate raw prompts and fixtures.
The original synthetic prompts and input files are preserved with their relative paths and hashes in the [forward fixture bundle](forward-fixtures/README.md).
The initial Chrome DevTools bridge launches failed for the product and narrative-report tasks; bounded operational retries with named isolated Chromium sessions later produced browser evidence.
Those startup failures and the subsequent retries are retained in the task evidence.
The evaluations found and documented real artifact defects, so they are not described as clean first-pass outputs.

### Interactive product audit

The audit-only review left the supplied HTML, CSV, and source note byte-identical.
Source reconciliation found 12 records, 8 `Open`, 4 `Waiting`, and 3 rows with missing documents, making the displayed “11 open” count unsupported by the supplied data.
Browser checks at 1440, 390, and 320 CSS pixels found 738px document width at both narrow sizes, with the first row action ending at x=703.55px at 320px.
Keyboard focus reached the first review button with no visible indicator, and pointer or keyboard activation changed only the local button label and disabled state while leaving row status and batch counts unchanged.
Search and status filtering, no-match, clearing, screenshots, and the local-only action state were exercised.
The audit separated four findings: unsupported batch count, page-wide narrow overflow, invisible button focus, and potentially misleading local-only action feedback.
No screen reader, real service, touch input, 200% zoom, forced-colors view, text-spacing override, or automated accessibility scan was tested.
The live result-count text changed in the browser; assistive-technology announcement behavior was not verified.

### Narrative report redesign

The first report output preserved the eight source records, units, date, method, missing-value treatment, screening qualification, and source attribution.
The source files contained no external URL, so the report retained the supplied attribution without inventing a destination.
The first browser pass had launch failures and later exposed cramped phone tick labels and collisions in narrow table cards; the evaluator adjusted the task artifact and checked the phone layout again.

A compiler review of the saved wide render identified that the 0, 2, 4, and 5 labels were equally spaced even though the 4.0 threshold line was at 80% of the 0-to-5 track.
The original task output and screenshot were preserved before the evaluator repaired only that output.
At 1440x1000, the track was 708.40625px wide, the 4 tick center was x=840.953125, and the threshold marker began at x=956.515875, a 115.56275px separation.
After repair, the 4 tick aligned with the marker within 0.00025px and the 2 tick was within 0.0032px of its 40% coordinate.
The evaluator reran CSV parity, keyboard filter and clear, phone rendering, and a tagged two-page Letter PDF export after the task-artifact repair.
The initial pass had not detected the quantitative geometry error; this specific gap motivated the guidance change and was checked again in the fresh task below.

### Printable A4 decision brief

The evaluator produced editable HTML and a tagged, two-page A4 PDF with the requested costs, status, sample counts, missing-data exclusion, limitations, exact quote, and all three supplied references.
The HTML was rendered at 1440, 390, and 320 CSS pixels; no page-wide overflow was observed, and keyboard Tab plus Enter reached the source notes.
The first PDF export included Chromium's default browser header and footer; the export was regenerated with those defaults removed and the final pages were visually inspected.
No screen reader, physical printer, 400% zoom, or reader study was used.
The supplied internal source files were not independently validated against their underlying records.

### Fixed-PDF audit

The findings-only review left the supplied one-page Letter PDF unchanged and did not claim that a screenshot supplied editable source or keyboard behavior.
Text extraction, structure and font inspection, `qpdf --check`, and actual color and grayscale renders supported an audit of the visible page.
The audit recorded four findings: an unverifiable 92% basis, a missing or mislabeled escalation visual, touching monthly bar labels, and no tagged structure.
The PDF was untagged and no underlying workbook or editable source was supplied, so the source truth, keyboard behavior, and accessibility for a particular reader could not be established.
No PDF conformance claim, screen-reader test, physical printer test, or user study was made.

## Fresh report task at `3a669ce`

The fresh evaluator received the raw report prompt, the original fixtures, and candidate snapshot `3a669ce05bea56a6b919777bc75d12975236fbff`.
It did not receive the prior report output, defect diagnosis, expected geometry, or source/author reports.
The machine ledger shows it read the updated `data.md` and `qa-parity.md` references at that snapshot.

The evaluator built a conclusion-led report with a common 0-to-5 mg/L plot, an exact-value table, a missing-value row, a station filter, and a Letter PDF export.
CSV reconciliation matched all eight station records, the classifications, and bar percentages; the report retained the seven-measured/one-missing denominator, method, date, screening-only qualification, and no-trend/no-health-effect limit.
Because the original files had no external source URL, it preserved the attribution and linked the supplied CSV instead.

The new shared-scale recipe was used to place the 0, 2, 4, and 5 ticks at 0%, 40%, 80%, and 100% of the actual plot bounds.
Browser geometry checked the same 80% threshold position at 1440, 390, and 320 CSS pixels, with plot widths of 770.8125px, 324px, and 265.21875px.
The threshold offsets measured 616.641px, 259.188px, and 212.172px respectively, and page scroll width matched the viewport at all three sizes.
Keyboard search returned one row for “East Weir,” an explicit zero-result state for “no station,” and all eight rows after clearing.
The tagged, three-page Letter PDF was regenerated, text-extracted, and visually inspected after the order correction.
The final first page still leaves substantial open space below the title and summary; page breaks keep the chart and table together on page 2 and interpretation, method, and source together on page 3.
This remains a print-density limitation, and no minimum-page optimization is claimed.

The initial integrity pass corrected the reference hashes but changed the report's order description to classification groups in source order without changing the artifact.
That description still contradicted the artifact's descending-order claim, which the screenshot review exposed.
After the first review, the retained 320px chart screenshot showed East Weir at 4.6 before Lower Mill at 4.7 even though the section promised descending measured-value order.
The follow-up correction moved Lower Mill before East Weir in both the chart and table, retained South Marsh last, and preserved all values, station associations, classifications, units, threshold, caveats, missingness, and filter logic.
The pre-correction screenshot remains in the evaluator evidence.
The evaluator refreshed wide and phone renders, rechecked chart/table parity and filter match, no-match, and clear states, then regenerated and inspected all three tagged Letter PDF pages.
The post-correction checks at 1440px and 320px retained viewport-width pages, the approximately 80% threshold position, and bar lengths proportional to value on the 0-to-5 scale.
The final chart and table both display Lower Mill, East Weir, Bay Outlet, West Reach, Harbor Gate, North Point, Upper Fork, then South Marsh.
This is a post-run artifact correction and focused verification, not a clean first-pass result or another independent task execution.

This is one fresh, task-specific forward execution of the changed references, not a user study, unaided control, general effectiveness claim, or professional-quality score.
Screen-reader announcements, contrast ratios, forced colors, text-spacing overrides, 200% or 400% zoom, Safari or Firefox, printed-link activation, and real-reader comprehension remain untested.
The 320px check is a measured viewport and overflow result, not a complete WCAG reflow conformance test.

## Reference-hash reconciliation

The machine-recorded reference digests for the four `b577bf8` tasks were checked against Git blobs at that commit: 15 product-audit files, 19 report files, 15 A4-document files, and 11 fixed-PDF-audit files all matched.
The verified `cognitive-accessibility.md` digest at that snapshot is `e1fd3a5d75296c38dad3a2e0fab7a137330e60298f520252a552b4b17f0b8f02`.
An earlier report-prose transcription concern was resolved against the candidate and machine records; the retired evaluator reports were left unchanged.

The v2 ledger records 20 candidate references and 18 retained artifact files, including the preserved pre-correction screenshot.
The first ledger had one manually transcribed reference-hash mismatch; the evaluator regenerated all 20 hashes from candidate snapshot `3a669ce05bea56a6b919777bc75d12975236fbff` and recorded the correction.
All 20 final reference hashes match their candidate files, all 18 artifact hashes match their files, and the report digest in `checks.json` matches the final `report.md`.
The evaluator refreshed the final HTML, print PDF, and changed screen captures after the order correction; those final hashes also match the machine record.

The evaluator-authored reports, machine records, screenshots, and generated redesigns are not part of the public fixture bundle.

## What remains unproven

Static checks do not show that another model will select references or follow instructions correctly.
Author inspection does not establish independent preference, professional equivalence, or improvements over existing skills.
The small fixtures do not cover a live backend, real booking, localization, large datasets, advanced controls, or production recovery.
Automated accessibility scanning and broader assistive-technology testing require separate evidence; keyboard and layout checks alone are insufficient.
Use the [benchmark plan](benchmark.md) before making comparative quality claims.
