---
artifact: documentation-standard
role: standard
status: published
version: 1.0.0
---

# Claude Code Tooling

Portable, **advisory** skills and agents that operationalize the [Documentation Standard](../STANDARD.md). They assist — they never block.

| Tool | Kind | Purpose |
|---|---|---|
| `install-dictum` | skill | Install the tooling + standard material into a target product repo (vendored or shared), with the CLAUDE.md path pointer. Runs *in this checkout*, not in a product repo. |
| `doc-scaffold` | skill | Greenfield: intake interview → product-profile manifest → generated doc set. |
| `doc-excavate` | skill | Brownfield: reverse-map an existing undocumented repo → manifest + doc set + binding map, via the cartographer + a confirm-and-fill interview (Part 10f). |
| `doc-levelup` | skill | Raise one concern's doc to its next maturity rung (depth). |
| `doc-feature` | skill | Author a feature *delta* into the owning concern(s) to Contract-grade, classify it, emit the `doc-edit` event, stub the binding map — the doc-led forward flow (Part 10e). |
| `doc-change-impact` | skill | Propagate a contract change along the ID web (Part 10d): impact set, cause-attributed staleness, markers, tombstones. |
| `report-failure-mode` | skill | Contribution path: when a product built to Dictum hits a failure the standard didn't prevent, distill it into a describe-by-shape failure-mode report (Observed failure · Root cause · Preventing mechanism · draft catalog row) for the maintainer. Writes to the product's scratch; never edits the standard. |
| `doc-maturity-auditor` | agent (read-only) | Report each concern's rung vs actual section completeness; list gaps; check build-readiness + README↔manifest consistency. |
| `code-cartographer` | agent (read-only) | Reverse-map an existing repo → candidate contracts + draft binding map + recoverability report; the Part 10f bootstrap that feeds `doc-excavate`. |
| `drift-detector` | agent (read-only) | Detect code→doc drift via the binding map; emit candidate `source: drift` change events for adjudication (Part 10d, model A). |
| `implementation-planner` | agent (read-only) | Turn a doc-led change (doc-edit events / doc diff) into an ordered vertical-slice build plan — the doc→code forward counterpart to the drift-detector (Part 10e). |
| `concern-specialist` | agent | Deep authoring/review for one heavy concern (parameterized). |

## Install (per product repo)

Use the **`install-dictum`** skill (run it from this Dictum checkout, targeting the product repo). It copies the six skills + five agents into the target's `.claude/`, vendors (or references) the standard material, and writes the `CLAUDE.md` path pointer so bare references to `STANDARD.md` / `concerns/11.x` / `templates/` resolve. The equivalent manual steps:

```
cp -r dictum/skills/doc-scaffold        .claude/skills/
cp -r dictum/skills/doc-excavate        .claude/skills/
cp -r dictum/skills/doc-levelup         .claude/skills/
cp -r dictum/skills/doc-feature         .claude/skills/
cp -r dictum/skills/doc-change-impact   .claude/skills/
cp -r dictum/skills/report-failure-mode .claude/skills/
cp dictum/agents/*.md                   .claude/agents/
```

(`install-dictum` itself is *not* copied into the product repo — it belongs to the Dictum checkout.) The tools locate the standard (`STANDARD.md`), concern specs (`concerns/11.x`), and templates from the Dictum checkout (vendored into the product repo, or referenced from a shared location); the target's `CLAUDE.md` records which. All edits are confirmed; the auditor is strictly read-only.
