# Design rationale and coverage

This package serves agents creating four kinds of HTML artifact and maintainers who need to know why each instruction exists.
The design entrypoint runs an inferred direction through implementation and rendered correction after invocation.
Review keeps its independent findings and repair path.
Both preserve project requirements and existing product decisions.

The design skill classifies the visitor's job per surface.
A product may have a persuasive landing page, an operational workspace, and a reading surface with different information needs.
The route uses that job rather than treating a whole company as one visual genre.

| Mechanism and intended effect | Maintained location | Conceptual sources |
|---|---|---|
| Reader, task, evidence, and unknowns are identified before styling | [Design: orient](../skills/artifact-design/SKILL.md#orient) | A, B, D, E |
| Surface job and mixed product surfaces separate brand expression from operational UI | Design: orient; [landing](../skills/artifact-design/references/landing.md); [tools](../skills/artifact-design/references/tools.md) | B, I, J |
| Autonomous direction keeps routine choices inside the work while material truth or authority gaps remain explicit | Design: orient and build | A, B, I |
| One relevant genre reference keeps report evidence and product task flows from inheriting a landing-page sequence | [Design router](../skills/artifact-design/SKILL.md#orient); the four genre references | B, I; original report synthesis |
| Fluid sizing, structural breakpoints, semantic contrast roles, and content-specific visual devices are reproducible | [Implementation techniques](../skills/artifact-design/references/implementation.md) | A, I, J, L |
| Copy review catches unsupported importance, vague claims, attribution gaps, rhythm, and weak endings while retaining voice | [Copy](../skills/artifact-design/references/copy.md) | H, E, F |
| A progressive reveal shows one passive sequence without hiding required content or keyboard actions | [Motion](../skills/artifact-design/references/motion.md) | A, I, J, L |
| Semantic controls, real state changes, and truthful recovery keep designed interactions usable | Design: build; tools; [review evidence](../skills/artifact-review/SKILL.md#gather-evidence) | D, I, J |
| Rendered captures plus keyboard, state, and source checks distinguish visual judgment from mechanical evidence | [Review: gather evidence](../skills/artifact-review/SKILL.md#gather-evidence) and design completion | B, C, J |
| Findings rank user consequence, evidence, and confidence; bounded repairs protect scope | [Review: judge and prioritize](../skills/artifact-review/SKILL.md#judge-and-prioritize) and [repair and close](../skills/artifact-review/SKILL.md#repair-and-close) | C, G |
| Unknowns and limits are disclosed rather than described as completed verification | Both entry skills; [validation](validation.md) | B, C, G; original completion contract |

## Context cost and routing

The design entrypoint holds the shared workflow and the links needed to route a task.
It loads the implementation reference for each build and one genre reference for the main surface.
It loads copy when visible language or claims need substantive editing.
It loads motion only when motion is useful.
It does not require every genre reference or a persistent design sidecar.

The total context cost is therefore the entrypoint plus implementation plus the selected genre, with copy and motion added only when relevant.
Validation records current word counts for each resource and the common paths.
The counts make the shared load and optional per-path cost visible; they are maintenance information, not a quality score.

The package leaves review independent and keeps its repair authority tied to the request.
It omits a runtime engine, install hook, automatic detector, required concept competition, random style selection, taste score, and external design service.
Those would add state or setup without being needed to deliver these HTML artifacts.

[Provenance](provenance.md) distinguishes conceptual sources from reused expression.
[Validation](validation.md) records executed checks and evidence limits.
[Benchmark](benchmark.md) describes a future comparison rather than a demonstrated advantage.
