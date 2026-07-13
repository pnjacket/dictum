---
name: install-dictum
description: Use when installing the Dictum documentation standard and its advisory tooling into another product repo. Copies the five skills and five agents into the target's .claude/, vendors (or references) the standard material, and writes a CLAUDE.md path-resolution pointer so the tools locate the standard unambiguously. On a re-install that vendors a newer standard over an existing doc set, runs the upgrade walk (new sub-aspect keys get an explicit in/out decision). Triggers - "install dictum on <repo>", "set up dictum in this repo", "add the doc tooling to <repo>", "vendor the standard into <repo>", "upgrade dictum in <repo>".
---

# install-dictum

Installs the Dictum tooling and reference material into a **target product repo** so its skills/agents resolve the standard without guessing. Advisory: confirm the target and mode before writing; never overwrite existing files without asking. This skill does the *install* only — it does not scaffold docs (that's `doc-scaffold`, the suggested next step).

## Inputs you rely on
- The **Dictum checkout** (this repo): `skills/` (5 skills), `agents/*.md` (5 agents), and the reference material `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/11.x-*.md`, `templates/`.
- The **target repo** path (from the operator; e.g. a sibling repo).

## Procedure

1. **Confirm the target and inspect it.** Get the target repo path. List it: is it empty, or does it already have a `.claude/skills`, `.claude/agents`, a `dictum/` dir, or a root `CLAUDE.md`? Report what you find. **Never overwrite** existing product files silently — if a collision exists, ask (upgrade in place vs skip vs back up). **If a vendored `dictum/` copy already exists and the operator chooses upgrade-in-place:** before overwriting anything, record the old copy's `STANDARD.md` front-matter `version` and snapshot each old concern spec's published *Sub-aspects* `key` set — the upgrade walk (step 5) diffs against exactly this, and it is gone after the copy.
2. **Choose the reference-material mode** (the one decision that changes the install):
   - **Vendor a copy (default, hermetic).** Copy the standard material into a `dictum/` subdir inside the target. Self-contained and portable; won't drift if the source checkout moves. Preferred — and required for a build that must stay hermetic to its own docs.
   - **Reference the shared checkout.** Point the target at this Dictum checkout's path. No duplication, always current, but the target is coupled to that sibling path existing. Only when the operator explicitly wants a shared source.
3. **Install the tooling** (both modes). Create `.claude/skills/` and `.claude/agents/` in the target and copy:
   - Skills: `doc-scaffold`, `doc-excavate`, `doc-levelup`, `doc-feature`, `doc-change-impact` (copy each skill *directory*).
   - Agents: all of `agents/*.md` — `doc-maturity-auditor`, `code-cartographer`, `drift-detector`, `implementation-planner`, `concern-specialist`.
   - Do **not** copy this `install-dictum` skill into the target — it belongs to the Dictum checkout, not to a product repo (installing it there is the confusion this skill exists to prevent).
4. **Place the reference material.**
   - *Vendor mode:* copy `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/`, and `templates/` into `<target>/dictum/`.
   - *Reference mode:* skip the copy; record the shared checkout's absolute path for step 6.
5. **Upgrade walk (re-vendor over an existing doc set).** Runs whenever the material just placed is a **newer** standard version than what the set was authored against **and** the target already has a doc set (a manifest + concern docs). Detection: when the manifest records the optional `authored_against:` field, compare it to the incoming standard version directly; otherwise, in vendor mode, the old vendored `STANDARD.md` version captured in step 1 is the authored-against proxy; in reference mode, or when no old copy survives, fall back to the symptom — any concern spec key unaccounted for below *is* the detection. Diff each concern's **old→new published sub-aspect `key` set** (Part 9), then **walk every new key with the operator** and record an explicit in/out decision per concern. This is an **interview step, never silent inference** — a new key exists precisely because the older authoring *couldn't* have decided it.
   - **In** → the owning concern doc gains the sub-aspect, usually as a `[GAP]` to fill (the manifest needs no new entry — in-scope is derived as published keys − out-record).
   - **Out** → the concern's `out_of_scope_subaspects` in the manifest gains the key, and the doc's *Non-goals* gains the one-line justification recording its Part 9 kind: `absent` (trait fact justifies; no re-entry note) vs `deferred` (a `[FUTURE-SCOPE]` re-entry note owed).
   - New keys on a concern the manifest holds at `in_scope: false` need no walk — the whole concern is already out. A key merely **renamed** from a form the manifest already records: update the record to the new canonical key (Part 9's near-miss case), no interview needed.
   - **No operator present:** do not decide — an in/out call is a product decision. Record each new key as an undecided `[GAP]` on the owning doc ("new sub-aspect key `<key>` published in v<new>; scope decision pending") and list them all in the report.
   On completing the walk, set/update the manifest's `authored_against:` to the newly vendored standard version (record it even if it was previously absent). Skipping this walk leaves the set silently non-partitioned: the new key sits in neither the out-record nor the in-scope readout, and nothing else forces the decision to surface. The `doc-maturity-auditor`'s **vocabulary re-partition** check reports any key left unaccounted.
6. **Write the path-resolution pointer.** The skills/agents reference `STANDARD.md`, `concerns/11.x`, `templates/`, `GLOSSARY.md`, and `failure-mode-catalog.md` by **bare name**. Add a root `CLAUDE.md` in the target (or a `## Documentation standard (Dictum)` section if one already exists) that states where those bare references resolve — under `dictum/` (vendor mode) or the shared absolute path (reference mode) — and lists the installed skills/agents. This pointer is the glue that makes the layout unambiguous; without it the tools will look for `STANDARD.md` at the repo root and miss.
7. **Report.** List exactly what was created (skills, agents, reference location, `CLAUDE.md`), note anything skipped to avoid overwrite, and — on an upgrade — the walk's outcome (each new key's in/out decision, or the undecided `[GAP]`s left for the operator). State that nothing is committed. Suggest the next step: run **`doc-scaffold`** in the target repo to generate the manifest + doc set (fresh install), or **`doc-maturity-auditor`** to confirm the upgraded set re-partitions cleanly.

## Reference commands (vendor mode)

```
SRC=<dictum-checkout>        # this repo
DST=<target-repo>

mkdir -p "$DST/.claude/skills" "$DST/.claude/agents"
cp -r "$SRC/skills/doc-scaffold" "$SRC/skills/doc-excavate" "$SRC/skills/doc-levelup" \
      "$SRC/skills/doc-feature"  "$SRC/skills/doc-change-impact" "$DST/.claude/skills/"
cp "$SRC/agents/"*.md "$DST/.claude/agents/"

mkdir -p "$DST/dictum"
cp "$SRC/STANDARD.md" "$SRC/GLOSSARY.md" "$SRC/failure-mode-catalog.md" "$DST/dictum/"
cp -r "$SRC/concerns" "$SRC/templates" "$DST/dictum/"
```

Then write `<target>/CLAUDE.md` per step 6.

## Guardrails
- **Confirm the target path first** — an install writes into another repo; get it right before copying.
- **Never overwrite** existing `.claude` tooling, vendored material, or a `CLAUDE.md` without asking; offer back-up/upgrade/skip.
- **Never copy `install-dictum` into the target.** It is a Dictum-checkout tool; a product repo installs *from* Dictum, it does not re-host the installer.
- **Always write the path-resolution pointer** (step 6). Skipping it is the failure this skill prevents — the tools would silently fail to find the standard.
- **Never re-vendor a newer standard over an existing doc set without the upgrade walk** (step 5). A vocabulary addition the walk doesn't surface is a silent partition hole — the scope decision the new key demands never gets made.
- **Don't commit or push.** Leave the install in the target's working tree; the operator commits.
- **Install ≠ scaffold.** Don't start the intake interview or generate docs here; hand off to `doc-scaffold`.
