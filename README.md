# Dictum

**A standard for build-ready software documentation — the doc set an AI or a human can build from without guessing.**

Dictum defines *what a complete software specification set must contain*, and to what precision, so that a product can be built straight from its docs with no gaps left for the implementer to fill by guessing. It scales by **scope alone**, from a 200-line CLI to a multi-product SaaS platform, and ships with templates and advisory Claude Code tooling to produce *and maintain* a conforming doc set repeatably.

It is **markdown-first and tool-agnostic**: the standard is prose plus templates; the tooling sits on top as a convenience, never a dependency.

---

## Why it exists

Hand a *layer-organized* specification to an implementer — human or AI — and they build in layers: backends with no frontend, frontends with no backend, tests that never exercise a real user, screens nothing links to. The documentation *teaches* the failure. Dictum was distilled from a real, AI-driven build study where exactly these failures appeared, and **every rule traces back to one of them** (see [`failure-mode-catalog.md`](./failure-mode-catalog.md)).

The fix isn't "write more docs." It's writing them against a **contract**: a feature can't be called done in a single layer, every interface is owned once and referenced everywhere, and "tested" means a real flow actually ran.

## The model in one minute

- **Two axes, nothing more.**
  - **Breadth** — *which* of 15 concerns (and which sub-aspects within them) are in scope, derived from the product's traits.
  - **Depth** — *how complete* each concern's doc is, on a 5-rung ladder: **Absent → Sketch → Specified → Contract-grade │ Verified**.
- **Scope is the only calibration lever.** A proof-of-concept and a regulated release use the *same* standard; the PoC simply scopes more out. **Contract-grade never weakens** — you apply it to a smaller surface, not a lower bar.
- **Owned once, referenced everywhere.** Every contract — a capability, entity, endpoint, role, screen — lives in exactly one concern and is referenced by stable ID (`CAP-### · ENTITY-### · API-### · …`). Those IDs form one **traceability web** — `CAP → SCREEN → API → COMPONENT → ENV` — so a capability can't be built in one layer and forgotten in another.
- **"Done" is fidelity-staged.** A developer's *merge gate* validates against the highest fidelity runnable locally (external dependencies may be substituted); a *release gate* validates against real infrastructure. The rule that keeps it honest: **your own code is always real; only external dependencies may be substituted** — mock S3, yes; bypass login, never.
- **Build-ready** = every in-scope concern has reached Contract-grade **and the set is published** (build markers stripped, status flipped, versions bumped). That is the handoff to implementation.

## Authored once, then maintained for life

A doc set is written ~once and **enhanced** for the rest of the product's life — never re-derived from scratch. The same owned-once ID web that prevents authoring drift, read backwards, *is* the change-impact graph, so the standard covers the whole lifecycle with no extra machinery:

- **Doc-led forward flow** *(Part 10e)* — move the docs ahead of the code on purpose, then derive an ordered, vertical-slice build plan from the delta.
- **Keep docs true over time** *(Part 10d)* — a change propagates one hop along the ID web; detected code↔doc drift is adjudicated (fix the doc, or fix the code — never both silently).
- **Brownfield adoption** *(Part 10f)* — reverse-author a faithful as-built baseline from an *existing* undocumented repo: code sources structure, an interview sources intent.
- **External trackers, without losing the source of truth** *(Part 10c)* — GitHub Issues / Jira / Azure DevOps are a **downstream mirror of what Dictum owns**: contracts and build-status stay repo-authoritative and work items *reference* contract IDs, while a feature request (demand) or a suspected bug (triage) is an input to authoring, never a substitute for it.

## What's in this repo

