# Motion and interaction

Load this only when movement helps a person notice a change, understand a relationship, or feel the subject's character.
A still page is often clearer.
Choose a trigger, the information it adds, the start and end states, and what happens if the change is interrupted.
Prefer a native control and clear text feedback over motion that exists only to decorate.

## Give movement a specific job and character

Inspect the actual trigger, initial and final states, path, repetition, scope of the moving area, interruption, reduced-motion response, and useful static state.
Use the product's existing motion language and component behavior as evidence.
If they are absent, choose a restrained treatment from the content and task, and label that direction as an inference rather than approved brand intent.

Movement can preserve spatial continuity, identify what changed, stage a sequence, confirm an action, communicate progress, or add a supported character.
Write its job in one sentence before implementation.
Ask what becomes harder to follow if it is removed; if nothing meaningful changes, keep the state static.
Describe character with observable qualities such as pace, distance, direction, grouping, and visual weight, rather than a mood adjective alone.
Do not impose a required number of animations or a signature duration.

Stage the primary change before secondary detail when sequence helps comprehension.
Coordinate items that readers perceive as one unit.
Use a stagger only when order clarifies hierarchy and does not delay useful content.
Choose easing and duration from the movement's distance, mass, semantic importance, frequency, urgency, and ability to interrupt.
An entering object may settle with deceleration; a departing object may accelerate away; a repositioning object may benefit from a smooth in-and-out path.
These are starting associations, not laws.
Shorter is not always better, and a longer transition needs a clear purpose without postponing access to the result.

Treat rapid input as part of the design.
When state can reverse, the latest state should win without snapping to an unrelated origin.
Cancel or retarget overlapping motion rather than stacking a backlog.
Keep focus and input available throughout.
Prefer transform and opacity only when they suit the effect; large surfaces, filters, shadows, compositing layers, and device constraints can still be costly.
Avoid repeated layout work during animation and use `will-change` only for a demonstrated need.
Profile representative hardware only when motion is large, repeated, or central to the task.

Separate observation from instruction when using a reference artifact.
An observation describes what the reference actually does; an instruction states what the new artifact should do and why that trait transfers.
Do not copy a reference's signature choreography or treat its performance as proof for this product.

## Example: reveal supporting material once

Use an entry reveal only for a small group of passive material where it improves reading order.
Do not put links, buttons, form controls, or other keyboard targets inside hidden reveal regions.
The page remains visible when scripts are disabled, the observer is unavailable, or reduced motion is requested.
The browser recalculates intersection as the viewport or layout changes; there is no scroll handler to maintain.

~~~html
<section class="story-beat" data-reveal>
  <h2>How the repair moves through the shop</h2>
  <p>The three labeled stations follow the actual intake sequence.</p>
</section>
~~~

~~~css
.story-beat {
  opacity: 1;
  transform: none;
}

.motion-ready [data-reveal] {
  opacity: 0;
  transform: translateY(0.55rem);
  transition:
    opacity 240ms ease-out,
    transform 240ms cubic-bezier(0.16, 1, 0.3, 1);
}

