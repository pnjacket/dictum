---
artifact: documentation-standard
role: guide
status: published
version: 1.1.0
audience: [human-team]
---

# The Dictum Tutorial — author a doc set by hand, end to end

This is the **human on-ramp**. In about twenty minutes it walks the standard's worked example — [`examples/jotdo/`](examples/jotdo), a ~150-line task-list CLI — from a two-sentence brief to a published, build-ready doc set, touching every core idea once: traits → scope, the maturity ladder, owned IDs, markers, the gate, the publish step, and life after publish.

Two things to know before you start:

- **You will not normally do this by hand.** The advisory tooling ([`WORKFLOWS.md`](WORKFLOWS.md)) carries the clerical layer — that division of labor is a first principle (STANDARD Part 0.7). You do it by hand *once, here*, because it is the fastest way to learn what the tooling is doing on your behalf and which decisions are irreducibly yours.
- **The normative text is a reference, not a syllabus.** [`STANDARD.md`](STANDARD.md) and the [`concerns/`](concerns) specs are dense on purpose — written for lookup (and for tooling), not cover-to-cover reading. This tutorial cites the parts as you meet them; read them the way you'd read a statute someone just quoted at you.

Every excerpt below is real — from [`examples/jotdo/docs/SPEC.md`](examples/jotdo/docs/SPEC.md), which you can keep open beside this page.

---

## The brief

> **jotdo** — a tiny single-user task-list CLI. Add tasks from the terminal, list them, mark them done, remove them. Tasks persist to a local JSON file. Python 3, standard library only.

That paragraph is the *operator's* contribution — the tooling's first move (`doc-scaffold`) is to ask you for exactly this, in your own words, before it infers anything.

## Step 1 — Traits decide breadth

Dictum has **15 concerns** (STANDARD Part 2). You never choose among them by taste; the product's **traits** decide. Six are Core (always in), two are Baseline (always in, depth scales with risk), and seven are Modules that a trait switches on:

| Trait question | jotdo | Module triggered |
|---|---|---|
| Interactive UI? | no — a CLI | User Experience: **off** |
| Deployed running service? | no — a local script | Operations, Observability: **off** |
| Third-party dependencies? | no — stdlib only | Integrations: **off** |
| Real performance/scale needs? | no | Performance: **off** |
| Any UI / multi-locale? | no | Accessibility & i18n: **off** |
| Commercial / distributed? | no | Business & Legal: **off** |

Result: jotdo's doc set covers exactly the 6 Core + 2 Baseline concerns, and nothing else. A trait answer, not a judgment call, is what keeps two authors' scope decisions consistent.

**Scoping continues *inside* each concern.** Each concern spec publishes a vocabulary of **sub-aspect keys**; you scope those in or out too, and every scope-out records one of two **kinds** (Part 9):

- `absent` — the subject **doesn't exist** in this product. Justification: the trait fact. Nothing is owed later.
- `deferred` — the subject exists but is calibrated out of *this* effort. A `[FUTURE-SCOPE]` re-entry note is owed.

From jotdo's Domain section, both kinds in the wild:

> - *Migrations & versioning (kind: **deferred**):* the store format is frozen at v1. [FUTURE-SCOPE] If the store format ever changes, migrations re-enter scope.
> - *Consistency & transactions (kind: **absent**):* single process, single writer — concurrent access is a product non-goal.

This is the whole PoC↔production mechanism. **Scope is the only calibration lever** (Part 0.4): a proof-of-concept scopes more out; the bar on whatever stays in never weakens.

## Step 2 — The manifest, and packaging

The scope decisions land in one machine-readable file, the **product-profile manifest** ([`examples/jotdo/manifest.yaml`](examples/jotdo/manifest.yaml), template in [`templates/`](templates)): traits, in-scope concerns, `out_of_scope_subaspects` (the published keys), and each concern's current rung. It is the source of truth; any human-facing index is derived from it (Part 7).

Packaging is your call, guided by size (Part 8): jotdo takes the **single-file** form — one `SPEC.md`, concerns as sections. A larger product takes one file per concern. Stable IDs (next step) make repackaging safe either way.

## Step 3 — Climb the ladder

Every concern's completeness is measured on one 5-rung ladder (Part 3):

```
Absent → Sketch → Specified → Contract-grade │ Verified
```

- **Sketch** — intent captured: purpose, non-goals, an outline.
- **Specified** — complete prose; a skilled human could build with judgment.
- **Contract-grade** — testable acceptance + explicit contracts; **an AI can build without guessing**. This is the author's finish line.
- **Verified** — built and proven by a real-flow test. Not yours to claim: it belongs to Delivery, after the build. **Doc maturity ≠ implementation status.**

The rungs aren't a vibe — the document skeleton maps sections to rungs (Part 4), so *which sections are complete IS the maturity*. And the gap between Specified and Contract-grade is precisely the set of questions an implementer would otherwise have to ask you mid-build. Dictum's bet is that answering them at authoring time is cheaper than answering them as build-time interruptions — or worse, not being asked (Part 0.6).

Watch Product & Requirements make the last climb. Specified says: *"users can add a task and see it listed."* Contract-grade says:

