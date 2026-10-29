# Interaction states, feedback, and recovery

Use this reference when an action changes visible or stored state, waits on asynchronous work, or can fail, be cancelled, repeated, or undone.
Use [forms and search](forms-search.md) for data entry and retrieval, and [keyboard and focus](keyboard.md) for input contracts.

## Model the path the artifact actually supports

For each important action, identify trigger, current state, pending state, success result, failure result, and available recovery.
Add empty, stale, disabled, cancelled, or undo states only when the product uses or needs them.
Do not add a state library or a workflow step solely to make a diagram complete.
Keep business rules, persistence boundaries, and permission scope unchanged unless the request authorizes a behavior change and the source supports it.

Make feedback local and proportional: a changed row can receive inline status; a long operation may need progress; a failed task needs a useful next action.
Use text or shape as well as color.
Name actions by their actual effect.
Distinguish a successful local simulation from a server-confirmed change.
Never claim persistence, undo, retry safety, deletion, or completion that the implementation does not provide.

For asynchronous work, ensure old responses cannot replace newer intent.
Use a request or generation identifier when overlapping operations can complete out of order, and accept a result only if it still belongs to the current request.
On refresh, distinguish first-load progress from refreshing while showing prior data.
If a refresh fails, keep the last known result when useful, mark it stale or previous, and offer retry only when retry exists.
Cancellation should invalidate future display of an old result; do not claim the remote service stopped unless it confirms cancellation.
Guard duplicate actions when repeated activation could cause duplicate effects.
Preserve input during recoverable errors.

## Exercise meaningful states safely

Test the normal path, relevant empty state, recoverable failure, retry or alternate route, repeated activation, and overlapping completion when applicable.
Check cancel, discard, undo, and duplicate prevention only when those affordances exist or the action's risk makes them necessary.
Use safe fixtures for hard-to-reach states and never make a real purchase, deletion, or irreversible change during a review.

### Example: stale search completion

Start query A, then query B; resolve B before A.
The displayed results must stay associated with B after A completes.
Repeat with A failing late, then fail B while prior results exist.
Keep the current query visible, distinguish prior results from fresh results, and keep retry tied to B.
Test an empty successful result separately from service failure.

## Report and preserve

For each finding, record location, state, exact steps, observed response, likely cause, task impact, remedy, confidence, and whether evidence came from source or runtime.
Before and after, compare supported actions, submitted values, stored or displayed data, permissions, labels, feedback, and state transitions.
Verify the same path after repair and include keyboard focus and status announcement where relevant.
If a state could not be exercised, report it as unknown rather than passing it by inspection.