| Path | What |
|---|---|
| [`STANDARD.md`](./STANDARD.md) | The standard itself — Parts 0–13. The normative reference. |
| [`TUTORIAL.md`](./TUTORIAL.md) | The human on-ramp — walk the worked example end to end in ~20 minutes. |
| [`WORKFLOWS.md`](./WORKFLOWS.md) | The end-to-end journeys — which tool, in what order, to what gate — each naming the operator's part vs the tooling's. |
| [`GLOSSARY.md`](./GLOSSARY.md) | The full vocabulary. |
| [`failure-mode-catalog.md`](./failure-mode-catalog.md) | Each rule tied to the real failure it prevents. |
| [`concerns/`](./concerns) | The 15 concern specifications (6 core, 2 baseline, 7 module). |
| [`templates/`](./templates) | Fill-in skeletons: per-concern, single-file, the product-profile manifest, the binding map, and the build-status record. |
| [`skills/`](./skills) · [`agents/`](./agents) | Advisory Claude Code tooling — 6 skills + 5 agents (see below). |
| [`examples/`](./examples) | A complete worked example: the CLI validation product (trimmed and renamed), a published single-file doc set with resolvable bindings over a ~200-line product. |
| [`ROADMAP.md`](./ROADMAP.md) | Open and deferred items (nothing blocking). |

## Using it

**New here?** Start with [`TUTORIAL.md`](./TUTORIAL.md) — it walks the worked example ([`examples/jotdo/`](./examples/jotdo)) from a two-sentence brief to a published, build-ready doc set in about twenty minutes. Then [`WORKFLOWS.md`](./WORKFLOWS.md) maps each journey (new product · adopt on an existing repo · close gaps · ship a feature doc-first · keep docs true) to the exact tool sequence and the gate that ends it.

**Who reads what.** The normative text — [`STANDARD.md`](./STANDARD.md) and the [`concerns/`](./concerns) specs — is a dense reference, optimized for completeness and auditability; in practice it is consumed mostly by tooling and AI assistants, and by humans as a lookup rather than a cover-to-cover read. Humans learn the method fastest by doing (the tutorial), and thereafter mostly read conforming *doc sets*, which are written for people. The division of labor behind this — intent and judgment are the operator's, the clerical layer is the tooling's, and the standard's honest limits are stated rather than patched — is a first principle: STANDARD Part 0.7.

**Run it in Claude Code** — the tooling is advisory (it assists, never blocks). Install it into a product repo with the `install-dictum` skill (run from this checkout), then reach for:

- **New product** → `doc-scaffold` — interview → product-profile manifest → generated doc set.
- **Existing undocumented repo** → `doc-excavate` — reverse-map the code → manifest + doc set + binding map *(Part 10f)*.
- **Raise maturity** → `doc-levelup` to bring a concern to its next rung; `doc-maturity-auditor` (read-only) reports rungs, gaps, and build-readiness.
- **Ship a feature** → `doc-feature` → `implementation-planner` — author the delta, then plan the slices.
- **Track drift** → `drift-detector` (read-only) → `doc-change-impact` — detect, then propagate.

PoC vs production is a scoping decision, not a different process — narrow the scope, keep the bar.

## Research companion

Real-world trials, reference tooling (including a deterministic, CI-friendly gate checker), trial protocols, and a conformance fixture corpus live in a separate research project, **`dictum-lab`** — deliberately outside this repository and **non-normative**: this standard's text is the only definition of conformance, and the standard never depends on any tool. Findings flow back here only as distilled rules, through the versioned release process.

## The 15 concerns

**Core (always):** Product & Requirements · Domain & Data · Architecture · Interfaces & Contracts · Quality & Testing · Delivery Process
**Baseline (always, scales with risk):** Security & Privacy · Governance & Compliance
**Module (trait-triggered):** User Experience · Operations & Infrastructure · Observability & Monitoring · Integrations & External Dependencies · Performance & Scalability · Accessibility & Internationalization · Business & Legal

## Status & provenance

