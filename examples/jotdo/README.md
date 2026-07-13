# jotdo — a worked Dictum example

A tiny single-user task-list CLI that persists to a local JSON file, together
with its complete, published Dictum doc set. This is the standard's **CLI
validation product** — one of the deliberately different products built to
validate the method end-to-end — folded in here, trimmed and renamed, as the
first worked provenance example.

```
jotdo add "buy milk"     # added #1
jotdo list               # [ ] #1 buy milk
jotdo done 1             # done #1
jotdo rm 1               # removed #1
```

Store location: `$JOTDO_FILE` (default `~/.jotdo.json`).

## What it demonstrates

- A **minimal conforming doc set** at the small end of the spectrum:
  single-file packaging (STANDARD Part 8) over a ~150-line product, all six
  core concerns plus the two baselines — Product & Requirements,
  Domain & Data, Architecture, Interfaces & Contracts, Quality & Testing,
  Delivery Process, Security & Privacy, Governance & Compliance — at
  Contract-grade, with the module concerns scoped out by trait.
- **Scope as the only calibration lever**: the manifest records every
  scoped-out sub-aspect key, and each concern's Non-goals records the kind
  (`absent` vs `deferred`) with its justification (Part 9).
- The **owned-once ID web**: every contract minted once
  (`CAP-… ENTITY-… INV-… COMPONENT-… CLI-… SEC-…`), referenced by stable ID.
- A **resolvable contract→code binding map** (`bindings.yaml`, Part 10d),
  including runnable `asserted_by` selectors for the invariants, plus the
  `DICT: <ID>` in-code annotations at each realizing site.
- The **gate-bound publish step** (Part 6): the set is `status: published`,
  build markers stripped, versioned.

## Layout

| File | Role |
|---|---|
| `docs/SPEC.md` | The doc set — single-file spec, all in-scope concerns |
| `manifest.yaml` | Product-profile manifest: traits, scope, rungs (Part 7) |
| `bindings.yaml` | Contract→code binding map (Part 10d) |
| `jotdo.py` | The product (~150 lines, Python 3 stdlib only) |
| `test_jotdo.py` | The coverage-map test suite |

## Develop

```
python3 -m unittest      # run the test suite (from this directory)
```

## Status

Illustrative, not normative: **the standard's text (`../../STANDARD.md`) is
the only definition of conformance.** The product name and identifiers here
are generic placeholders; the doc content is the real authored set from the
validation build, adapted to the standard's current vocabulary.
