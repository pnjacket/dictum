---
artifact: documentation-standard
role: roadmap
status: published
version: 1.0.0
---

# Dictum — Open Items

The core standard is complete and validation-hardened (Parts 0–13, the full enhancement lifecycle + the doc-led implementation flow + the reverse-authoring/brownfield bootstrap (Part 10f), the advisory tool suite of 5 skills + 5 agents, and the doc↔tracker boundary (Part 10c); `v1.0.0`). **Nothing below is blocking** — these are deferred or future items, recorded here so they live in the repo rather than only in a maintainer's notes. Each points at where it is already referenced.

## Housekeeping

- **Worked example not published.** The CLI validation product lives only as a local repo. Optionally publish it, or fold a trimmed copy into this repo, as the standard's first real provenance example.

## Parked design topics

- **Design-system binding** `[REVISIT]` — the sole entry in STANDARD *Parked Topics*; informs User Experience (11.9). **Blocked on external input (design-tool access);** an interim component-reuse rule stands in. See `concerns/11.9-user-experience.md`.
- **Cross-product / platform federation of the reverse index** — the multi-doc-set version of the enhancement lifecycle (an ID owned in product A's doc set, referenced by product B). Noted as out-of-scope-for-now in STANDARD **Part 10d**; a real design effort when platform scale is needed.

## Future tooling

- **Model B drift-detector** `[FUTURE-SCOPE]` — a deterministic, CI-gradeable detector (per-stack extractors, or comparison against build-emitted OpenAPI/JSON-schema), versus the built advisory **model A** agent (`agents/drift-detector.md`). Pursue only if drift must be a hard CI gate. Referenced in STANDARD Part 10d and `agents/drift-detector.md`.
- **Deterministic reverse-extraction for `code-cartographer`** `[FUTURE-SCOPE]` — the built agent (Part 10f) is advisory model-A LLM extraction; per-stack AST/route/schema extractors could make the contract inventory + draft binding map deterministic. Shares the model-B question with the drift-detector (the two agents could share one code-mapping backend). Pursue only if reverse-authoring must be repeatable/CI-gradeable.
- **Live doc↔tracker sync tooling** `[FUTURE-SCOPE]` — an adapter that projects the derived backlog (10e) + build-status (11.6) into an external tracker (GitHub Issues / Jira / Azure DevOps) as execution items and reconciles status **repo-wins**. The standard defines the *boundary* — the **execution mirror**, declared by the product-local **tracker-binding declaration** (11.6, STANDARD Part 10c: downstream-mirror invariant, three item roles, two gates); only the sync tooling is deferred. Pursue when a product wants its tracker kept in lockstep with the repo automatically rather than by hand.

## Reverse-authoring vocabulary extensions (from the Part 10f generalization validation)

The reverse-authoring flow was validated read-only across a **diverse set of existing real-world codebases** spanning Go, TypeScript, React/Angular, Rust, and C#/.NET (including one with companion device firmware) — all mapped cleanly; the core BREADTH×DEPTH model + ID web held on every one. Low-risk extraction-guidance clarifications were folded into `code-cartographer` directly; these **larger vocabulary/machinery changes** are parked because each is a real design decision, not a guidance tweak. Each is described by the **product shape** that surfaced it, not by any specific project:

- **Embedded/hardware surface** — a first-class `firmware`/`embedded` interface-kind + a hardware-boundary contract kind (a pin↔logical-input map, a HID report format, a bill of materials). Surfaced by a desktop input-mapping tool with companion device firmware and a printed enclosure. Interim: scoped out honestly (STANDARD Part 10f scope-boundary note).
- **Cross-language dual-realization binding** — a binding-map schema extension for one logical contract realized in two languages (a backend DTO class + a hand-written front-end interface) bridged by a serialization convention: **producer + consumer locators** per contract plus an explicit **wire-serialization sub-contract** (casing/enum/date), so full-stack DTO drift is checkable. Surfaced by a typed-backend + typed-SPA full-stack app with observed type-name drift across the two languages; any full-stack app with a shared-types package is adjacent.
- **`CONFIG-###` / committed-config-key contract kind** — behavior-shaping env/config keys that drive real invariants (a retention cutoff, a cleanup cadence) currently land under `ENV-###` as prose. Surfaced by a small full-stack app whose env keys drive its retention/cleanup behavior.
- **Output-serialization-schema contract kind** — for report-emitting tools whose load-bearing contract is the emitted JSON/Markdown shape, not a persisted entity. Surfaced by a static-analysis CLI/library that emits a report.
- **A LEAN cartographer/excavate tier** — the full 15-concern sweep + separate binding-map artifact is over-scaled for a tiny single-interface repo (a ~200-line CLI); a proportionate tier would report only concerns with code evidence + the must-interview shortlist.
- **Per-app trait sub-blocks** — a multi-plane monorepo (several backend services + multiple SPAs/workers, or N language modules) has genuinely different security/role/interface surfaces under one trait read. Surfaced by multi-app monorepos.

## Standard-upgrade migration (from auditing v0.12-era doc sets against v1.0.0)

- **Vocabulary additions create silent partition holes on upgrade.** When a newer standard version publishes a *new* sub-aspect key on a concern (as Part 10c did with `external-tracker-binding` on 11.6), every existing doc set authored against the older vocabulary is silently non-partitioned: the new key appears in neither the manifest's `out_of_scope_subaspects` nor the doc's `in-scope-subaspects` readout, so the scope decision the key demands was never made — and nothing in the method forces it to surface. Observed on all three older doc sets audited after the v1.0.0 re-vendor; in each, the new key's trigger actually fired. Candidate fixes: an **upgrade re-partition check** (the `doc-maturity-auditor` diffs each concern's published key set against the manifest-era vocabulary and reports unaccounted keys — it already catches this incidentally; make it a named check), and/or a **standard-upgrade step** in `install-dictum`/`doc-levelup` that walks new keys and records an explicit in/out decision per concern. Related: new-key additions should be called out in release notes (`RELEASES.md`) as requiring a re-partition.

## Minor open findings (from the real-time messaging build, non-blocking)

- **Send-to-unjoined-public-channel behavior** — the disclosure rule (a public channel a member hasn't joined is *visible*) vs. the membership rule (`INV-MESSAGE-MEMBER` requires the author be a conversation member at send) leave "post to a public channel you haven't joined" undefined (auto-join vs reject). Pin it in Interfaces/Domain. Minor.
- **Observability worked-example at the "alerting in-scope" end** — the existing example is single-SLO; a richer alert-rule authoring example would help real-time products. Deferred.
