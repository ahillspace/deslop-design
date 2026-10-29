# Forward-use fixture inputs

These folders retain the four original synthetic prompts and the source files supplied with them for the forward-use tasks described in [validation](../validation.md).
Names, dates, organizations, sample readings, quotations, request records, and report content are fictional evaluation material and are not operational records.

Each case preserves the original relationship between its prompt and fixture paths, so the prompt's `fixtures/...` references resolve when used from the same task-relative directory as the original.
The input set contains no evaluator reports, expected answers, screenshots, browser profiles, or redesigned outputs.

| Case | Prompt | Fixture directory |
|---|---|---|
| Interactive product audit | [01-product-audit.md](01-product-audit/artifacts/01-product-audit.md) | [01-product](01-product-audit/artifacts/fixtures/01-product/) |
| Narrative report redesign | [02-report-redesign.md](02-narrative-report/artifacts/input/02-report-redesign.md) | [02-report](02-narrative-report/artifacts/input/fixtures/02-report/) |
| Printable decision brief | [03-print-document.md](03-print-decision/artifacts/03-print-document.md) | [03-print-decision](03-print-decision/artifacts/fixtures/03-print-decision/) |
| Fixed-PDF audit | [04-fixed-pdf-audit.md](04-fixed-pdf-audit/artifacts/input/raw/04-fixed-pdf-audit.md) | [04-fixed-document](04-fixed-pdf-audit/artifacts/input/raw/fixtures/04-fixed-document/) |

`SHA256SUMS` records the hashes of all 15 original prompt and fixture files.
From the repository root, verify them with `sha256sum -c docs/forward-fixtures/SHA256SUMS`.

These are the cases used during development and are not held-out material for a comparative benchmark.
