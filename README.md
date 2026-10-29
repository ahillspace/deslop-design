# deslop-design

Two Markdown skills for agents building HTML artifacts with deliberate design and useful copy.
They connect the reader's task to content, visual decisions, implementation, and browser evidence.
They prescribe no house palette or universal layout.

| Skill | Use it for |
|---|---|
| [artifact-design](skills/artifact-design/SKILL.md) | Creating or substantially redesigning a report, dashboard, explanation, or landing page. |
| [artifact-review](skills/artifact-review/SKILL.md) | Reviewing an existing artifact or checking completed UI work, with repairs only within granted authority. |

Design loads only relevant genre guidance and works without review.
Review works without a prior design session.
Neither needs a framework, external service, global install, or project instruction-file changes.
Bring the browser tooling and project components you already use.

## Project-local installation

Clone this repository or download a revision, then open a shell.
Set `package_dir` to its absolute checkout path and `project_dir` to the existing project's absolute root.
The commands below copy both complete skill folders with the package license and refuse to replace an existing installation.
Review existing folders before intentionally updating them.
Keep the two folders beside each other so the optional cross-skill link resolves.

For Codex CLI, use the repository's `.agents/skills` directory, as described in the [official local skill documentation](https://learn.chatgpt.com/docs/build-skills).

```sh
set -eu
test -d "$project_dir"
skill_parent="$project_dir/.agents/skills"
mkdir -p "$skill_parent"
for skill in artifact-design artifact-review; do
  test ! -e "$skill_parent/$skill" || { echo "Already installed: $skill" >&2; exit 1; }
done
for skill in artifact-design artifact-review; do
  cp -R "$package_dir/skills/$skill" "$skill_parent/$skill"
  cp "$package_dir/LICENSE" "$skill_parent/$skill/LICENSE"
done
```

For Claude Code, use `.claude/skills`, as described in its [skill documentation](https://code.claude.com/docs/en/skills).

```sh
set -eu
test -d "$project_dir"
skill_parent="$project_dir/.claude/skills"
mkdir -p "$skill_parent"
for skill in artifact-design artifact-review; do
  test ! -e "$skill_parent/$skill" || { echo "Already installed: $skill" >&2; exit 1; }
done
for skill in artifact-design artifact-review; do
  cp -R "$package_dir/skills/$skill" "$skill_parent/$skill"
  cp "$package_dir/LICENSE" "$skill_parent/$skill/LICENSE"
done
```

Start a session in the target project.
In Codex CLI, mention `$artifact-design` or `$artifact-review`; `/skills` also lists available skills.
In Claude Code, invoke `/artifact-design` or `/artifact-review`.
Both can select skills from descriptions; explicit invocation makes your intention clear.
If a skill is missing, restart the session and check its path.
These project paths and copy commands were tested in temporary directories; live discovery and invocation are separately described in [validation](docs/validation.md).
Other Markdown-capable agents can read the entry file and relevant relative references directly, but automatic discovery in other harnesses is untested.

## Example

Suppose you have a CSV of sampling stations, collection dates, concentrations, and a supplied threshold.
A useful request is:

> Use artifact-design to build an HTML report for the sampling team from this CSV and methods note.
> Lead with which stations exceed the supplied threshold, retain missing readings, include units and methods, and make the evidence usable on phones.
> Label uncertainty; do not infer a health conclusion from the threshold alone.

After building, request:

> Use artifact-review to review the report at desktop and phone sizes.
> Check table navigation and whether each conclusion is supported.
> Report findings only; do not edit files.

This is an illustrative brief, not a claim about an actual dataset or a measured improvement.

## Package and limits

```text
skills/
  artifact-design/
    SKILL.md
    references/{reports,tools,editorial,landing,copy}.md
  artifact-review/
    SKILL.md
docs/
  rationale.md
  provenance.md
  validation.md
  benchmark.md
scripts/check_package.py
.github/workflows/check.yml
LICENSE
```

Read [rationale and coverage](docs/rationale.md) for the mechanisms retained, [source provenance](docs/provenance.md) for the licensing boundary, and [validation](docs/validation.md) for executed checks.
The [benchmark plan](docs/benchmark.md) is proposed, not executed.
A small author-run smoke trial cannot establish human preference or professional equivalence.
Browser access can be unavailable; the review skill must disclose that limitation instead of claiming rendered verification.
Automated checks cannot certify accessibility or taste.

Original package text and checker code are [MIT licensed](LICENSE).
Linked projects, fonts, images, customer content, and other external assets retain their own terms.
