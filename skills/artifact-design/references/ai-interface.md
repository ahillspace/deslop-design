# AI-dependent interface behavior

Use this reference only when an artifact presents model-generated output, confidence, source attribution, review or approval, automated actions, consent, refusal, correction, or handoff.
Do not add a generic AI trust panel to unrelated content.

## Trace each consequential claim and action

Identify what the model or automation produces, what data and tools it can use, what action it can take, and which decision remains with the person.
Check the displayed answer against available source data, implementation, and provenance.
Distinguish quoted source, retrieved evidence, inference, generated suggestion, action status, and unknown.
Mark confidence only when it reflects a defined evidence basis; confident tone, a numeric score, and polished prose are not proof.
Do not expose or request private chain-of-thought.

Map supported, ambiguous, missing-source, refusal, tool-failure, correction, and handoff paths that actually exist.
Check whether the person can inspect the evidence that matters, control a consequential action, correct a result, cancel when supported, and recover from failure.
Make the scope of access or change visible before consent.
Separate a proposed action from one the system has actually completed.
Use a human handoff only when it has a real destination and its limits are clear.

Do not invent citations, sources, confidence calibration, refusal policy, human review, privacy guarantees, capability, or user trust outcomes.
Do not add a universal disclosure or disclaimer layer without a specific product need or policy.
Protect privacy: avoid collecting or displaying information unrelated to the task, and do not propose blanket storage or logging without a valid basis.

### Example: access change

If an assistant says “No contractor can see this log” because it found no contractor entry in one access guide, that conclusion is unsupported; absence in one source does not prove the permission state.
Say that the connected guide contains no contractor rule and that current access cannot be confirmed, linking the source when available.
Before changing permissions, show the affected log, current roles, proposed change, and who gains or loses access.
Only report success after the system confirms it; provide undo only if it exists.
If source or implementation cannot confirm the flow, label it unavailable rather than inventing a control.

## Verify and report

Exercise one supported path and each relevant missing-source, ambiguity, refusal, tool failure, correction, and handoff path with safe fixtures.
Check consent timing, action scope, cancel/retry/duplicate behavior, provenance access, keyboard path, status changes, and narrow layouts where applicable.
Report source inspected, observed, tested, inferred, and unavailable evidence separately.
Do not claim calibrated model performance, real-user validation, or complete accessibility from a visual check.
