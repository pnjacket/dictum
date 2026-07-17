# Contributing to Dictum

Thanks for wanting to improve Dictum. Contributions are welcome — corrections,
sharper wording, new worked examples, translations, and improvements to the
tooling.

How a contribution is **licensed** depends on *what you are changing*, because the
repository is licensed in two parts (see [`LICENSE`](LICENSE)) — but both zones
are simple: **inbound = outbound**.

## The two zones

| You are editing… | Licensed under… | What contributing means |
|---|---|---|
| The **standard's prose** — `STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/`, project docs | **CC BY 4.0** | Your contribution is accepted under the same CC BY 4.0 (inbound = outbound). |
| The **tooling and templates** — `skills/`, `agents/`, `templates/` | **MIT** | Your contribution is accepted under MIT (inbound = outbound). |

You **keep the copyright** in your contributions in both zones. There is no
copyright assignment and no separate inbound license grant: CC BY and MIT are
both permissive, so "same license as the project" is all the project needs to
incorporate and publish your change as part of the canonical standard.

## Translations

Translations are especially welcome, and are the adaptation the project wants to
carry under the Dictum name. Because CC BY lets anyone translate the text, the
way we keep **one authoritative version per language** is to bring official
translations *through this process* and publish them from the canonical
repository. Open an issue proposing a translation before starting a large one so
effort isn't duplicated. (An unofficial translation is allowed by the license but
may not use the Dictum name — see [`TRADEMARK.md`](TRADEMARK.md).)

## Sign-off: the Developer Certificate of Origin

Every commit must be signed off, certifying you have the right to submit it under
the license of the files you changed. Add the sign-off with `git commit -s`,
which appends a line:

```
Signed-off-by: Your Name <you@example.com>
```

Use your real name and a real email. The sign-off certifies the Developer
Certificate of Origin, version 1.1, reproduced below.

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## How to contribute

1. Open an issue first for anything substantive (a bar change, a new rule, a
   structural edit, a translation) so the direction can be agreed before you
   invest in it. Dictum's rules are tied to real failures — see
   [`failure-mode-catalog.md`](failure-mode-catalog.md) — so a change to a rule
   should say which failure it prevents.
2. Follow the **[Editorial Charter](EDITORIAL.md)** — the rules for how the
   standard's own text is authored: the three-tier split (rule → standard ·
   rationale → catalog · evidence → the lab), rule-plus-one-line-why, no
   war-stories in normative prose, and describe-by-shape. Its Appendix B is the
   PR checklist your change is reviewed against.
3. Keep docs **self-exemplifying**: match the existing front-matter and
   document-contract structure. If you change a rule, keep
   `failure-mode-catalog.md` and the relevant *Design Decisions* in sync, and
   keep `concerns/11.x` consistent with `STANDARD.md` Part 11.
4. Reference contracts by ID; never duplicate a contract another concern owns.
5. Commit with `git commit -s` and open a pull request.

## Reporting a failure mode

The strongest contributions come from **real builds** — a failure the standard
did not prevent. Every rule in Dictum traces to an observed failure
([`failure-mode-catalog.md`](failure-mode-catalog.md)), and that catalog grows
from reports like yours.

1. If you can, run the **`report-failure-mode`** skill (installed with the Dictum
   tooling). It interviews you and produces a structured report — observed
   failure, root cause, a proposed preventing mechanism, and a draft catalog row
   — with the describe-by-shape scrub already applied.
2. File it as a new issue using the **Failure-mode report** template; the form
   mirrors that shape.

**Describe by shape — this is load-bearing, and for the maintainer it is legal.**
The tracker is public and a filed issue is effectively permanent. Name **no**
real product, company, or person, and **no** domain-identifying specifics
(function / entity / field names, regulated-domain terms) — describe the product
only by its shape, and **keep concrete evidence in your own repo**. The issue
form requires you to confirm this before it can be filed; the maintainer also
scans on triage, but the first responsibility is the submitter's. (This is
[`EDITORIAL.md`](EDITORIAL.md) Part 3 applied at the public boundary.)

**What happens next.** A report is a *hypothesis*, not a change — nothing you
file alters the standard until the maintainer **adjudicates** it (the same
triage-then-write discipline the standard applies to external trackers, Part
10c). If it is accepted, the distilled rule lands as a **catalog entry** and
ships in a **versioned release** with a named re-conformance step — which your
own doc set then picks up through the upgrade walk. Executable detectors, where
warranted, live non-normatively in the research companion (`dictum-lab`), never
in the standard.

## Questions

Open an issue. For anything about the name or conformance claims, see
[`TRADEMARK.md`](TRADEMARK.md).
