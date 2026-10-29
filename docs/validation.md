# Validation record

This record distinguishes package correctness, author practice, and evidence that has not been collected.
Initial release checks are dated 29 October 2026 (UTC).
No independent human scores, blinded comparison, professional-equivalence result, or large paid benchmark is claimed.

## Repeatable package checks

Run from the repository root with Python 3.10+ and a POSIX shell:

```bash
python3 scripts/check_package.py
```

The checker resolves every explicit local Markdown link and local heading fragment in the package.
It executes both README installation snippets in temporary projects with spaces in their paths, checks complete copies including the package license, resolves installed references, and verifies that a second installation refuses without overwriting files.
It reports entry word counts without treating wording or exact headings as evidence of model behavior.
CI runs this same network-free check on pull requests and the default branch.
It does not score taste or run a model.
Development probes confirmed that missing files, missing anchors, and links escaping the package fail the checker; a valid fixture link passes.

The package check passed for 31 explicit local links and both documented installation paths, including overwrite refusal.
Codex CLI 0.163.0 discovered both enabled skills from a temporary project's `.agents/skills` directory through its app-server `skills/list` interface.
This confirms discovery, not an autonomous skill invocation or automatic-selection outcome.
Claude Code's `.claude/skills` copy layout was checked against official documentation and exercised by the install test; live discovery and invocation were not run.
Invocation syntax in the README follows the linked official harness documentation.
The author practice below applies the instructions directly in the current working context rather than claiming fresh-session harness execution.

Both skills passed the skill-creator `quick_validate.py` check during development.
That external development tool checks frontmatter, names, and scaffold validity; it is not a runtime dependency and does not establish design quality.
The package checker initially detected a README link to this not-yet-written validation record; the missing document was added without weakening link checks.

## Description and scope inspection

The author checked the descriptions against the following realistic requests.
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
The design skill also includes completion checks and does not require review to be installed or invoked.
The review skill has no required cross-skill references and works alone.

## Author-run practice trial

Four small HTML artifacts were built in isolated scratch space from explicit illustrative briefs, using the package's process and the relevant genre guidance.
The author both produced and reviewed them in the current working context; this was not an independent or blinded forward test.
There were no competing arms, fresh evaluator contexts, external images, or model-based scores.

| Fixture | Behavior exercised |
|---|---|
| Sampling report | A qualified finding, four-station table, missing reading, units, threshold comparison, methods, and explicit absence of trend/health inference |
| Dispatch tool | Inherited compact system, local site/status filtering, current result count, no matches, reset, missing owner, stale fixture notice, and no invented persistence |
| Explanation | A sustained reading column, arithmetic diagram/caption, ordered reasoning, section anchors, source footnote and return path |
| Ceramics landing page | Hypothetical exact terms, no invented testimonials or imagery, native form validation, and explicit local-only enquiry feedback |

The browser trial used Chromium 154 through an existing Chrome DevTools CLI in a dedicated isolated session.
All four fixtures were checked at 1440, 768, 390, and 320 CSS px; no unintended page overflow was observed.
Eight full-page captures at desktop and phone widths were visually inspected, including opening, middle, and ending content.
System fonts settled and no external media were used.
Console inspection found no messages; network inspection showed only successful local document loads.

The tool fixture's large introduction delayed job rows on phones.
One repair batch reduced its heading and spacing and added overdue/unassigned counts derived from the currently visible rows.
The affected tool was recaptured at desktop/mobile and rechecked at all four widths.
This was a fixture correction, not a new universal rule in the skill.

Fifteen browser assertions passed: tool search/no-match/reset, visible keyboard focus, keyboard status filtering and active-scope summary, combined filters, article anchors and footnote return, landing action destination, empty/invalid email rejection, keyboard form submission with truthful local-only feedback, and report table keyboard focus.
No automated accessibility scanner or screen reader was run, and browser zoom was not tested.
No live backend or destructive operation was exercised.
These checks establish the listed fixture behavior only, not general aesthetic effectiveness.

Raw briefs, HTML, captures, and logs were kept outside the distributable package; the package includes this bounded result summary instead of operational records.

## What remains unproven

Static checks do not show that another model will select references or follow instructions correctly.
Author inspection does not establish independent preference, professional equivalence, or improvements over existing skills.
The small fixtures do not cover a live backend, real booking, localization, large datasets, advanced controls, or production recovery.
Automated accessibility scanning and broader assistive-technology testing require separate evidence; keyboard and layout checks alone are insufficient.
Use the [benchmark plan](benchmark.md) before making comparative quality claims.
