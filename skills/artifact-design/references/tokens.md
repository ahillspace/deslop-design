# Token and design-system drift

Use this reference when a change touches shared tokens, components, themes, or repeated visual patterns.
For a local one-off correction, use [visual craft](visual-craft.md) and leave the system unchanged unless the evidence shows shared drift.

## Establish what governs the artifact

Inspect current documentation, token definitions, component contracts, relevant implementation, and repeated current surfaces.
Record the artifact revision, files or system sources checked, properties and states in scope, and any conflicting or missing authority.
Classify evidence as observed, documented system rule, inference, or unknown.
An inferred role is not approved policy.
A lone divergence from a token is not automatically a defect; it may serve a different state or surface.

## Map roles before values

For each repeated use, record its semantic role, component or context, current token/value, intended rule if known, theme/state, and visible effect.
Look first for a role mismatch: an error may use body-text color; a selected item may share the default surface; a focus state may be missing; a text token may be applied to a gradient.
Then trace values to actual computed output where available.
Do not assume a token name proves the rendered color, typeface, spacing, or state.

When a role is inferred rather than documented, label the proposal and its evidence.
Consolidate only repeated patterns whose meaning and behavior should match.
Keep a justified exception local.
Do not add a token framework, component, naming scheme, global mode, or full tonal scale to normalize a handful of unrelated values.

## Make a scoped system correction

Fix the shared source when multiple relevant components use the same incorrect role or value.
Fix a consuming component when it uses the right system incorrectly.
Create a new role only when a recurring meaning lacks a truthful existing role and the system can own it.
Name the intended uses and non-uses of any proposed role.
Check connected components, variants, themes, and states before changing a shared value.
Record meaningful exceptions rather than flattening different reader tasks.

### Example: one wrong status role

If three related product screens use the documented warning token for “At risk,” while a new report uses the success token, first verify the report's meaning and rendered state.
If the report shares the same semantics, correct its role use and preserve any distinct report hierarchy through structure rather than changing the shared warning palette.
If its status has a different documented meaning, keep the exception and explain the difference.
Then inspect all affected screens and theme states.
This is an illustrative decision, not a universal token recipe.

## Close with evidence

For an audit, report the system source, repeated pattern, mismatch, impact, remedy, and confidence without changing files.
For a repair, compare source values and actual output, inspect affected component variants and themes, and run only the checks appropriate to the change.
Automated token lint can find raw values but cannot determine semantic correctness.
Report unknown runtime values and do not claim system conformance from a partial sample.