.motion-ready [data-reveal].is-visible {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: reduce) {
  .motion-ready [data-reveal] {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
~~~

~~~js
const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
let revealObserver;

function updateReveals() {
  revealObserver?.disconnect();
  revealObserver = undefined;
  document.documentElement.classList.remove("motion-ready");
  document.querySelectorAll("[data-reveal]").forEach((item) => {
    item.classList.remove("is-visible");
  });

  if (motionPreference.matches || !("IntersectionObserver" in window)) return;

  const items = document.querySelectorAll("[data-reveal]");
  if (!items.length) return;

  revealObserver = new IntersectionObserver((entries, observer) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  }, { rootMargin: "0px 0px -5% 0px" });

  document.documentElement.classList.add("motion-ready");
  items.forEach((item) => revealObserver.observe(item));
}

updateReveals();
motionPreference.addEventListener("change", updateReveals);
window.addEventListener("pagehide", () => {
  revealObserver?.disconnect();
});
window.addEventListener("pageshow", (event) => {
  if (event.persisted) updateReveals();
});
~~~

Adjust distance, easing, and duration for the content and device; a short fade with a small offset is a starting point, not a signature.
For a related set, stagger only a few items and keep the total wait short.
Prefer opacity and transform for inexpensive paint work; avoid animating layout dimensions on every frame.
When the system motion preference changes to reduce, the example removes its opt-in class and makes every item visible immediately.
When the page is hidden, it disconnects the observer; a page restored from the back-forward cache starts observing again.
For a component-based app, disconnect the observer and remove the media-query listener when that component unmounts.
Do not apply this recipe to content whose visibility is required before interaction or to an entire long page by default.

## Example: preserve position while filtering a list

Use movement only to show where the remaining rows went after a local filter.
The filter result and count update immediately; the motion only bridges the spatial change.
This example keeps the filter input outside the rows so rapid typing keeps focus in place.

~~~html
<label for="reading-filter">Filter readings</label>
<input id="reading-filter" type="search" autocomplete="off">
<p data-result-count role="status" aria-live="polite"></p>
<ul data-reading-list>
  <li data-reading-row>North channel: 4.6 mg/L nitrate-N</li>
  <li data-reading-row>East meadow: 3.1 mg/L nitrate-N</li>
  <li data-reading-row>Lower bridge: 4.0 mg/L nitrate-N</li>
</ul>
~~~

~~~css
[data-reading-row][hidden] { display: none !important; }
~~~

~~~js
const filter = document.querySelector("#reading-filter");
const list = document.querySelector("[data-reading-list]");
const count = document.querySelector("[data-result-count]");
const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
let activeMoves = [];

function filterReadings(query) {
  const rows = [...list.querySelectorAll("[data-reading-row]")];
  const canMove = !motionPreference.matches && typeof Element.prototype.animate === "function";
  const before = new Map();

  if (canMove) {
    for (const row of rows) {
      if (!row.hidden) before.set(row, row.getBoundingClientRect());
    }
  }

  for (const animation of activeMoves) animation.cancel();
  activeMoves = [];

  const term = query.trim().toLowerCase();
  for (const row of rows) row.hidden = !row.textContent.toLowerCase().includes(term);

  const visible = rows.filter((row) => !row.hidden);
  count.textContent = `${visible.length} readings shown`;

  if (!canMove) return;

  for (const row of visible) {
    const start = before.get(row);
    if (!start) continue;
    const end = row.getBoundingClientRect();
    const x = start.left - end.left;
    const y = start.top - end.top;
    if (Math.abs(x) < 1 && Math.abs(y) < 1) continue;

    activeMoves.push(row.animate(
      [
        { transform: `translate(${x}px, ${y}px)` },
        { transform: "translate(0, 0)" },
      ],
      { duration: 220, easing: "cubic-bezier(.2, .8, .2, 1)" },
    ));
  }
}

filter.addEventListener("input", () => filterReadings(filter.value));
motionPreference.addEventListener("change", (event) => {
  if (!event.matches) return;
  for (const animation of activeMoves) animation.cancel();
  activeMoves = [];
});
window.addEventListener("pagehide", () => {
  for (const animation of activeMoves) animation.cancel();
  activeMoves = [];
});

filterReadings(filter.value);
~~~

On each new keystroke the current rendered row positions are captured before the prior moves are canceled, so the next transition starts from where the rows appear now instead of a queued or stale destination.
Newly visible rows appear immediately; surviving rows move into their new positions.
The 220ms easing is a short-distance trial for a local list; check the actual row travel and frequent input, and shorten or remove it if it competes with filtering.
If reduced motion is enabled during a transition, cancellation leaves the already-updated list in its final state.
If a row contains focusable controls, do not hide the focused row without a separate focus-recovery rule; see [keyboard behavior](keyboard.md).
Test rapid filter changes and the reduced-motion toggle in the actual component before using this recipe.

Interactive elements must still work by keyboard and show a visible focus state.
Provide the same state information in text or shape, not animation or color alone.
For state transitions triggered by a control, make the control work first and animate only the resulting state.
Respect reduced motion for those transitions too.

See [W3C's reduced-motion guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) and inspect the effect on a real device when the movement could affect comfort or performance.