> **Capabilities.**
> - `CAP-ADD` — add a task by title.
> - `CAP-LIST` — list all tasks with their state.
>
> **Success criteria (measurable).**
> - `SUCCESS-ROUNDTRIP` — a task added in one invocation is present in the next `list`.

Those backticked names are the next idea.

## Step 4 — Owned IDs, minted once

Every contract — a capability, an entity, an invariant, a CLI command — gets a **stable ID**, is **defined in exactly one place** (its owning concern), and is **referenced by ID everywhere else** (Part 5). The line that defines it is its **register line** — like `` `CAP-ADD` — add a task by title`` above; every other occurrence anywhere in the set is a reference, never a second definition.

The point is not tidiness. The IDs form a **traceability web** that runs through the whole set:

```
CAP-ADD  →  CLI-ADD  →  COMPONENT-CLI  →  ENTITY-TASK  →  INV-TASK-ID-MONOTONIC
(product)   (interface)  (architecture)     (domain)         (invariant)
```

Follow one strand through jotdo's sections: Domain owns the entity and its invariants —

> - `INV-TASK-ID-MONOTONIC` — a new task's `id` is strictly greater than every id ever issued; ids are never reused, even after a removal.

Architecture records the decision that satisfies it —

> - `ADR-MONOTONIC-SEQ` — the store carries a persisted `seq` rather than computing `max(id)+1`, so ids stay monotonic across removals (satisfies `INV-TASK-ID-MONOTONIC`).

Interfaces specifies the command that exercises it, referencing — never restating — the capability, component, and entity. And Quality's **coverage map** closes the loop by giving every contract an observable check:

> | `INV-TASK-ID-MONOTONIC` | `test_ids_monotonic` |

This web is why a capability can't quietly ship backend-only, and — read backwards — it is also the change-impact graph you'll meet in Step 7. Every rule of this kind traces to an observed failure; the receipts are in [`failure-mode-catalog.md`](failure-mode-catalog.md).

## Step 5 — Markers: honesty while you work

While authoring you will not know everything. Dictum gives you two marker families (Part 6) so the doc never silently pretends:

- **Subject markers** — `[GAP]` (something the product owes an answer), `[ASSUMPTION]` (inferred, not confirmed), `[REVISIT]`, `[FUTURE-SCOPE]`. About the *product*; they survive into published docs.
- **Build markers** — `<!-- BUILD: ... -->` comments: authoring scaffolding, stripped on publish.

The discipline they enforce: **an unanswered question is recorded, never guessed.** When the tooling runs unattended it must infer — and then every inference is an `[ASSUMPTION]` you review later (Part 0.6). Nothing is silently settled either way.

## Step 6 — The gate, and the publish step

Author the remaining concerns in dependency order — Product → Domain/Architecture → Interfaces → Quality/Delivery → the baselines — so contracts exist before anything references them (Part 10). Even a baseline concern earns its keep at this scale: jotdo's Security section is one testable *negative* assertion (`SEC-LOCAL-ONLY` — no network I/O of any kind, asserted by `test_local_only`) plus honest `absent` scope-outs.

Then the finish line, two halves (Part 10):

1. **Build-ready** — every in-scope concern has reached Contract-grade. The `doc-maturity-auditor` checks this for you: actual rung vs claimed, dangling references, open markers.
2. **Published** — the mechanical publish step: strip build markers, flip `status: draft → published`, bump the version. The handoff artifact is the *published* set; a marker-laden draft is not hand-off-able (Part 6).

What you hand to the implementer — human or AI — is a contract they can satisfy **without asking you anything**. That sentence is the entire standard (Part 0.3).

## Step 7 — Life after publish

The doc set is authored ~once and then **enhanced** for the product's life (Part 0.1). Two artifacts and one habit carry the whole lifecycle:

- **The binding map** ([`examples/jotdo/bindings.yaml`](examples/jotdo/bindings.yaml)) — where each contract lives in code, down to runnable `asserted_by` selectors for invariants. jotdo's code also carries the in-code marker (`# DICT: CLI-ADD`) at each realizing site — cheap at build time, and it keeps every later code→doc pass a *recovery* instead of a re-derivation (Part 10f).
- **Change events** (Part 10d) — suppose jotdo grows due dates. `doc-feature` authors the delta (a new field on `ENTITY-TASK`, a flag on `CLI-ADD`), classifies it (`additive`), and the ID web — read backwards — says exactly who must react: the entity's referencers get flagged; everything else is provably untouched. Detected code↔doc drift enters as the same kind of event, and **you adjudicate** it: fix the doc, or fix the code — never both silently.
- **The habit** — docs move first, code catches up (Part 10e). The delta re-publishes at hand-off; the build then closes the loop (bindings resolve, coverage tests pass) without ever touching doc status.

## Where to go next

- [`WORKFLOWS.md`](WORKFLOWS.md) — the six journeys, tool by tool, each naming *your part* vs the tooling's.
- [`examples/jotdo/`](examples/jotdo) — reread the spec now that you know what every line is doing; then the manifest and binding map.
- [`STANDARD.md`](STANDARD.md) — the reference. You now know its shape; use it as a lookup.
- [`GLOSSARY.md`](GLOSSARY.md) — every term above, defined.
- [`failure-mode-catalog.md`](failure-mode-catalog.md) — why each rule exists; the standard's receipts.
