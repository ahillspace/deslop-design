# Keyboard, focus, and input alternatives

Use this reference when interactive behavior, focus, composite controls, pointer-only gestures, or keyboard access is in scope.
For focus visibility and contrast criteria, also use [accessibility](accessibility.md); for responsive input contexts, use [responsive](responsive.md).

## Start with the task and native behavior

Exercise the essential task with keyboard and pointer where available.
Record the control, starting state, exact key or action, resulting state, focus location, and any untested assistive technology.
Inspect source or DOM to identify roles and accessible names, but verify behavior in the rendered artifact.
Prefer native links, buttons, inputs, and disclosure controls over custom elements with recreated keyboard behavior.
Use ARIA only when native semantics do not provide the needed name, role, state, or relationship.

Do not require every descendant of a composite widget to be a separate Tab stop.
Use the widget's documented internal navigation and ensure keyboard order remains logical for the task.
Do not reorder focus with positive `tabindex` values.
Visual and focus order need not be pixel-identical, but they must not create a misleading or impossible task sequence.

## Match the contract to the pattern

Consult the actual [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) pattern when implementing or auditing a custom widget.
Patterns vary and are not interchangeable.

- **Tabs:** the tablist is normally entered at the selected tab; arrow keys move among tabs; another Tab leaves for the panel or next stop. Automatic activation suits panels that appear without noticeable delay; otherwise use manual activation with an explicit activation key.
- **Menu button:** a trigger opens the menu and moves focus into its menu items; Escape closes it and returns focus when appropriate. Do not apply application-menu keys to ordinary site navigation links.
- **Modal dialog:** focus moves into meaningful dialog content, remains within the modal while it is open, and returns to its opener or a justified fallback on close. Non-modal dialogs do not trap focus.
- **Forms:** use native labels, fieldset/legend for related choices, and a task-meaningful order. Associate errors and preserve data; move or announce focus only when it helps recovery.
- **Drag and gesture:** provide a non-drag route for functionality that otherwise requires dragging, such as buttons or a keyboard-operable position field. Keep the gesture as an optional shortcut when useful.
- **Carousels and sliders:** follow the chosen pattern; keep current value or slide perceivable and controls available. Autoplay needs a usable stop/pause mechanism. Do not assume every slide is traversed with arrow keys.

Check visible focus in every relevant state and ensure dialogs, sticky bars, tooltips, and menus do not hide the active control at zoom.
Use the exact WCAG criterion and exceptions when claiming a standards defect; the detailed rule is in [accessibility](accessibility.md).

### Example: a custom date picker

If a calendar grid has no predictable keyboard movement and selection is encoded only by color, do not patch it with arbitrary key handlers.
Use a labeled native date input when that meets the task.
If a calendar is required, implement the APG date picker dialog pattern and test date entry, calendar navigation, selection, cancellation, focus visibility, and return of focus.
Keep a text-entry route when it serves the product.
Report any browser or assistive-technology behavior that could not be checked.

## Preserve and report

Keep supported pointer actions, shortcuts, labels, permissions, and task behavior.
Add an equivalent input path without deleting a useful optional gesture.
For findings, record location, reproduction steps, observed focus and state, likely cause, task effect, remedy, and evidence limits.
For repairs, repeat the same keyboard and pointer path and confirm focus and state after the change.
Automated scans can flag likely issues; they do not prove keyboard operation.
