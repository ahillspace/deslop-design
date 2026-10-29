# Design rationale and coverage

This package serves agents creating four kinds of HTML artifact and maintainers who need to know why each instruction exists.
The central decision is to organize content around reader success before choosing a visual direction.
Two skills separate creation from evidence-based review without requiring an orchestrator or a specific browser vendor.

The design skill owns content truth, selective genre routing, and a coherent surface system.
The review skill owns evidence, findings, and a bounded repair loop within the user's authority.
Genre references hold only decisions that differ by surface; copy guidance is optional additional detail.
Ordinary task notes can retain facts, design choices, provenance, and review evidence without imposing filenames or a new persistence system.

| Mechanism and intended effect | Maintained location | Conceptual sources in the provenance register |
|---|---|---|
| Audience, task, and source ledger prevent decoration from substituting for substance | [Design: establish the material](../skills/artifact-design/SKILL.md#establish-the-material) | A, B, D, E |
| Surface-specific routing prevents reports and tools from inheriting marketing structures | [Design router](../skills/artifact-design/SKILL.md#establish-the-material), all four genre references | B; original report-specific synthesis |
| Established-system precedence protects existing product decisions | Both entry skills; [tools](../skills/artifact-design/references/tools.md) | B, D |
| Reference interpretation transfers a principle while excluding identity and unlicensed assets | [Design: choose and implement](../skills/artifact-design/SKILL.md#choose-and-implement) | A, C |
| Related type, color, spacing, density, and responsive choices create coherence without a house style | Design; all genre references | A, B, D |
| Actual copy, proof, terminology, and truthful recovery preserve meaning | [Copy](../skills/artifact-design/references/copy.md), [landing](../skills/artifact-design/references/landing.md), both entries | E, F |
| Semantic elements, existing primitives, and explicit states protect usable behavior | Design; tools; [review evidence](../skills/artifact-review/SKILL.md#obtain-evidence) | D; existing browser practice |
| Captures plus interaction and source checks distinguish visual judgment from mechanical evidence | Review evidence and [judgment](../skills/artifact-review/SKILL.md#judge-and-prioritize); design completion | B, C |
| Ranked findings and small repair batches focus effort on consequences | [Review: repair and close](../skills/artifact-review/SKILL.md#repair-and-close) | C, G |
| Budgeted rounds and explicit unknowns prevent false completion claims | Both entry skills; validation documentation | B, C, G; original completion contract |

The entry bodies target at most 1,500 words combined.
The initial draft contains 1,235 body words, or 1,304 including frontmatter; the checker reports current counts so revisions remain inspectable.
The five references total 1,182 words and range from 204 to 299 words each.
This is an ownership budget, not a quality score; exceptions should explain which behavior needs the extra context.
No instruction requires loading the whole collection.

The package deliberately omits universal aesthetic bans, random style selection, required concept competitions, numerical taste gates, mandatory design sidecars, runtime engines, and global hooks.
These mechanisms either substitute a house style for the brief or add maintenance without a concrete need here.
An existing design system can already answer most visual decisions; a small artifact can remain native HTML/CSS.

[Provenance](provenance.md) distinguishes ideas from reused expression.
[Validation](validation.md) describes what has actually been exercised, and [benchmark](benchmark.md) describes the evidence still needed before claiming an advantage.
