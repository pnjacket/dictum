<!-- Thanks for contributing to Dictum. Describe your change, then confirm the
     editorial checklist below. Full rules: EDITORIAL.md. -->

## What this changes

<!-- One or two sentences. For a rule change, name the failure it prevents
     (failure-mode-catalog.md) per CONTRIBUTING.md step 1. -->

## Editorial checklist ([EDITORIAL.md](../EDITORIAL.md), Appendix B)

- [ ] **Tier placement** — every addition is a rule (→ standard), rationale (→ `failure-mode-catalog.md`), or evidence (→ `dictum-lab`), in its correct home.
- [ ] **Rule + one-line why** — no normative prose carries more than one clause of rationale; no war-stories ("surfaced building…", "verified in practice"); no research artifacts ("(round N)", "vX.Y bar").
- [ ] **Stands alone** — no new `standard → lab` dependency; the rule is followable without the lab.
- [ ] **Describe by shape** — no real product / company / domain names anywhere in the diff.
- [ ] **Self-exemplifying** — front-matter and structure match; IDs referenced not duplicated; a new owned ID sits on one register line in the Part 5 grammar.
- [ ] **In sync** — a changed rule updates `failure-mode-catalog.md` and keeps `concerns/11.x` ⇄ `STANDARD.md` Part 11 consistent.
- [ ] **Version** — if an editorial rule itself changed, `EDITORIAL.md`'s version is bumped and `RELEASES.md` notes it (with a re-conformance step if a re-sweep is owed).
- [ ] Signed off with `git commit -s` (DCO, per `CONTRIBUTING.md`).