> **Version caveat — trust tags, not `main`.** The version numbers you see on the
> latest commit of `main` (this section, the docs' front-matter `version:` fields)
> describe a **working state** and can be ahead of, or simply wrong relative to,
> any released version. The only authoritative versions of Dictum are the
> **signed release tags and the exact commits they point to** — see
> [`RELEASES.md`](./RELEASES.md) for how to verify one. Cite and build against a
> release, not against `main`.

**`v1.1.0`**. The standard is complete and validation-hardened across Parts 0–13: the full authoring method, the enhancement lifecycle *(10d)*, the doc-led implementation flow *(10e)*, brownfield reverse-authoring *(10f)*, the doc↔tracker boundary *(10c)*, and the advisory tool suite (6 skills + 5 agents). v1.1.0 binds the **publish step** to the authoring gates (build-ready hands off a *published* set; implementation events never touch doc status — failure-mode #30), adds the **versioning policy**, names the three **machine-extraction extension points** (the in-code `DICT: <ID>` marker token; the register-form minting bar; the `SOURCE:` provenance marker), adds the `CONFIG-###`/`OUT-###` contract kinds, the optional dual-realization binding, the vocabulary re-partition check + upgrade walk, and the worked example — full notes in [`RELEASES.md`](./RELEASES.md).

It was distilled from a real AI-driven build study, then **validated by building** four deliberately different products — a CLI, a multi-user record-management web app, a real-time multi-tenant messaging SaaS exercising all 15 concerns, and a client-only browser voxel game. Each build fed refinements back into the bars — every one traceable to an observed failure in [`failure-mode-catalog.md`](./failure-mode-catalog.md); the per-build validation write-ups live in the research companion (above). The worked examples throughout the standard are illustrations, not dependencies. Open and deferred items live in [`ROADMAP.md`](./ROADMAP.md).

## License

Dictum is licensed in two parts, by content type (see [`LICENSE`](./LICENSE) for the authoritative mapping):

- **The standard (prose)** — `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/`, and the project docs — is under **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. Share and adapt it freely, with attribution and an indication of any changes. There is one *canonical* standard, but that guarantee comes from **signed releases from the canonical repository** ([`RELEASES.md`](./RELEASES.md)) plus a **first-mover naming convention** ([`TRADEMARK.md`](./TRADEMARK.md)) — not a copyright restriction — so an adaptation is allowed; we just ask that forks not call themselves "Dictum." **Applying** Dictum to your own product's docs is not even an adaptation of the text; do that without restriction.
- **The tooling and templates** — `skills/`, `agents/`, `templates/` — are under the **[MIT License](./LICENSES/MIT.txt)**, so you can copy them into your own repos and adapt them freely.

The **"Dictum" name** is a first-mover naming convention (no registered trademark) — see [`TRADEMARK.md`](./TRADEMARK.md); release authenticity is established by [`RELEASES.md`](./RELEASES.md).

## Contributing

Contributions are welcome — see [`CONTRIBUTING.md`](./CONTRIBUTING.md). Sign commits off with `git commit -s`. Prose changes are contributed under **CC BY 4.0** (inbound = outbound) and tooling/template changes under **MIT**; you retain copyright in either case.

## Prior art & influences

Dictum is a synthesis; almost none of its primitives are original, and it doesn't need them to be. Its contribution is the *composition* — a breadth×depth completeness bar, an owned-once contract-ID web, and a fidelity-staged Definition-of-Done — assembled into one standard aimed at building software from documentation without guessing. It stands on:

- **Design by Contract** — Bertrand Meyer (Eiffel; *IEEE Computer*, 1992): the "contract" vocabulary. "Contract-grade" as a named rung is Dictum's own.
- **The Capability Maturity Model** — Paulk et al., SEI (1993): the device of discrete, named, ordered maturity levels. Dictum's rungs and their build-readiness semantics are its own.
- **Separation of concerns** — E. W. Dijkstra (EWD447, 1974); carried forward by ISO/IEC/IEEE 42010's "concerns."
- **Don't Repeat Yourself / single source of truth** — Hunt & Thomas, *The Pragmatic Programmer* (1999): the root of "owned once, referenced everywhere." The cross-concern stable-ID *web* is Dictum's extension.
- **Continuous Delivery & test doubles** — Humble & Farley (2010); Meszaros, *xUnit Test Patterns* (2007): promotion/quality gates and dependency substitution. Dictum adds the structured **environment fidelity map** over a *documentation* Definition-of-Done.
- **Requirements-engineering traceability** — ISO/IEC/IEEE 29148 and the RE tradition, extended into a cross-concern reference web.

Where Dictum reuses a term of art, it means what the source means. Where it coins a term (*contract-grade*, *owned once, referenced everywhere*, *fidelity map*, the rung names), that term is its own — and, being a short phrase, is not claimed by copyright regardless; the name and conformance are governed by [`TRADEMARK.md`](./TRADEMARK.md).
