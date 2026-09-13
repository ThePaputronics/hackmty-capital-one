# F.R.E.D open SPEI detection engine presentation

Spanish, seven-slide, five-minute executive pitch with a five-second animated opener, large projection typography,
high-level and low-level architecture, business impact, proposed AWS scaling, Open Banking positioning, and an IEEE references slide. F.R.E.D is the product
name; Sentinel remains the technical package name in the repository.

## Run and present

Serve the directory from the repository root to enable the locally bundled Three.js modules:

```bash
python -m http.server 4173 --bind 127.0.0.1 --directory site
```

Visit <http://127.0.0.1:4173>. No build is required. Cormorant Garamond and Lora
load from Google Fonts, with Georgia as the offline fallback.

- The opener begins as plain text. Right arrow, Page Down or Space starts its five-second transformation; it stops on F.R.E.D until you advance.
- During the animation, two forward presses within 420 ms skip it. The launch press is excluded; held-key repeats are ignored.
- After the opener, left/right arrows, Page Up/Page Down, or Space advance; Shift+Space reverses.
- Home resets the opener; End jumps to the closing slide.
- The animation pauses while a dialog is open or the tab is hidden. Moving the mouse distorts the text and repels particles.
- F toggles fullscreen; I opens the index.
- Escape closes a dialog or exits browser fullscreen.
- Hash links open individual slides, such as `#high-level` and `#low-level`.
- Mobile screens scroll within each slide to preserve readable typography.
- Without JavaScript, slides appear in a continuous document.
- Print/PDF keeps the seven content slides plus references, omitting the animated opener and controls.

`speech.md` provides the timed five-minute pitch: 5-second opener + 30 + 45 + 45 + 40 + 60 + 45 + 30 seconds.
`sources.md` records evidence, assumptions, rubric coverage and pending work.
`benchmark.json` records the synthetic benchmark executed for this revision.
This website is a presentation, not a PPTX, live risk API client, or payment UI.

## Confirmed product direction

F.R.E.D is a detection engine for destination risk and transfer manipulation,
not a CLABE search service. The confirmed model is API as a Service: a worker continuously processes
SPEI transactions, correlates activity by CLABE, and updates a risk database.
The API serves already-processed signals to banks; API reads and customer
transfers do not trigger the analysis. Banxico is the proposed central operator.
Central operation, national capacity, and institutional adoption are not delivered.
The current checkout has a simulation worker calling synchronous evaluation;
it does not establish a production risk materializer or per-CLABE read endpoint.

The user confirmed open APIs and rules with protected data, as a proposed
standard for Banxico. Financing is explicitly undefined; the pitch focuses on
public impact. No license, pricing, funding agreement, or service-revenue model
was introduced. API documentation alone is not an adopted standard or an
open-source license.

## Validation

Backend review used the existing API, scorers, feature store, schemas, simulator,
tests and evaluation harness. Five API tests and two generator tests passed.
The seed-42, 30-day benchmark evaluated 615 synthetic transfers, intercepted
6/6 APP attacks, and reported 0% consumer/merchant false positives in that sample.
The local latency is not an end-to-end or national-scale claim. See `sources.md`
for limitations and observed production-readiness gaps; no backend code changed.

## Cloud migration boundary

Dockerfiles, FastAPI, PostgreSQL, environment configuration and Alembic are
present. The pitch proposes ECR, independent ECS/Fargate API and worker services,
ALB and RDS. There is no deployed AWS infrastructure or completed cloud migration.
Images were not built for this revision. Worker coordination/idempotency,
materialized risk, single-run schema migrations, IAM/networking and load testing
are required before production scaling. See `sources.md` for exact evidence.

Headless Chromium validation passed for the content slides at 1440 × 900,
1280 × 720 and 390 × 844. Desktop slides fit without scrolling; mobile content
scrolls vertically without horizontal overflow. Keyboard navigation, index,
sources and fullscreen passed without JavaScript page errors. Print
export contains the content slides and references. Opening metrics and cloud architecture were
visually reviewed; syntax, local assets, IDs and whitespace checks passed.
Backend tests and benchmark were not rerun for this content-only revision;
`benchmark.json` retains the prior executed results.

## Animated opener

`opener.js` manages the animation clock, double-press gesture, pauses and fallback.
`intro-scene.js` uses custom Three.js shaders and canvas-generated glyph textures
for mouse distortion, luminous particles and the transformation into F.R.E.D.
The F/R particles originate from Fraud, E from Engine and D from Detection.
Three.js 0.186.0 is bundled locally under `vendor/three` with its MIT license.
No build step or remote JavaScript CDN is required. WebGL2 is required for the
shader version; unavailable/lost contexts use a text fallback. Reduced-motion
preferences use a simpler transition with the same controls and timing.
Opening through `file://` may block modules and use that fallback instead.

Opener validation passed in headless Chromium with software WebGL rendering:
initial idle state, launch versus double-press skip, held-key suppression, five-second
auto advance, dialog pause/resume, replay, navigation cancellation, mouse response,
reduced motion, unavailable WebGL and context loss. Eight screen sections fit the
three documented viewports, and the PDF retains the expected pages. JavaScript syntax
checks passed; the browser reported no page errors. Physical
GPU performance and projector appearance still require a check on the presentation
computer. The existing backend was not changed by this animation.
