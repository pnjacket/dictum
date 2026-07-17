# CLAUDE.md

Guidance for Claude Code working in the **Dictum** repo.

## What this repo is

Dictum is a product-agnostic **standard for build-ready software documentation** — a spec for what a software spec *set* must contain so that an AI or a human can build the product from the docs **without guessing**. It scales from a 200-line CLI to a multi-product platform. Read `README.md` (overview) and `STANDARD.md` (the method). It was distilled from a real AI-driven build study; the worked examples throughout are illustrations, not dependencies.

## Repo map

- `STANDARD.md` — the standard, Parts 0–13. The source of truth for the method.
- `TUTORIAL.md` — the human on-ramp (authors the worked example by hand, end to end). `WORKFLOWS.md` — the journey index: tool sequences per situation, each naming the operator's part vs the tooling's.
- `GLOSSARY.md` — the vocabulary.
- `failure-mode-catalog.md` — each rule tied to the real failure it prevents.
- `concerns/11.1`–`11.15` — the 15 concern specifications (STANDARD Part 11): 6 core, 2 baseline, 7 module.
- `templates/` — fill-in skeletons (concern-doc, single-file, manifest, binding-map).
- `examples/jotdo/` — the worked example: the CLI validation product, folded in trimmed and renamed (the name is invented; never reintroduce the original).
- `skills/`, `agents/` — advisory Claude Code tooling. Skills: `install-dictum` (install the tooling + standard into a target product repo; runs from this checkout, not copied into products), `doc-scaffold` (greenfield start), `doc-excavate` (brownfield code→doc bootstrap, Part 10f), `doc-levelup`, `doc-feature` (doc-led forward flow, Part 10e), `doc-change-impact`. Agents: `doc-maturity-auditor`, `code-cartographer` (reverse-map existing code, Part 10f), `drift-detector` (code→doc), `implementation-planner` (doc→code, Part 10e), `concern-specialist`.
- `ROADMAP.md` — open/deferred items (none blocking).
- **Boundary rule:** executable/empirical tooling (deterministic checkers, extractors, trial corpora, studies) lives in the **`dictum-lab`** companion repo (sibling checkout), never here — this repo holds normative text + the Claude Code authoring skills/agents only, and must never depend on anything in the lab. Findings flow back only as distilled rules (failure modes, bar changes) via versioned releases.

## Core model (settled — don't re-derive)

- **Two axes:** BREADTH (which of the 15 concerns / sub-aspects apply, from product traits) × DEPTH (a 5-rung ladder: `Absent → Sketch → Specified → Contract-grade │ Verified`).
- **Scope is the only calibration lever** — it covers both CLI↔platform and PoC↔production. **Contract-grade never weakens**; a PoC just scopes more out (recorded in each doc's *Non-goals*).
- **Owned once, referenced everywhere** — every contract lives in one concern and is referenced by stable ID (`CAP-### · ENTITY-### · COMPONENT-### · API-### · ROLE-### · SCREEN-### · ENV-### · …`). Those IDs form the traceability web.
- **Document contract** — uniform sections that *map to rungs* (STANDARD Part 4): a doc's maturity is which sections are complete.
- **Markers** — subject markers (`[GAP] [ASSUMPTION] [REVISIT] [FUTURE-SCOPE]`) stay in published docs; build markers (`<!-- BUILD: ... -->`) strip on publish.
- **Fidelity-staged DoD** — merge gate vs release gate; own code always real, external deps substitutable per an environment fidelity map.

## Conventions when editing

- **Editorial form is governed by [`EDITORIAL.md`](EDITORIAL.md)** (the source; the points below summarize it): the **three-tier split** — rule + one-line why → the standard · distilled rationale → `failure-mode-catalog.md` · evidence/worked-examples/numbers → `dictum-lab`; no war-stories or research artifacts ("(round N)", "vX.Y bar") in normative prose; the standard stands alone and never links to the lab; describe-by-shape. Charter version rides the standard's (RELEASES.md).
- Docs are **self-exemplifying**: match the existing front-matter and document-contract structure.
- If you add or change a **rule**, keep `failure-mode-catalog.md` and the relevant *Design Decisions* in sync.
- `concerns/11.x` correspond to STANDARD Part 11 — keep the two consistent.
- **Reference contracts by ID; never duplicate** a contract another concern owns.
- On publish: strip build markers, flip `status: published`, bump the version.

## Status & roadmap

- Complete and validation-hardened at **`v1.1.0`** — Parts 0–13: the authoring method, the **enhancement lifecycle** (10d), the **doc-led implementation flow** (10e), **brownfield reverse-authoring** (10f), and the **doc↔tracker boundary** (10c), plus the advisory tool suite (6 skills + 5 agents). (v1.1.0 = the **gate-bound publish step** (failure-mode #30) + the **versioning policy**, plus: the **machine-extraction extension points** (the `DICT: <ID>` in-code marker token grammar; the register-form minting bar, Part 5; the `SOURCE:` provenance marker added in v1.2.0), the `CONFIG-###` (11.10) and `OUT-###` (11.4) contract kinds, the optional **dual-realization binding** (`wire:` sub-contract, failure-mode #31), the **vocabulary re-partition check + upgrade walk** (failure-mode #32, optional manifest `authored_against:`), the worked example, and the 11.11 alerting-in-scope worked example — full notes in `RELEASES.md`.) Validated by building four deliberately different products — a CLI, a multi-user web app, a real-time multi-tenant messaging SaaS, and a client-only browser voxel game (the per-build validation write-ups live in `dictum-lab`). Every bar traces to a real failure in `failure-mode-catalog.md`.
- **Licensing (settled):** prose is **CC BY 4.0** (freely shareable *and* adaptable, with attribution + indicate-changes; *applying* the method carries no obligation); tooling and templates (`skills/`, `agents/`, `templates/`) are **MIT**. The **one-canonical-version** guarantee rests on **signed releases from the canonical repo** (`RELEASES.md`) + a **first-mover naming convention** (`TRADEMARK.md`) — not copyright, and **not a registered trademark** (none is claimed or intended; the name may change without affecting the method). Root `LICENSE` is the authoritative file→license map; `POSITIONING.md` holds the competitive positioning + prior-art basis.
- **Open items live in [`ROADMAP.md`](ROADMAP.md)** — nothing blocking: cross-repo doc-set linking & federation (parked); embedded/hardware surface generalization (revisit soon); per-app trait sub-blocks. The standard defines machine-readable **extension points, never tools** — worked-example tooling lives in `dictum-lab`. Keep `ROADMAP.md` current when items open or close.
