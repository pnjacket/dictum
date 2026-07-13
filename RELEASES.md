# Dictum — Releases & Provenance

There is one authoritative Dictum standard. Because the text is CC BY 4.0
(freely shareable *and* adaptable), the guarantee that a given copy **is** the
official standard does not come from copyright — it comes from **where a release
is published** and a **verifiable signature/checksum** on it.

## What "Dictum v*X*" means

"Dictum" + a version identifier (e.g. *Dictum v1.0.0*) denotes the exact
text published for that version **from the canonical repository**. Any other
copy — an adaptation, a translation, a fork — is permitted by the license but is
**not** "Dictum v*X*" unless it is that official release, byte-for-byte.

The tip of `main` is a **working state, not a release**: the version numbers its
files carry (front-matter `version:` fields, the README status line) may be
ahead of — or wrong relative to — any released version. Only a **signed release
tag and the commit it points to** authoritatively carry a version.

## How authenticity is established

Each tagged release is:

1. **Published from the canonical repository** as an annotated, **signed git tag**
   (`git tag -s vX.Y.Z`), so the tag's provenance is cryptographically verifiable.
2. Accompanied by a **`SHA256SUMS`** manifest covering the normative files
   (`STANDARD.md`, `GLOSSARY.md`, `failure-mode-catalog.md`, `concerns/`), so any
   copy can be checked against the official hashes.

To verify a copy that claims to be Dictum v*X*:

```sh
gpg --import dictum-signing-key.asc   # once — the key is in this repo and on each release
git verify-tag vX.Y.Z                 # confirms the signed tag
sha256sum -c SHA256SUMS               # confirms the files match the release
```

A copy that fails either check is not the authentic standard, whatever it is named.

## Versioning policy

Version numbers follow semantic versioning, calibrated to what a bump means for an
**existing conforming doc set**:

- **MAJOR** — the core model changes in a way that can invalidate previously
  conforming doc sets with no mechanical repair: the two axes, the rung ladder or
  its semantics, owned-once/ID stability, or removing/renaming a published
  sub-aspect key or a rung.
