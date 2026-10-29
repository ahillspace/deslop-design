---
name: artifact-review
description: Review existing or newly built HTML artifacts for visual hierarchy, useful copy, responsive behavior, and interaction using rendered evidence. Repair only when authorized; disclose source-only review when browser access is unavailable.
---

# Artifact review

Assess whether the actual artifact helps its intended reader understand or act.
This skill works independently on existing work.
Establish the target/version, audience, genre, required facts and actions, governing design system, and review budget.
User/project requirements and the established system outrank this advice.
Preserve strengths and out-of-scope behavior.
A request for review authorizes findings, not edits; a build or repair request permits relevant corrections within that scope.

## Obtain evidence

Open the real artifact using existing browser tooling in a dedicated context suited to the material.
Wait for fonts, images, and a representative stable state; verify what actually loaded.
Record version, viewport, state, and capture locations.
Inspect desktop and phone screenshots, including the opening, middle, ending, and full composition or working screen.
Check 1440, 768, 390, and 320 CSS px when applicable, plus zoom and long content.
Distinguish intentional usable table scrolling from page overflow.

Walk the main task with keyboard and pointer.
Check accessible names, reading/focus order, visible focus, overlay focus return, and applicable hover, active, pending, disabled, loading, empty, error, and success states.
Use safe fixtures for unavailable states; do not trigger real purchases or destructive actions merely to test them.
Inspect DOM/computed styles, console, failed requests, and available automated accessibility checks.
Investigate serious findings and record manual checks separately.
Screenshots cannot establish behavior; DOM snapshots cannot establish composition.

When browser access or a state is unavailable, continue with permitted evidence and explicitly limit the conclusion.
A source-only review must not claim rendered, interaction, or accessibility verification.
Identify the missing check and what would resolve it.

## Judge and prioritize

Look at the rendered work before consulting style detectors.
Judge hierarchy, reading comfort, alignment, rhythm, density, typography, image crops, captions, and whether expressive choices suit the material.
Do not score taste, enforce a favorite palette, or replace the governing system with a trend.

Judge genre by the reader's success:

- Reports: answer, comparisons, units, uncertainty, methods, and source trail remain connected.
- Tools: current scope, urgent work, next actions, data meaning, and recovery are clear.
- Explanations: argument, figures, references, and navigation support sustained understanding.
- Landing pages: the offer, terms, credible proof, and actual next action are clear.

Audit content truth separately from appearance.
Trace claims to supplied evidence; flag fabricated proof, lost qualifications, misleading chart encodings, and copy that promises behavior the artifact lacks.
Distinguish a verified defect from an inference or preference.

For each actionable finding record:

`location / viewport and state / evidence / user consequence / severity / concrete repair / confidence`

Use blocker for failed essential tasks, fabricated or missing required evidence, or material access barriers; major for substantial friction; minor for limited polish.
Rank by consequence, then confidence and repair scope.
Include strengths worth preserving and mark untested behavior unknown.

## Repair and close

In review-only mode, return ranked findings and limitations without changing files.
With repair authority, fix up to three highest-impact issues as one batch, then recapture the same views and retest affected behavior.
Do not broaden the redesign or rewrite supported facts to improve visual fit.
Repeat for at most three rounds, the agreed budget, or until two rounds bring no meaningful improvement.
Preserve the best verified result.

Completion requires the essential task and required content to work with no known material correctness, accessibility, or layout blocker.
If budget or access prevents that, report the unresolved condition and its consequence explicitly.
Report what was inspected, repaired, retested, and left uncertain, with evidence locations.
A clean linter, screenshot match, self-rating, or attractive first viewport is insufficient proof of quality or professional authorship.
