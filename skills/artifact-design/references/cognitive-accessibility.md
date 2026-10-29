# Cognitive access and task continuity

Use this reference when a task asks readers to remember information across steps, understand nested choices, recover from interruption, or navigate a dense artifact.
It is a design lens, not a diagnosis of a person or a score of an interface.

## Distinguish task complexity from avoidable friction

Read the real task, fields, content, and decision rules.
Some work is inherently complex; redesign should not hide that complexity or shift it into a reader's memory.
Look for avoidable recall, unclear progress, unstable context, competing attention, hard-to-reverse choices, and help that appears only after an error.
Treat any numeric cognitive-load model as a heuristic for discussion, never as a release gate or user measurement.

Do not claim confusion, disability, or performance outcomes without user evidence.
Use a task walkthrough to describe what the artifact presents and where a reader must infer, remember, or reconstruct information.
If user research exists, identify its source, scope, and date.

## Make the task easier to follow

Keep the current goal, relevant prior answer, progress, and next action visible where they help a task continue.
Carry known information forward instead of making a reader repeat it.
Use stable labels and location cues.
Show dependencies and meaningful choice boundaries; distinguish a required decision from an optional one.
Place instructions beside the field, unfamiliar term, or action they explain.
Make search and wayfinding follow a reader's language and entry point where evidence supports it.

Reduce interference without hiding meaning.
Group related controls and information; remove repeated setup only when it carries no separate meaning; focus attention with hierarchy rather than concealing necessary evidence.
Offer progressive disclosure when it reduces distraction and preserves the relevant basis, current state, and route back.
Do not add an alternate “simple” view that changes facts, omissions, or actions without making the difference clear.

Support safe choice and return.
Use known defaults only when safe and reversible.
Keep entered work through recoverable errors and back/forward navigation where supported.
For costly actions, make scope and consequence clear before commitment and provide confirmation or undo when the actual risk and product behavior justify it.
Do not require a confirmation step for every action.
Design interruption and return behavior around privacy, session lifetime, and actual persistence; never claim autosave until it succeeds.

### Example: a comparison form

If a multi-step comparison asks a reader to re-enter location after navigating back, the repeated request is directly observable but user burden is an inferred effect.
Carry the value across steps if the application already supports that state, display progress and the current subject, and say clearly if the value is not saved between sessions.
Retest back/forward, correction, and recoverable failure.
Do not promise saved progress without verifying persistence.

## Review output

Record the specific step, visible evidence, information the task requires the reader to hold or infer, likely effect, targeted repair, and confidence.
Keep inference separate from observed behavior.
Preserve required detail, exceptions, labels, and working paths.
After authorized changes, repeat the same task and interruption/recovery path.
Report source inspection, rendered walkthrough, user research, and untested behavior separately.
