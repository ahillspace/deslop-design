# User preferences and adaptable presentation

Use this reference when user or operating-system settings can change motion, color, contrast, text spacing, or density in the artifact.
It does not require adding a dark theme or a preference panel to every product.

## Inspect the actual preference behavior

Identify which settings the platform or product exposes and which parts of the artifact depend on them.
Check reduced motion, forced colors, contrast or color scheme, text enlargement and spacing, and any explicit user-selected density or theme when applicable.
Name the browser, operating system, setting, state, and rendered result actually tested.
Source inspection cannot prove system rendering; a screenshot of one theme cannot establish other preference behavior.

Keep the core meaning and task available under each supported setting.
Use semantic color roles so preference overrides change related states coherently.
In forced colors, prefer system colors and explicit outlines or borders where needed, then inspect the browser output because platforms vary.
Do not globally ban black or invert every illustration, chart, logo, or photograph.
Keep status labels and shapes legible if colors are substituted.

Make nonessential motion suppressible when the user requests reduced motion.
Prefer content visible by default and add reveal behavior only after motion support is ready.
When reduced motion is active or scripts fail, required content should remain visible.
Avoid strobing, large spatial displacement, forced autoplay, or motion that blocks a task.
If motion has a useful role, keep the state understandable without animation.
See [motion](motion.md) for construction and lifecycle details.

Allow user text and spacing overrides without clipping, overlap, or loss of function.
Keep controls and content at intrinsic height where possible.
If the product provides a density or simplified view, preserve important facts and actions and make the alternate presentation clear; do not label a preference as an accessibility fix without evidence.

### Example: status and reduced-motion fallback

A report labels “On track” in green and “At risk” in red, marks invalid input only with a red border, and hides sections until an observer reveals them.
In forced colors, the two statuses may become indistinguishable; the error may lose its only cue; and a script failure may leave the report invisible.
Keep textual status labels and a distinct non-color cue, associate an error message with the invalid field, and keep sections visible unless motion support explicitly enhances them.
Check default, forced-color, reduced-motion, and script-failure states where the environment allows.
The scenario is illustrative, not observed evidence.

## Preserve and report

Keep user-selected settings, data, meaning, behavior, and established visual system.
Do not invent a user preference or claim that an interface caused harm from source alone.
Report the actual preference states tested, the context and result, any applicable criterion, and what remained unavailable.
Repeat the same preference checks after an authorized change.
