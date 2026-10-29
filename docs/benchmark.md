# Proposed evaluation

This plan is for maintainers deciding whether the package improves outcomes enough to justify owning it.
No blinded benchmark, independent human scoring, or professional-equivalence study has run.
The author-run [smoke checks](validation.md) test practical paths and obvious failure modes only.

## Fair comparison

Compare the same capable model without a design skill, pinned unmodified Anthropic frontend-design, pinned unmodified Impeccable using its relevant workflow, and this package.
Use the pins in [provenance](provenance.md), freezing any later chosen versions before evaluation.
Consider full Taste Skill as a further tool/landing challenger only with a separate budget.
Give all arms identical briefs, facts, licensed assets or reference-search permissions, model snapshot/settings, harness, browser capabilities, network rules, and time/token/tool limits.
Include retrieval, images, retries, required setup, and failures in costs.
Use fresh contexts and isolated directories; randomize run order and repeat runs if seeds cannot be held constant.
If a missing fact materially changes the task, provide the same answer to each arm and count the interruption in its cost.
Do not add concept approvals or aesthetic steering to an arm that does not require them.

Start with one brief in each of four genres and two repetitions per arm: 32 builds.
A proposed confirmation uses three held-out briefs per genre and three repetitions per arm: 144 builds.
These are plans requiring a separate resource decision, not authorized spending.
Calibrate limits on practice briefs before freezing them; an initial candidate is 30 minutes, 60,000 total model tokens, 50 browser actions, and no image generation per build.
Do not tune on the held-out briefs.

Include a sourced report with uncertainty and a difficult table, an operations tool with filtering and recovery, a long explanation with figures/footnotes, and a landing page with exact terms and a working action.
Vary density, content length, established-system maturity, imagery availability, and relevant languages/glyphs.
Include both restrained and expressive briefs.

## Independent assessment

Hide process/skill names behind random identifiers and randomize pair order.
Present consistent desktop, phone, and full-page views plus an interactive task without flattening meaningful design differences.
Use 1440x900 and 390x844 for comparison and 320px for reflow checks under a fixed browser/font environment.
Recruit at least three independent reviewers with visual, content, and accessibility expertise, plus representative readers for task/comprehension checks.
Collect judgments independently before discussion and retain disagreement.

Judge purpose/hierarchy, composition/typography, genre fit, factual and useful copy, responsive/accessibility/state behavior, and readiness for the intended context.
Calibrate anchors such as obstructed, usable with friction, and ready for the intended task on separate examples.
Collect pairwise preference with an evidence-based reason rather than relying on a producing model's self-score.
Record fabrication, missing required evidence, broken essential actions, and material access barriers separately; attractive styling must not average away a task failure.
Report results by genre and viewport, cost distributions, budget exhaustion, and brief-clustered uncertainty rather than treating captures as independent samples.

Before confirmation, preregister the decision rule and sample-size rationale after calibration.
Require no disqualifying defects and evidence of an advantage over the strongest existing option at acceptable ownership cost.
If the comparison is inconclusive, prefer the simpler maintained option rather than declaring a win.
A professional-equivalence claim would additionally need consented matched professional controls, a predefined equivalence margin, and an adequately sized blinded study.
Failure to detect a difference in a small sample does not establish equivalence.
