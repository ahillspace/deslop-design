---
name: artifact-review
description: Audit HTML and documents with visual, content, factual, accessibility, responsive, and interaction evidence. Report findings only unless repair or redesign is explicitly authorized.
---

# Artifact review

Judge whether the artifact helps its intended reader understand, decide, present, or act.
Preserve its supported facts, required content, behavior, and strengths outside the authorized scope.

## Route before reviewing

Read [classification and routing](../artifact-design/references/routing.md) first.
Classify medium, purpose, requested operation, and conditional features for each materially different route or section.
Read every applicable reference in full and use its procedure.
For a thorough review, cover all applicable visual craft, content, accessibility, factual, responsive, document, and interaction dimensions even if the request named one concern.
Record a compact coverage note for the delivery.

## Gather evidence

Inspect the actual artifact in an isolated browser or document view when available.
Check the complete relevant sequence, representative long content, middle and end, important states, and the relevant screen widths or pages.
For HTML, use rendered evidence for appearance, DOM/source for structure, and keyboard or pointer checks for behavior.
For documents, inspect the reading order, figures, captions, tables, references, and actual print/export when applicable.
Use safe fixtures for unavailable or failure states; do not trigger real destructive actions.

Name the version, state, viewport or page, and evidence class for each finding.
A screenshot does not prove behavior or keyboard access; source inspection does not prove rendering; an automated scan cannot establish accessibility conformance or comprehension.
If evidence is unavailable, continue with what can be inspected and mark the affected conclusion unknown.

## Report findings and strengths

Separate **visual craft** findings from **usability, accessibility, factual, and behavior** findings.
For each actionable finding include location and state, observed evidence, likely cause or explicit uncertainty, reader impact, a specific remedy, verification needed or performed, severity, and confidence.
Keep preference separate from defects and cite an exact standard only when the observed failure matches it.
Prioritize an essential task failure, misleading or unsupported claim, material access barrier, and substantial friction before local polish.
Name evidence-backed strengths that should survive a repair.

## Keep review authority clear

An audit, review, critique, or inspection request is findings-only.
Do not edit or silently rewrite.
When the request explicitly authorizes repair, redesign, or rewrite, fix only the scoped issues, compare protected content and behavior before and after, and retest the affected views and paths.
Do not remove a qualification or change behavior to make a layout look cleaner.

Report the route coverage, surfaces and states inspected, findings, strengths, changes if authorized, checks actually performed, and material limitations.
Do not report a clean screenshot, linter, self-rating, or first viewport as proof of the whole artifact.
