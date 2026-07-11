---
name: install-dictum
description: Use when installing the Dictum documentation standard and its advisory tooling into another product repo. Copies the five skills and five agents into the target's .claude/, vendors (or references) the standard material, and writes a CLAUDE.md path-resolution pointer so the tools locate the standard unambiguously. Triggers - "install dictum on <repo>", "set up dictum in this repo", "add the doc tooling to <repo>", "vendor the standard into <repo>".
---

# install-dictum

Installs the Dictum tooling and reference material into a **target product repo** so its skills/agents resolve the standard without guessing. Advisory: confirm the target and mode before writing; never overwrite existing files without asking. This skill does the *install* only — it does not scaffold docs (that's `doc-scaffold`, the suggested next step).

## Inputs you rely on
- The **Dictum checkout** (this repo): `skills/` (5 skills), `agents/*.md` (5 agents), and the reference material `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/11.x-*.md`, `templates/`.
- The **target repo** path (from the operator; e.g. a sibling repo).

## Procedure

1. **Confirm the target and inspect it.** Get the target repo path. List it: is it empty, or does it already have a `.claude/skills`, `.claude/agents`, a `dictum/` dir, or a root `CLAUDE.md`? Report what you find. **Never overwrite** existing product files silently — if a collision exists, ask (upgrade in place vs skip vs back up).
2. **Choose the reference-material mode** (the one decision that changes the install):
   - **Vendor a copy (default, hermetic).** Copy the standard material into a `dictum/` subdir inside the target. Self-contained and portable; won't drift if the source checkout moves. Preferred — and required for a build that must stay hermetic to its own docs.
   - **Reference the shared checkout.** Point the target at this Dictum checkout's path. No duplication, always current, but the target is coupled to that sibling path existing. Only when the operator explicitly wants a shared source.
3. **Install the tooling** (both modes). Create `.claude/skills/` and `.claude/agents/` in the target and copy:
   - Skills: `doc-scaffold`, `doc-excavate`, `doc-levelup`, `doc-feature`, `doc-change-impact` (copy each skill *directory*).
   - Agents: all of `agents/*.md` — `doc-maturity-auditor`, `code-cartographer`, `drift-detector`, `implementation-planner`, `concern-specialist`.
   - Do **not** copy this `install-dictum` skill into the target — it belongs to the Dictum checkout, not to a product repo (installing it there is the confusion this skill exists to prevent).
4. **Place the reference material.**
   - *Vendor mode:* copy `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/`, and `templates/` into `<target>/dictum/`.
   - *Reference mode:* skip the copy; record the shared checkout's absolute path for step 5.
5. **Write the path-resolution pointer.** The skills/agents reference `STANDARD.md`, `concerns/11.x`, `templates/`, `GLOSSARY.md`, and `failure-mode-catalog.md` by **bare name**. Add a root `CLAUDE.md` in the target (or a `## Documentation standard (Dictum)` section if one already exists) that states where those bare references resolve — under `dictum/` (vendor mode) or the shared absolute path (reference mode) — and lists the installed skills/agents. This pointer is the glue that makes the layout unambiguous; without it the tools will look for `STANDARD.md` at the repo root and miss.
6. **Report.** List exactly what was created (skills, agents, reference location, `CLAUDE.md`), note anything skipped to avoid overwrite, and state that nothing is committed. Suggest the next step: run **`doc-scaffold`** in the target repo to generate the manifest + doc set.

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

Then write `<target>/CLAUDE.md` per step 5.

## Guardrails
- **Confirm the target path first** — an install writes into another repo; get it right before copying.
- **Never overwrite** existing `.claude` tooling, vendored material, or a `CLAUDE.md` without asking; offer back-up/upgrade/skip.
- **Never copy `install-dictum` into the target.** It is a Dictum-checkout tool; a product repo installs *from* Dictum, it does not re-host the installer.
- **Always write the path-resolution pointer** (step 5). Skipping it is the failure this skill prevents — the tools would silently fail to find the standard.
- **Don't commit or push.** Leave the install in the target's working tree; the operator commits.
- **Install ≠ scaffold.** Don't start the intake interview or generate docs here; hand off to `doc-scaffold`.
