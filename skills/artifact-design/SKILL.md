---
name: artifact-design
description: Create or substantially redesign HTML reports, dashboards, explanations, and landing pages with coherent visual decisions, useful copy, and working interactions. Skip backend work and narrow factual or style corrections.
---

# Artifact design

Build a truthful artifact that helps its reader understand, decide, or act.
Once invoked for a design task, carry the work from inspection through implementation and rendered correction without asking the user to choose an aesthetic direction.
The user brief, existing product behavior, and established design system govern.

## Orient

Read the request, implementation, representative content or data, components, assets, and existing design decisions.
Identify the reader, the main task, the intended outcome, and which facts or behaviors are confirmed.
Separate facts, interpretation, illustrative material, and unknowns when the distinction affects a claim.
Never invent results, customers, quotes, prices, dates, availability, or capabilities.

Classify the requested surface by what its visitor is doing, not by the company or product name.
A landing page may persuade, a dashboard may operate, a guide may explain, and a portfolio may let the work speak.
A mixed product can use more than one of these jobs across its routes or sections.
On a persuasive brand surface, make the supported offer, proof, terms, and next action easy to see.
In a working product surface, foreground the task, current state, controls, and recovery; carry the brand through details that do not compete with that work.
Do not move campaign language into an operational screen or flatten a brand surface into generic utility copy.
Read the matching genre reference below and [implementation techniques](references/implementation.md).
Load [copy](references/copy.md) for substantive prose, labels, or claims.
Load [motion](references/motion.md) only when movement helps explain a change, direct attention, or give the subject useful character.

Use the brief and repository to settle routine design choices.
Make a reversible assumption and proceed when a detail is missing but does not change the task.
Ask one focused question only if missing information changes the requested outcome, authority to act, or whether the artifact would tell the truth.
Do not request a concept vote, palette selection, questionnaire, or approval at every step.

Make a short working outline before styling: what the reader needs first, the order that answers the request, the actual section names and representative content, the key visual device, and the states or actions that must work.
Keep ordinary working notes in context; do not create a design sidecar unless the project already uses one or the user asks for it.

Choose the applicable genre by the reader's task:

- [Reports](references/reports.md): evidence, comparisons, uncertainty, and methods.
- [Dashboards and internal tools](references/tools.md): repeated decisions, current state, and operational actions.
- [Editorial and explanations](references/editorial.md): sustained reading, arguments, figures, and navigation.
- [Landing pages](references/landing.md): a real offer, supporting proof, terms, and an informed next action.

## Build

Choose one visual direction that follows from the content, task, existing system, and available assets.
Tie type, composition, color roles, density, imagery, and interaction details together for a reason the artifact can show.
Use the techniques reference to make the layout adapt to content instead of defaulting to a fixed desktop grid.
A photograph, diagram, annotated chart, timeline, table, live sample, or typographic treatment earns space when it explains this subject.
Do not add one to satisfy a recipe.

Use semantic HTML, project components and tokens, and native controls before custom behavior.
Keep actual content and key actions present at narrow widths and zoom.
Implement every action that the artifact presents.
Label simulations plainly, preserve entered data after recoverable errors, and show only success that the code actually performs.
Do not introduce a framework or remote service for a simple HTML artifact.

Use movement selectively.
When it helps, implement one clear entrance, transition, or response that explains a relationship or user action.
The optional motion reference includes a working progressive enhancement, reduced-motion handling, focus behavior, and lifecycle notes.
Static work can be the right result.

## Inspect and finish

Open the rendered artifact after fonts, images, and data settle.
Inspect the whole page at desktop and phone widths, the longest content, keyboard order and visible focus, the main action, relevant empty or error states, and console or failed network requests.
Use the reference review sizes of 1440, 768, 390, and 320 CSS pixels unless the surface calls for different checks.
Check text wrapping, zoom and reduced motion where they affect the changed work.
For a source-only result, state that rendered and interaction checks are pending.

Fix defects you actually observe, then inspect the affected views and behavior again.
Stop after three focused repair rounds or the agreed budget, and report remaining blockers.
For a separate critique, [artifact-review](../artifact-review/SKILL.md) can be used independently.
Deliver the artifact, the actions and checks completed, and material limitations.