- **MINOR** — an **additive method change**: a new Part, a new published sub-aspect
  key, a new or tightened bar or gate — where an existing conforming set can be
  brought back to conformance by a bounded, mechanical step. **The release notes
  must name that re-conformance step** (e.g. *"new published key `K` on concern
  `C`: record an in/out scope decision"*; *"the build-ready gate now includes the
  publish step: run it"*). A vocabulary or gate addition shipped without its named
  step is how an upgrade silently strands existing doc sets.
- **PATCH** — editorial or clarifying changes only; no bar, gate, or vocabulary
  change.

## Release notes

### v1.1.0 — MINOR

An additive method release. Per the policy above, each addition names the
re-conformance step it asks of an existing conforming doc set.

- **Gate-bound publish step** (STANDARD Part 6/10/10e; failure-mode #30) — the
  build-ready gate hands off a *published* set; an enhancement delta re-publishes
  at its hand-off, before the build it authorizes; implementation events never
  touch `status:`. The `doc-maturity-auditor` detects status↔claim inconsistency
  from implementation evidence. *Re-conformance:* a set already claiming
  build-ready (or demonstrably built) runs the publish step — strip build
  markers, flip `status: published`, bump the doc version; a set not yet at the
  gate owes nothing now.
- **Versioning policy** (this file) — MAJOR/MINOR/PATCH calibrated to impact on
  existing conforming sets; MINOR notes must name each addition's re-conformance
  step. *Re-conformance:* none (it binds future releases, starting with this
  entry).
- **Register-form ID minting bar** (STANDARD Part 5) — an owned ID is minted on
  exactly one register line of the stated form; every other occurrence is a
  non-minting reference. *Re-conformance:* verify the set's register lines parse
  to the stated form — sets authored from the templates already do; an owned ID
  defined only in free prose moves onto a register line.
- **New contract kinds `CONFIG-###`** (committed-config key, Operations 11.10)
  **and `OUT-###`** (output-document schema, Interfaces 11.4). No new published
  sub-aspect key — both live under existing keys (`runtime-configuration`; the
  interface-surface kinds). *Re-conformance:* optional migration — where a set
  states a behavior-shaping config key or an emitted-document shape as prose,
  mint it under the new kind; no action if none.
- **Dual-realization binding extension** (`templates/binding-map.template.md`;
  STANDARD Part 10d; failure-mode #31) — optional producer/consumer locators plus
  a wire-serialization sub-contract for one contract realized in two languages.
  *Re-conformance:* none (optional; existing single-realization bindings remain
  conforming).
- **Marker-token grammar fix** (STANDARD Part 10f) — the `DICT: <ID>` token
  grammar clarified. *Re-conformance:* none — existing `// DICT:` annotations
  remain conforming.
- **Vocabulary re-partition check + upgrade walk** (`doc-maturity-auditor`;
  `install-dictum` re-vendor path / `doc-levelup`; failure-mode #32) — every
  published sub-aspect key of every in-scope concern must be accounted for in the
  set's recorded partition, and a standard upgrade records an explicit in/out
  decision per new key. *Re-conformance:* none for current sets — the check and
  the walk run on the next audit/upgrade, and this release adds no new published
  key.
- **Optional manifest field `authored_against:`**
  (`templates/manifest.template.md`) — the standard version a set was authored
  (or last re-partitioned) against; when present, the vocabulary re-partition
  check attributes partition holes to the version delta and the upgrade walk
  updates it. *Re-conformance:* optional — recommended on the set's next touch;
  absent, the check and walk still run, without version attribution.
- **Alert rules are complete routing rows** (Observability 11.11, bar + second
  worked example) — an in-scope alert rule carries the guarded `SLO-###`,
  trigger (threshold + window or burn rate), severity, a `ROLE-###` target
  (never a person), and a `RUNBOOK-###` response. *Re-conformance:* only sets
  with `alerting-rules` in scope — complete each existing alert rule to a full
  routing row; sets with alerting scoped out owe nothing.
- **LEAN cartographer/excavate tier** (STANDARD Part 10f; `code-cartographer`;
  `doc-excavate`) — a proportionate reporting/interview mode for tiny
  single-interface repos: full detail only for concerns with code evidence plus
  the must-interview shortlist, landing on the single-file form. Same
  vocabulary, same partition, same gates — deliberately not a vocabulary
  change (core stays six concerns), and never a code-first license.
  *Re-conformance:* none (advisory-tool behavior).
- **Worked example + extension-point reframing** (`examples/`; STANDARD Parts
  5/10d/10f) — a published worked example, and the machine-extraction extension
  points named as such (register lines; the in-code marker token).
  *Re-conformance:* none (illustrative/editorial).
- **Adjudicated to stay out of the standard** (recorded here so the decisions
  are citable): a machine-readable route/field convention on API registers, and
  a pinned tracker-binding declaration shape (11.6) — the standard binds to a
  form only where there is one way; both remain suggested conventions
  demonstrated non-normatively in the research companion. *Re-conformance:*
  none.

## The signing key

Releases are signed with:

```
David H. Jung (Dictum signing key) <pnjacket@msn.com>
ed25519  fingerprint  2CF3 8F61 49CA 7925 2A0B  6DD9 5394 C856 2397 2DCF
```

The public key is committed at [`dictum-signing-key.asc`](dictum-signing-key.asc)
and attached to every release. Verify the fingerprint above against a second
source (the release page) before trusting an imported copy — a key shipped in the
same repository it authenticates only proves internal consistency.

## Relationship to the other policies

- **License** ([`LICENSE`](LICENSE)) — CC BY 4.0 lets anyone share/adapt the text.
- **Name** ([`TRADEMARK.md`](TRADEMARK.md)) — a first-mover naming convention asking
  that adaptations not call themselves "Dictum" (no registered trademark).
- **Provenance** (this file) — lets anyone *verify* which copy is the official one.

Together these deliver "one authoritative version" without restricting reuse.
