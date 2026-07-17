---
artifact: documentation-standard
role: roadmap
status: published
version: 1.1.0
---

# Dictum — Open Items

The core standard is complete and validation-hardened (Parts 0–13, the full enhancement lifecycle + the doc-led implementation flow + the reverse-authoring/brownfield bootstrap (Part 10f), the advisory tool suite of 6 skills + 5 agents, the doc↔tracker boundary (Part 10c), and a worked example at [`examples/`](examples/); `v1.1.0` — see [`RELEASES.md`](RELEASES.md) for the full release notes). **Nothing below is blocking** — these are deferred design items, recorded here so they live in the repo rather than only in a maintainer's notes.

## Parked design topics

- **Cross-repo doc-set linking & federation.** Two converging needs, one design effort. (1) The multi-doc-set version of the enhancement lifecycle — an ID owned in product A's doc set, referenced by product B; noted as out-of-scope-for-now in STANDARD **Part 10d**. (2) **Linked doc sets for multi-repo systems**: a repo that is one part of a really large system often cannot explain itself in isolation, because its use cases are defined by the downstream apps/services that consume it — so a doc set needs a first-class way to declare that its capabilities serve another set's capabilities, across repo boundaries, with the reference web (and change-impact traversal) following the link. A real design effort when platform scale is needed; pairs with the per-app trait sub-blocks item below (sub-division *within* a repo; linking *across* repos).

## Reverse-authoring vocabulary extensions (from the Part 10f generalization validation)

The reverse-authoring flow was validated read-only across a diverse set of existing real-world codebases spanning Go, TypeScript, React/Angular, Rust, and C#/.NET (including one with companion device firmware) — all mapped cleanly; the core BREADTH×DEPTH model + ID web held on every one. The smaller extensions this surfaced (`CONFIG-###`, `OUT-###`, dual-realization bindings, and the LEAN cartographer/excavate tier — a ceremony-proportionality mode, deliberately *not* a vocabulary change: core stays six) were folded in at `v1.1.0`; these remain open, each described by the **product shape** that surfaced it, never by a specific project:

- **Embedded/hardware surface** — **revisit soon.** A first-class `firmware`/`embedded` interface-kind + a hardware-boundary contract kind (a pin↔logical-input map, a HID report format, a bill of materials). Surfaced by a desktop input-mapping tool with companion device firmware and a printed enclosure. A *generalized* hardware-interface treatment is judged necessary — there are too many kinds of hardware boundary for one-off modeling — but the shape of that generalization is the open design question. Interim: scoped out honestly (STANDARD Part 10f scope-boundary note).
- **Per-app trait sub-blocks** — a multi-plane monorepo (several backend services + multiple SPAs/workers, or N language modules) has genuinely different security/role/interface surfaces under one trait read. Surfaced by multi-app monorepos. Pairs with the cross-repo linking item above.
