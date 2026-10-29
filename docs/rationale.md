# Architecture and reference coverage

The package keeps the existing `artifact-design` and `artifact-review` invocation names.
Both entrypoints begin with the shared [routing reference](../skills/artifact-design/references/routing.md), which classifies medium, reader purpose, requested operation, and conditional features for each distinct route or section.
The router then requires the agent to read every applicable reference in full, use its procedure, and record coverage and unavailable evidence.

## Why the architecture has two entrypoints

Design and review have different authorization boundaries.
Design carries authorized work through implementation and rendered correction; review is findings-only unless the request grants repair authority.
Keeping the entrypoints separate preserves existing invocation compatibility and prevents review from silently becoming a rewrite.
The folders are installed together because review shares the design package's classifier and references.

The substantive methods live in focused references rather than a long skill preamble.
The router requires broad applicable coverage for thorough audits and substantial redesigns, while narrow tasks select only the relevant methods.
Mixed products combine routes at the page or section that needs them.

## Reference ownership

| Concern | Maintained reference | Distilled capability |
|---|---|---|
| Medium, purpose, operation, feature classification | [routing](../skills/artifact-design/references/routing.md) | Separate HTML, documents, fixed-page inputs, mixed routes, reader jobs, audit-only and authorized changes; list required reads and limits. |
| Purpose, evidence, authority, information architecture | [intake and structure](../skills/artifact-design/references/intake-structure.md) | Evidence order; inference boundaries; content inventory; task paths; document argument; smallest justified structural change. |
| Visual audit and redesign | [visual craft](../skills/artifact-design/references/visual-craft.md) | Hierarchy, composition, grids, rhythm, type, color, density, affordance, and brand as related decisions grounded in task and evidence. |
| Narrative reports and operational interfaces | [reports](../skills/artifact-design/references/reports.md), [tools](../skills/artifact-design/references/tools.md) | Preserve evidence and interpretation for reports; keep operational task, current state, action, and recovery discoverable in tools. |
| Sustained reading and persuasion | [editorial](../skills/artifact-design/references/editorial.md), [landing](../skills/artifact-design/references/landing.md) | Preserve reading sequence, figures, and source trail; present only supported offer, terms, proof, and working action. |
| Long-form and printable documents | [documents](../skills/artifact-design/references/documents.md) | Argument structure, claim ledger, evidence placement, captions, semantic order, pagination, margins, footnotes, and export limits. |
| Data displays | [data](../skills/artifact-design/references/data.md) | Trace source values and transformations; choose faithful encoding; preserve denominator, units, missingness, and exact values. |
| Accessibility and responsive behavior | [accessibility](../skills/artifact-design/references/accessibility.md), [responsive](../skills/artifact-design/references/responsive.md), [keyboard](../skills/artifact-design/references/keyboard.md) | Bounded evidence, exact standards, reflow, user spacing, native input, focus, and pattern-specific widget contracts. |
| Content semantics | [semantics](../skills/artifact-design/references/semantics-content.md) | Headings, links, image alternatives, table relationships, media equivalents, and reading order. |
| Interaction and cognition | [interaction states](../skills/artifact-design/references/interaction-states.md), [forms and search](../skills/artifact-design/references/forms-search.md), [cognitive access](../skills/artifact-design/references/cognitive-accessibility.md) | Truthful state transitions, overlap-safe asynchronous work, form/search recovery, task continuity, and interruption handling. |
| User settings and movement | [preferences](../skills/artifact-design/references/preferences.md), [motion](../skills/artifact-design/references/motion.md) | Reduced motion, forced colors and text overrides; purposeful, interruptible motion with working static fallback. |
| Systems, AI, and alternatives | [tokens](../skills/artifact-design/references/tokens.md), [AI interfaces](../skills/artifact-design/references/ai-interface.md), [concepts](../skills/artifact-design/references/concepts.md) | Repair repeated drift by semantic role; apply trust and control only to AI surfaces; compare materially different lightweight concepts when the choice matters. |
| Copy and completion | [copy](../skills/artifact-design/references/copy.md), [QA parity](../skills/artifact-design/references/qa-parity.md) | Preserve voice and claim meaning; compare protected content and behavior before and after using evidence matched to the claim. |
| Task evaluation | [task walkthrough](../skills/artifact-design/references/task-walkthrough.md) | Neutral task scenarios, observed paths, qualitative priority, confidence, and explicit unassessed criteria. |

## Required behavior by task

For any visual audit or redesign, inspect the whole relevant artifact and distinguish what is visible from likely effect.
For a thorough screen audit, route to visual craft, accessibility, content semantics, responsive behavior, and a task walkthrough, then add content, data, forms, keyboard, motion, preferences, AI, and system references where their features occur.
For narrative HTML with data, combine report and document structure, data, visual craft, accessibility, semantics, responsive behavior, task walkthrough, and parity; add keyboard or interaction checks when the table or report has controls.
For a printable document or deck, combine documents, visual craft, applicable semantics/accessibility, data, copy, task walkthrough, and parity; inspect actual page output when available.
For an audit-only task, do not edit.
For a mixed task, state which part is audit-only and which has repair authority.

The shared [QA reference](../skills/artifact-design/references/qa-parity.md) separates source, rendered, interaction, automated, export, and user evidence.
It requires a before/after record of protected facts, figures, units, citations, links, qualifications, actions, and meaningful states.
Visual craft findings and usability, accessibility, factual, or behavior findings use separate report groups so that a style preference cannot obscure a factual or access barrier.

## Synthesis boundaries

The compiler integrated all 26 primary distillation assignments into the local taxonomy; the exact sources, collection categories, pins, licensing links, and adopted/conditional/excluded rationale are in [source selection](source-selection.md).
The resulting prose, examples, procedures, and code are rewritten synthesis rather than concatenated summaries.
Existing report, tool, editorial, landing, copy, implementation, and motion references were preserved and connected to the route.
The [provenance register](provenance.md) also records prior Anthropic, OpenAI, Impeccable, writing, critique, taste, and standards sources.

The package does not install upstream plugins, require an MCP service, or depend on an online source catalog at runtime.
It does not require a concept vote, design questionnaire, fictional study, universal palette, arbitrary quota, or claim of world-class quality.
Reference coverage documents routing intent; only executed evidence can establish that a particular artifact was reviewed or improved.
