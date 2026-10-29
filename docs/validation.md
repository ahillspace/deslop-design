# Validation record

This record separates package correctness, author practice, and evidence that has not been collected.
The strengthened snapshot and author checks are dated 29 October 2026 (UTC).
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

The package check passed with 35 local links and both documented installation paths, including overwrite refusal.
Both skills passed the skill-creator `quick_validate.py` check during development.
`git diff --check` passed before the snapshot commit.
The checker initially detected that a README shell block used a fence style its parser did not recognize; the parser was updated to handle both supported fence styles and the real installation checks passed.

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
The design skill includes completion checks and does not require review to be installed or invoked.
The review skill has no required cross-skill references and works alone.

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

## Independent forward-use trial

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

## What remains unproven

Static checks do not show that another model will select references or follow instructions correctly.
Author inspection does not establish independent preference, professional equivalence, or improvements over existing skills.
The small fixtures do not cover a live backend, real booking, localization, large datasets, advanced controls, or production recovery.
Automated accessibility scanning and broader assistive-technology testing require separate evidence; keyboard and layout checks alone are insufficient.
Use the [benchmark plan](benchmark.md) before making comparative quality claims.
