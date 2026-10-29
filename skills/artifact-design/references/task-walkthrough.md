# Evidence-based task walkthrough

Use this reference for an expert review of whether an artifact supports a real task, especially when its controls, content, or recovery path need to be exercised.
It is an inspection method, not a substitute for user research or usability testing.

## Define the task before opening the route

Record artifact version and route, reader job, task outcome, scope, protected content and behavior, governing system, available evidence, and inspection limits.
For mixed products, define each materially different task separately.
Write neutral scenarios in reader language without naming the control or prescribing a route.
Define an observable completion condition before the walkthrough, such as reaching the correct state or finding a supported answer.
Include a normal path and a consequential alternative or recovery path only when the artifact supports it.

## Walk and record the path

Start at a realistic entry point and trace choices, actions, system work, results, exits, and recovery.
First examine the task as an unfamiliar reader; check repeat or expert use only when it presents a materially different route or shortcut.
Record each step's location, viewport and state, action or transition, observed result, and evidence type: rendered, interaction, source/DOM, supplied data, or inference.
For asynchronous work, mark waits and test stale or overlapping results when relevant.
Use safe fixtures for unavailable states and never trigger a real purchase or destructive action just to explore.

Apply only relevant prompts: task completion, accuracy, relevance, clarity, visible state, language-to-control mapping, user control, error prevention, recognition, recovery, consistency with the actual product, and help at the point of need.
Heuristics are prompts, not a required quota.
A criterion without evidence is unassessed, not a pass.
Record positive evidence and strengths as well as failures.

### Example: duplicate-looking records

For the neutral task “Remove the duplicate imported record while keeping the other record,” establish that completion means the intended record is removed and the retained record and count are correct.
Walk the row actions, inspect distinguishing details, then check the actual remove result and any recovery path using a safe fixture.
If the control only says “Remove” and two rows look alike, report the visible ambiguity and the consequence as a likely risk; do not claim that real readers made the error.
Recommend naming the affected record in context and an undo or confirmation only when the product supports it.

## Write a causal finding without fake precision

Use `location / state / observed behavior / likely cause or violated task criterion / task consequence / targeted repair / severity / confidence`.
Separate direct observation from an inferred effect.
Severity reflects the task: blocker when essential completion fails, required evidence is materially false or absent, or a material access barrier prevents the task; major when substantial friction threatens completion; minor for limited disruption or polish.
Explain the reason for the priority.
Confidence describes evidence strength, not impact.

Do not invent total quality scores, prevalence, time-on-task, error rates, conversion, inter-rater agreement, or release thresholds from an expert walkthrough.
Use numeric measures only when supplied by actual evidence and explain its sample and method.
Do not call a walkthrough user-validated.

## Repair and close

Audit-only tasks end with findings and limits.
For authorized changes, preserve facts, qualifications, citations, links, required content, product behavior, and meaningful choices; then repeat the same scenario and affected recovery path.
Inspect the relevant rendered views, responsive states, document sequence, keyboard/focus, and data as applicable.
Report what was inspected, changed, retested, and left unknown.
