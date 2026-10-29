# Accessibility evidence and review

Use this reference for a thorough HTML or interface audit, an accessibility-focused repair, or a material access concern found during broader work.
For documents, apply only the checks supported by the actual format and state the applicable standard before making a conformance claim.
This is an evidence and repair guide, not a legal opinion or accessibility certification.

## Set a bounded scope

Record artifact version, route or document, reader task, states, environments available, and any stated target standard, version, and level.
If no conformance target is given, report applicable observed failures against exact criteria without declaring the page or product conformant or nonconformant as a whole.
Whole-process claims require the complete relevant scope, states, and alternatives.
For non-web documents, use an applicable document standard; WCAG2ICT can guide interpretation, but do not assume every web criterion or legal requirement applies.

Use WCAG 2.2 when it is the applicable target and cite the exact success criterion and level.
The normative [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) defines the requirement; W3C Understanding pages are informative explanations.
Useful criteria for common artifact work include [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships), [1.3.2 Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence), [1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum), [1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow), [1.4.12 Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing), [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard), [2.4.3 Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order), [2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible), [2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum), [2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), and form criteria [3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification), [3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions), and [3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion).

Use only the criterion whose requirement matches the observed issue and account for its exceptions.
WCAG 2.2 AA target size is 24 by 24 CSS pixels subject to stated exceptions; 44 by 44 is the Level AAA criterion's target size, with its own exceptions, and may also be a design preference.
Do not conflate CSS pixels with points or call 44px the universal AA minimum.
The 1.4.10 reflow test is not a generic phone screenshot; test the criterion's equivalent width and relevant two-dimensional-content exception.
The 1.4.12 criterion tests tolerance of specified user text-spacing overrides, not an author default style recipe.

## Gather and label evidence

- **Automated:** record tool, version if known, build/state, rule, element, and whether the issue was confirmed. A clean scan cannot establish accessibility or usability.
- **Manual:** record browser, viewport/zoom, input, starting state, action sequence, and visible outcome. Name assistive technology and version only if used.
- **Source:** identify relevant markup, style, or code; use it to support a likely cause, not to claim rendered behavior.
- **Rendered:** name the view, theme, state, and content actually opened. A screenshot establishes appearance only.
- **Inferred:** state what the artifact suggests and what evidence is missing.
- **Untested:** name the unavailable environment or state and what conclusion it prevents.

Inspect the whole relevant task path, including normal, focused, expanded, invalid, loading, empty, success, and failure states when they exist.
Use safe fixtures rather than triggering destructive or real consequential actions.
Use available automated checks as leads, then verify context and exceptions.
Check native semantics, headings and relationships, accessible names, visible focus, text and status alternatives, keyboard operation, reading order, contrast, zoom/reflow, and user preference behavior as applicable.
Read [keyboard and focus](keyboard.md) for widget contracts and [responsive behavior](responsive.md) for the exact reflow and text-spacing methods.

## Write useful findings

For each actionable finding record:

`title and location / state and reproduction / evidence class / exact criterion or “no criterion asserted” / cause or hypothesis / task impact / priority / remedy / verification`.

Keep criterion conformance separate from practical usability.
Severity reflects task consequence, scope, and workaround; it is not a WCAG rating.
Use a blocker for an essential task failure or material access barrier; major for substantial friction; minor for limited polish.
Do not claim that a specific person was blocked without evidence about that person.
Keep strengths worth preserving and unassessed areas visible.

Prefer native controls and semantic relationships.
Use ARIA only when native semantics do not express the required name, role, state, or relationship.
Keep meaning available without color alone and keep essential content available through zoom and reflow.
For documents, inspect meaningful link text, heading and table structure, captions, alternatives, and reading sequence when the format exposes them.

### Example: an inaccessible disclosure

A pointer click expands a section, but the clickable `div` is skipped by Tab and does nothing with Enter or Space.
This supports a keyboard finding against WCAG 2.2 SC 2.1.1 when the disclosed functionality is unavailable by keyboard.
Replace it with a native button, preserve its visible name, expose the expanded state, and retest Tab, Enter, Space, focus visibility, and both states.
Do not assert a name/role/state criterion unless those programmatic properties were also checked.

## Close with honest limits

Report scope, criteria applied, evidence types, findings, strengths, changed and retested behavior, and exact untested areas.
Do not infer full conformance from sampled pages, a linter, a screenshot, source markup, ARIA attributes, or a short manual path.
For a review-only request, report findings and do not edit.
For an authorized change, repeat the reproduction steps and describe any remaining barrier.
