---
artifact: documentation-standard
role: guide
status: published
version: 1.0.0
audience: [ai-implementer, human-team]
---

# Dictum Workflows

The end-to-end journeys through Dictum — **which tool, in what order, to what gate**.

This page is an **index, not a re-specification**. Each workflow *sequences* the tools and points into the authoritative method (`STANDARD.md`, its Part 10x flows) and the individual tool procedures (`skills/`, `agents/`). Owned-once (STANDARD Part 5) applies to Dictum's own docs too — the steps live in the tools and the standard; this page only orders them. All tooling is **advisory: it assists, never blocks** (STANDARD Part 10b).

**First:** install the tooling into your product repo with the **[`install-dictum`](skills/install-dictum/SKILL.md)** skill (run it from the Dictum checkout, targeting your repo).

## Pick your starting point

| Your situation | Workflow |
|---|---|
| Brand-new product, no code yet | [1. Start a new product (greenfield)](#1-start-a-new-product-greenfield) |
| Existing code, no or only informal docs | [2. Adopt Dictum on an existing repo (brownfield)](#2-adopt-dictum-on-an-existing-repo-brownfield) |
| Docs exist but aren't build-ready | [3. Raise maturity and close open sections](#3-raise-maturity-and-close-open-sections) |
| Add or change a feature | [4. Ship a feature, doc-first](#4-ship-a-feature-doc-first) |
| Code and docs have drifted apart | [5. Keep docs true over time](#5-keep-docs-true-over-time) |
| "Where do we stand?" | [6. Check maturity and build-readiness](#6-check-maturity-and-build-readiness) |

Two constants across every journey (STANDARD Part 3): **Contract-grade** is the author's finish line — an AI can build without guessing; **build-ready** = every in-scope concern at Contract-grade. **Verified** is owned by Delivery Process, not the doc tools. The markers you will resolve — `[ASSUMPTION]` `[GAP]` `[REVISIT]` `[FUTURE-SCOPE]` — are defined in STANDARD Part 6 and the [`GLOSSARY.md`](GLOSSARY.md).

---

## 1. Start a new product (greenfield)

**When** — a new product; author the docs first, then build.

1. [`doc-scaffold`](skills/doc-scaffold/SKILL.md) — an interview (to saturation) → the product-profile manifest → a generated doc set from the templates.
2. [`doc-levelup`](skills/doc-levelup/SKILL.md) — raise each concern toward Contract-grade, **foundational first**: Product & Requirements → Domain / Architecture → Interfaces → downstream.
3. [`doc-maturity-auditor`](agents/doc-maturity-auditor.md) — rungs vs claims, gaps, cross-reference integrity, build-ready verdict.

**Gate** — build-ready: every in-scope concern Contract-grade. Hand off to implementation (Workflow 4 covers the first build).
**See** — STANDARD Part 10 (Intake → Scaffold → Author-to-rung → Review → Publish), Part 10b.

## 2. Adopt Dictum on an existing repo (brownfield)

**When** — the product already exists as code with no (or only informal) docs.

1. [`doc-excavate`](skills/doc-excavate/SKILL.md) — reverse-authors an **as-built baseline from code** (via the read-only [`code-cartographer`](agents/code-cartographer.md)): manifest + doc set + a **binding map minted at authoring time**, with `[ASSUMPTION]`/`[GAP]`/`[REVISIT]` marking everything code could not settle. Code sources structure; the interview sources intent.
2. [`doc-maturity-auditor`](agents/doc-maturity-auditor.md) — your **punch-list** of open markers per concern.
3. Close the markers → **Workflow 3**.
4. Optional, immediately possible: [`drift-detector`](agents/drift-detector.md) — the bootstrap binding map lets you check code↔doc drift from day one.

**Gate** — a baseline is deliberately **not** build-ready (Sketch/Specified). It hands off to Workflow 3. *(Adopting a regenerated set onto an existing web owes the Part 10f ID-reconciliation step.)*
**See** — STANDARD Part 10f.

## 3. Raise maturity and close open sections

**When** — docs exist (authored or excavated) with open markers or below-target rungs. This is where an excavated baseline's intent gaps get filled.

1. [`doc-maturity-auditor`](agents/doc-maturity-auditor.md) — list every open marker and the rung it blocks. This list **is** your interview agenda.
2. **Resolve each marker** (STANDARD Parts 6, 9) — closed means resolved, not necessarily filled:
   - `[ASSUMPTION]` → **confirm** (clear) or **correct** (edit + clear).
   - `[GAP]` → **fill** the intent, **or** scope it out in Non-goals with its Part 9 kind (`deferred` + a re-entry note / `absent` + the trait justification).
   - `[REVISIT]` → **adjudicate**: *doc-stale* (fix the doc) / *code-defect* (raise in the code tracker — no doc change) / *drop* (dead or wrong-project artifact).
3. [`doc-levelup`](skills/doc-levelup/SKILL.md) per concern — interview-fill the missing intent, author it, wire the ID web, clear the resolved markers. Use the [`concern-specialist`](agents/concern-specialist.md) agent for heavy concerns (threat model, UX, domain). Order dependency-first.
4. Re-run the auditor until build-ready.

**Gate** — every in-scope concern Contract-grade, no open blocking markers.
**See** — STANDARD Parts 3, 4, 6, 9. *(The intent layer — personas, threat model, targets, commercial model, `absent`-vs-`deferred` — is closed by a human, by design: no code artifact carries it.)*

## 4. Ship a feature, doc-first

**When** — add or change a capability on a live doc set (the doc→code direction).

1. [`doc-feature`](skills/doc-feature/SKILL.md) — author the feature **delta** to Contract-grade in the owning concern(s), classify it (emit the `doc-edit` change event), and stub the binding map. *(A request in an external tracker — a **demand-role** item — is a valid intake trigger: it seeds this interview (Part 0.6), never substitutes for it, and is not built until it references a Contract-grade repo ID. Doc↔tracker boundary: Delivery Process 11.6, STANDARD Part 10c.)*
2. [`implementation-planner`](agents/implementation-planner.md) — turn the delta into an **ordered vertical-slice build plan** with code sites, required tests, and the fidelity-staged DoD.
3. **Delivery builds** the slices (human or AI) — not a Dictum tool; the plan is advisory.
4. [`drift-detector`](agents/drift-detector.md) — confirms the loop closed (new bindings resolve, coverage tests pass, staleness clears).

**Gate** — the delta's contracts reach **Verified** (Delivery), staleness cleared.
**See** — STANDARD Part 10e.

## 5. Keep docs true over time

**When** — a contract changes, or code has drifted from the docs (the enhancement lifecycle).

- **A deliberate doc edit** → [`doc-change-impact`](skills/doc-change-impact/SKILL.md) — propagate the change along the ID web (reverse traversal), write cause-attributed staleness, open markers, place tombstones on retirement.
- **Suspected code drift** → [`drift-detector`](agents/drift-detector.md) — emits candidate `drift` change events; **you adjudicate** each: *doc-stale* → hand to `doc-change-impact`; *code-defect* → the code tracker; *divergent* → split.
- **A bug filed in an external tracker** → a **triage-role** item: an externally-sourced, unadjudicated `drift`-type event that stays **repo-invisible until reproduced** (no marker, no staleness before then). On adjudication: *can't-reproduce* → tracker-only; *code-defect* → revoke `Verified` via a regression case, contract text untouched; *doc-defect* → it becomes demand (→ Workflow 4 / `doc-change-impact`). Doc↔tracker boundary: STANDARD Part 10c.

**Gate** — staleness does **not** lower a rung (the verification record stands) but **blocks the release gate** until reconciled or waived.
**See** — STANDARD Part 10d.

## 6. Check maturity and build-readiness

**When** — any time you want the current picture; a read-only checkpoint used inside every other workflow.

- [`doc-maturity-auditor`](agents/doc-maturity-auditor.md) (read-only, never edits) — actual rung vs claimed per concern, gaps to the target rung, dangling references, README↔manifest consistency, and the overall build-ready verdict.

**See** — STANDARD Parts 3, 7.

---

*New to the method? Read [`README.md`](README.md) for the model in one minute, then [`STANDARD.md`](STANDARD.md) for the method; [`GLOSSARY.md`](GLOSSARY.md) defines every term used above, and [`failure-mode-catalog.md`](failure-mode-catalog.md) ties each rule to the real failure it prevents.*
