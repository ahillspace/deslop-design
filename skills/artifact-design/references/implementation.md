# Implementation techniques

Read this during design work.
These are editable starting points, not a required visual style or component library.
Keep the project system when one exists and change the values to fit its content.

## Let content set the layout

Use flexible measures and reflow where the content stops fitting.
Fluid type and spacing help editorial or promotional work; dense product controls often need steady sizes and structural breakpoints instead.
Do not let a narrow viewport remove evidence or actions that define the task.

~~~css
:root {
  --page-gutter: clamp(1rem, 3vw, 3rem);
  --section-gap: clamp(2.75rem, 7vw, 6rem);
  --display-size: clamp(2.25rem, calc(1.25rem + 4vw), 5.5rem);
  --reading-width: 68ch;
}

.page-shell {
  width: min(82rem, calc(100% - var(--page-gutter) - var(--page-gutter)));
  margin-inline: auto;
}

.prose {
  max-width: var(--reading-width);
}

.content-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(15rem, 0.85fr);
  gap: clamp(1.5rem, 4vw, 4rem);
  align-items: center;
}

@media (max-width: 50rem) {
  .content-layout {
    grid-template-columns: 1fr;
  }
}
~~~

Use a fluid value for something that should change continuously, such as an editorial title, outer gutter, or section gap.
Use a breakpoint when the order, available controls, or relationship between regions changes.
Let the text and media set their height; avoid fixed-height containers that clip zoomed, translated, or longer content.
For repeated peers, an auto-fitting grid can work; do not turn unequal information into equal cards just because the CSS is easy.

## Make hierarchy visible

Decide what should be noticed first, next, and only when needed.
Create that order with scale, weight, position, contrast, grouping, and density together.
One primary action may need a strong treatment; quiet supporting material still needs enough contrast to read.

Assign semantic color roles from the product system, such as text, secondary text, surface, border, action, status, and focus.
Measure actual foreground and background pairs.
WCAG 2.2 AA calls for 4.5:1 for ordinary text and 3:1 for large text; key visual component boundaries and graphic information also have a 3:1 contrast requirement against adjacent colors.
Do not use color as the only cue for status, selection, or error.
Check focus rings and links as well as default text.
See [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## Pick a device that explains this material

Use the content's real shape to decide what the visitor sees.
A chart can compare measured values; an annotation can point out the exception; a timeline can show a real sequence; a diagram can explain a relationship; a table can preserve exact records; a photograph can show the actual place or object.
Connect each device to nearby text that explains its meaning and limits.
Do not invent data, use filler imagery as proof, or use decoration to imply evidence.

Before adding a small visual detail, ask what it helps someone see, distinguish, or do.
A border can group related controls; a number can show an actual sequence; an icon can help locate an action.
Leave it out when it carries no meaning.
