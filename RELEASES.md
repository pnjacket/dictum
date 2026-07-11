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
