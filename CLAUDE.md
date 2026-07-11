# CLAUDE.md

Guidance for Claude Code working in the **Dictum** repo.

## What this repo is

Dictum is a product-agnostic **standard for build-ready software documentation** — a spec for what a software spec *set* must contain so that an AI or a human can build the product from the docs **without guessing**. It scales from a 200-line CLI to a multi-product platform. Read `README.md` (overview) and `STANDARD.md` (the method). It was distilled from a real AI-driven build study; the worked examples throughout are illustrations, not dependencies.

## Repo map

- `STANDARD.md` — the standard, Parts 0–13. The source of truth for the method.
- `GLOSSARY.md` — the vocabulary.
- `failure-mode-catalog.md` — each rule tied to the real failure it prevents.
- `concerns/11.1`–`11.15` — the 15 concern specifications (STANDARD Part 11): 6 core, 2 baseline, 7 module.
- `templates/` — fill-in skeletons (concern-doc, single-file, manifest, binding-map).
- `skills/`, `agents/` — advisory Claude Code tooling. Skills: `install-dictum` (install the tooling + standard into a target product repo; runs from this checkout, not copied into products), `doc-scaffold` (greenfield start), `doc-excavate` (brownfield code→doc bootstrap, Part 10f), `doc-levelup`, `doc-feature` (doc-led forward flow, Part 10e), `doc-change-impact`. Agents: `doc-maturity-auditor`, `code-cartographer` (reverse-map existing code, Part 10f), `drift-detector` (code→doc), `implementation-planner` (doc→code, Part 10e), `concern-specialist`.
- `ROADMAP.md` — open/deferred items (none blocking).

## Core model (settled — don't re-derive)

- **Two axes:** BREADTH (which of the 15 concerns / sub-aspects apply, from product traits) × DEPTH (a 5-rung ladder: `Absent → Sketch → Specified → Contract-grade │ Verified`).
- **Scope is the only calibration lever** — it covers both CLI↔platform and PoC↔production. **Contract-grade never weakens**; a PoC just scopes more out (recorded in each doc's *Non-goals*).
- **Owned once, referenced everywhere** — every contract lives in one concern and is referenced by stable ID (`CAP-### · ENTITY-### · COMPONENT-### · API-### · ROLE-### · SCREEN-### · ENV-### · …`). Those IDs form the traceability web.
- **Document contract** — uniform sections that *map to rungs* (STANDARD Part 4): a doc's maturity is which sections are complete.
- **Markers** — subject markers (`[GAP] [ASSUMPTION] [REVISIT] [FUTURE-SCOPE]`) stay in published docs; build markers (`<!-- BUILD: ... -->`) strip on publish.
- **Fidelity-staged DoD** — merge gate vs release gate; own code always real, external deps substitutable per an environment fidelity map.

## Conventions when editing

- Docs are **self-exemplifying**: match the existing front-matter and document-contract structure.
- If you add or change a **rule**, keep `failure-mode-catalog.md` and the relevant *Design Decisions* in sync.
- `concerns/11.x` correspond to STANDARD Part 11 — keep the two consistent.
- **Reference contracts by ID; never duplicate** a contract another concern owns.
- On publish: strip build markers, flip `status: published`, bump the version.

## Status & roadmap

- Complete and validation-hardened at **`v1.0.0`** — Parts 0–13: the authoring method, the **enhancement lifecycle** (10d), the **doc-led implementation flow** (10e), **brownfield reverse-authoring** (10f), and the **doc↔tracker boundary** (10c), plus the advisory tool suite (5 skills + 5 agents). Validated by building four deliberately different products — a CLI, a multi-user web app, a real-time multi-tenant messaging SaaS (**Verified** on local Kubernetes: real OIDC no-bypass, cross-replica fan-out, tenant isolation on REST *and* the event surface), and a client-only browser voxel game (**Verified at merge fidelity**). Every bar traces to a real failure in `failure-mode-catalog.md`.
- **Licensing (settled):** prose is **CC BY 4.0** (freely shareable *and* adaptable, with attribution + indicate-changes; *applying* the method carries no obligation); tooling and templates (`skills/`, `agents/`, `templates/`) are **MIT**. The **one-canonical-version** guarantee rests on **signed releases from the canonical repo** (`RELEASES.md`) + a **first-mover naming convention** (`TRADEMARK.md`) — not copyright, and **not a registered trademark** (none is claimed or intended; the name may change without affecting the method). Root `LICENSE` is the authoritative file→license map; `POSITIONING.md` holds the competitive positioning + prior-art basis.
- **Open items live in [`ROADMAP.md`](ROADMAP.md)** — nothing blocking: publishing a worked example (housekeeping); design-system binding `[REVISIT]` (UX 11.9, needs a design tool) and cross-product federation (parked design topics); model-B deterministic drift-detector (`[FUTURE-SCOPE]`). Keep `ROADMAP.md` current when items open or close.
