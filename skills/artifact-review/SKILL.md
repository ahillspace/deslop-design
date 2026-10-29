---
name: artifact-review
description: Review existing or newly built HTML for visual hierarchy, useful copy, responsive behavior, and interaction using rendered evidence. Repair only when authorized and disclose source-only review when a browser is unavailable.
---

# Artifact review

Judge whether the artifact helps its intended reader understand or act.
This skill works independently on existing work.
A review request authorizes findings, not edits; a build or repair request permits relevant corrections within that scope.
Preserve strengths, required content, and behavior outside scope.

## Establish the review

Identify the target version, audience, requested task, important facts and actions, governing design system, and review budget.
Classify the surface by its job: persuade, operate, explain, or present the work itself.
A product may have a landing route and a working interface with different priorities.
Apply the existing brand and product system where one exists; do not invent missing rules.

## Gather evidence

Open the actual artifact in an isolated browser context.
Wait for fonts, images, and a representative state, then verify what loaded.
Capture the opening, middle, ending, and full working view at desktop and phone widths.
Check 1440, 768, 390, and 320 CSS pixels when applicable, plus zoom and long content.
Treat intentional table scrolling as usable only when its label, headers, and keyboard access work.

Walk the main task with keyboard and pointer.
Check names, reading and focus order, visible focus, focus return, and applicable hover, active, pending, disabled, loading, empty, error, and success states.
Use safe fixtures for unavailable states; do not trigger purchases or destructive actions just to test them.
Inspect DOM and computed styles, console errors, failed requests, and available accessibility findings.
Screenshots show composition, not behavior; DOM snapshots show structure, not visual quality.

When browser access or a state is unavailable, continue with permitted evidence and say exactly which checks remain unknown.
Do not describe a source inspection as rendered, interaction, or accessibility verification.

## Judge and prioritize

Look at the rendered artifact before consulting style detectors.
Check hierarchy, alignment, rhythm, density, typography, image crops, captions, responsive reflow, and whether the visual direction fits the material.
Judge contrast against the applicable accessibility target and keep meaning available without color alone.
Do not score taste, impose a favorite palette, or replace the governing system with a trend.

Judge the artifact by the reader's job:

- Reports: conclusions, comparisons, units, uncertainty, methods, and source trail.
- Tools: task, current state, status scope, next action, and recovery.
- Explanations: argument, figures, references, and wayfinding.
- Landing pages: offer, terms, credible proof, and actual next action.
- Showcases: the work itself, with controls that support rather than compete with it.

Trace claims to supplied evidence.
Flag fabricated proof, lost qualifications, misleading encodings, and copy that promises behavior the artifact lacks.
Treat awkward stock phrases and vague headings as editing clues, not evidence of who wrote them.
Distinguish observed defects from interpretation or preference.

For each actionable finding, record:

location / viewport and state / evidence / user consequence / severity / concrete repair / confidence

Use blocker for a failed essential task, fabricated or missing required evidence, or a material access barrier; major for substantial friction; minor for limited polish.
Rank by consequence, confidence, and repair scope.
Name strengths worth preserving and mark untested behavior unknown.

## Repair and close

In review-only mode, return ranked findings and limitations without changing files.
With repair authority, fix the highest-impact findings in a focused batch, then recapture the same views and retest affected behavior.
Do not broaden the redesign or rewrite supported facts to make the layout fit.
Repeat only while a round can meaningfully improve the result, up to three rounds or the agreed budget.

Completion requires the essential task and required content to work without a known material correctness, access, or layout blocker.
If time or access prevents that, report the unresolved condition and its consequence.
Report what you inspected, repaired, retested, and left uncertain.
A clean linter, screenshot match, self-rating, or attractive first viewport is not proof of overall quality.
