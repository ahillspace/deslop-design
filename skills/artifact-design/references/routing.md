# Classify and route an artifact task

Read this reference first after invoking either artifact skill.
Classify the artifact and each materially different route or section before selecting any other reference.
Read every selected reference in full, then use its procedure.

## Classify four things

Record a compact working brief from the request, files, source material, project instructions, and available rendered output.

| Field | Classify | Evidence and limits |
|---|---|---|
| Medium | Browser HTML; interactive prototype; long-form source document; PDF or other fixed-page export; slide deck; screenshot or image; or a combination. | Source files show declared structure; a render shows only the produced view; a screenshot cannot establish editable source, interaction, semantics, or keyboard behavior. |
| Reader purpose | Persuade or choose; operate or monitor; explain or read; present or record; or a combination by route or section. | Infer from the reader's task and artifact, not the organization or product name. Mark an inference when it changes a decision. |
| Requested operation | Audit/review/critique; targeted repair; deslop/edit; redesign/rewrite/build; or a mixed request with separate authority per part. | Review alone is findings-only. A request to redesign or rewrite authorizes that scope, not unrelated changes. Preserve current behavior when the brief does not grant a behavior change. |
| Conditional features | Claims or data; substantial prose or argument; navigation or information architecture; form/search; asynchronous or consequential actions; custom controls; motion; AI output; established brand/tokens; responsive behavior; preferences; print/export; or meaningful media. | Select a specialist reference only when its feature exists or is in scope. Do not infer a feature from the filename or hypothetical implementation. |

For mixed artifacts, write one route line per materially different surface: medium, purpose, task, operation, and important constraints.
Keep shared facts and behavior consistent across routes.
Do not make a report embedded in a product inherit the product's operational priorities, or make a working form inherit a report's reading order.

## Reference routes

Load the common audit and redesign references for broad work, then add the specialist routes that the artifact needs.
When a user asks for a thorough audit or substantial redesign, inspect all listed dimensions applicable to the artifact even if the request names only one visible defect.

| Reference | Load when |
|---|---|
| [intake and structure](intake-structure.md) | Purpose, audience, authority, evidence, grouping, argument, navigation, or protected content needs reconstruction. |
| [visual craft](visual-craft.md) | Any visual audit or redesign; use it for hierarchy, composition, type, color, density, affordance, and brand intent as one system. |
| [accessibility](accessibility.md) | Any thorough HTML/interface audit, access request, or material access concern. For a document, use the format-specific parts and applicable document guidance. |
| [reading semantics](semantics-content.md) | Headings, source order, links, alternatives, captions, table structure, transcripts, or conversion between formats affect meaning or access. |
| [responsive behavior](responsive.md) | HTML or other screen content must work across widths, zoom, text expansion, orientation, or input contexts. |
| [documents](documents.md) | Long-form, evidence-led, printable, exported, or slide content; or any document whose argument, captions, reading order, or pagination is in scope. |
| [data displays](data.md) | A chart, table, metric, comparison, or data-dependent claim affects understanding or action. |
| [interaction states](interaction-states.md) | Controls, loading, persistence, asynchronous work, feedback, failures, cancellation, retries, undo, or state changes are present. |
| [forms and search](forms-search.md) | The artifact collects input, validates it, searches, filters, or returns query results. |
| [keyboard and focus](keyboard.md) | Interactive controls, composite widgets, focus order, drag/gesture alternatives, or keyboard access are in scope. |
| [cognitive access](cognitive-accessibility.md) | A task has meaningful memory, sequencing, wayfinding, choice, interruption, or recovery demands. |
| [user preferences](preferences.md) | Reduced motion, forced colors, text spacing, contrast preference, or other user setting affects the artifact. |
| [motion](motion.md) | Motion exists, is requested, or could clarify a transition or give subject-specific character. Static output is valid. |
| [tokens and systems](tokens.md) | Shared component, design-token, theme, or repeated visual-system drift is in scope. |
| [AI interfaces](ai-interface.md) | The artifact presents model-generated output, confidence, sources, review, consent, automated action, or handoff. |
| [concept exploration](concepts.md) | A redesign has multiple materially different ways to organize the task, argument, or interaction. Do not load for audit-only or an obvious narrow correction. |
| [task walkthrough](task-walkthrough.md) | A review or redesign needs a neutral expert walkthrough of a supported task and its consequential alternate or recovery path. |
| Existing genre references | Read [reports](reports.md), [tools](tools.md), [editorial](editorial.md), or [landing pages](landing.md) for the reader's main job; combine routes for mixed jobs. |
| Existing [copy](copy.md) | Substantive copy, labels, headings, or claims will be reviewed or changed. |
| Existing [implementation techniques](implementation.md) | A new or substantially changed HTML layout is being built. |
| Existing [QA parity](qa-parity.md) | Any authorized change must preserve facts, links, controls, or behavior, or a redesign needs before/after evidence. |

An interactive product with an embedded data report may need the product genre, documents, data, interaction, keyboard, accessibility, semantics, responsive, visual-craft, task-walkthrough, and parity routes together.
A print-only source file does not need web responsive checks; an HTML report with an intended print export needs both its screen and print routes.
A screenshot-only review can assess visible composition and displayed text, but must mark source behavior, keyboard, semantics, and editability unknown.

## Required coverage record

Before acting, keep a compact record in working context and include it in the delivery note for broad work.
List medium, purpose, operation, conditional features, references read, and material checks unavailable.
Mark a route **not applicable** only with a brief reason; mark an applicable but inaccessible check **unverified** with its consequence.
Never imply a reference was used because it was linked or named.

For audit findings, keep **visual craft** separate from **usability, accessibility, factual integrity, and behavior**.
Each actionable finding names location and state, observed evidence, cause or uncertainty, reader impact, specific remedy, verification performed or needed, severity, and confidence.
Do not let a style preference absorb or hide a correctness or access issue.

Example:

> Route: HTML narrative report with an interactive comparison table; explain/decide; audit-only. Features: sourced claims, table, responsive reading, keyboard-operable table region. Read: intake/structure, reports, documents, data, visual craft, accessibility, responsive, keyboard, QA parity. Print not requested; screen-reader output unavailable; no edits made.

If later evidence changes the medium, purpose, operation, or feature set, update the route and read any newly applicable reference before proceeding.
