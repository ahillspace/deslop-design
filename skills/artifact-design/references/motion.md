# Motion and interaction

Load this only when movement helps a person notice a change, understand a relationship, or feel the subject's character.
A still page is often clearer.
Choose a trigger, the information it adds, the start and end states, and what happens if the change is interrupted.
Prefer a native control and clear text feedback over motion that exists only to decorate.

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

Interactive elements must still work by keyboard and show a visible focus state.
Provide the same state information in text or shape, not animation or color alone.
For state transitions triggered by a control, make the control work first and animate only the resulting state.
Respect reduced motion for those transitions too.

See [W3C's reduced-motion guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) and inspect the effect on a real device when the movement could affect comfort or performance.
