# Forms and search

Use this reference when an artifact collects or validates information, or searches, filters, and returns results.
Apply only the relevant parts to a mixed interface.
Do not use it to change backend rules, ranking, privacy, retention, required fields, or submission outcomes without evidence and authority.

## Map the task and its states

Identify whether the surface collects input, retrieves information, or both.
Trace a form through initial, partial, invalid, pending, server-rejected, recoverable, submitted, and saved/resumed states only where supported.
Trace search through empty, query entry, suggestions if present, loading, results, filtered, no results, failure, and cleared query states.
Use safe fixtures when possible; name a state that cannot be reached.

Inspect the field definitions, existing product language, source behavior, nearby flows, data constraints, and privacy notices.
Keep observations, likely user effects, and unverified business rules distinct.
Do not assume fewer fields or default values improve completion.

## Review and redesign forms

Give each control a persistent visible label and verify its programmatic name when source or DOM is available.
A placeholder can show an example but should not be the only label.
Place format, privacy, or choice instructions where they help before entry and associate help/errors with the relevant field when the medium supports it.
Group related fields around the real task; choose sequence from dependencies and preserve a clear reading and focus order.
Use native controls and input types when they accept the legitimate input and fit the platform.

Check every requiredness rule, allowed value, length, format, default, and conditional field against its source.
Do not loosen established validation or silently coerce, truncate, or overwrite meaningful input.
Use defaults only when known, safe, reversible, and unlikely to misstate intent.
For consequential choices, make the effect plain and require a deliberate selection when the source or policy calls for it.

Make errors identify the problem and a supported correction.
Keep entered data through recoverable errors.
For multiple issues, consider a linked summary plus field-level messages; move or announce focus only when it helps recovery and verify the actual behavior.
Separate invalid input from server or network failure, preserve values, and guard repeat submission when duplicates matter.
For a multi-step flow, test back navigation, review, save/resume, cancel, and discard only when implemented or required by the task.

## Review and redesign search

Make searchable scope clear and keep the query visible with its results.
Use the simplest interaction that supports retrieval; autocomplete and a particular suggestion count are optional patterns, not standards.
When suggestions exist, check their relevance, dismissal, keyboard operation, input association, and whether they steal focus or submit unexpectedly.
Make active filters and sort state visible, removable, and consistent with the displayed count and results.
Keep ranking and result semantics unchanged unless the request authorizes it.

Distinguish no matches from timeout, permission denial, and unavailable service.
For no results, keep the query and offer only real next steps such as editing a term, removing a filter, browsing an existing collection, or retrying a failed service.
Do not silently replace the query or infer a system defect from one empty response.
Do not recommend blanket query logging or personalization; search terms can be sensitive and require a valid privacy basis.

## Example and verification

If a form shows “Invalid form” after submit and clears the location field, preserve the entered value, point to the missing required field in text, associate its error, and show a linked summary when several errors make the path hard to find.
If search returns no matches for a query, keep that query visible and suggest removing a real filter only when the filter exists.
Use this as a repair shape, not as literal product copy without checking actual rules.

After an authorized change, test a valid path, invalid submission and recovery, relevant empty result, clear/refine, failure and retry, and a stale response where asynchronous requests can overlap.
Check names, focus order, status feedback, retained values, narrow layout, zoom, and actual persistence boundary.
For static printable forms, check field space, instructions, grouping, page breaks, and handwriting or completion needs; do not claim interactive behavior.
Use exact WCAG criteria only when the requirement matches the observed issue.
