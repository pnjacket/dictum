---
artifact: product-doc
role: single-file-spec
product: jotdo
status: published
version: 1.0.0
# Per-concern rung tracking lives in manifest.yaml; this file holds the content.
---

# jotdo — Specification

> A tiny single-user task-list CLI that persists tasks to a local JSON file.
> Single-file Dictum doc set (STANDARD Part 8 packaging); contracts are owned here and realized in code per `../bindings.yaml`.

## 1. Product & Requirements

**Problem.** A user wants to track short-lived to-do items from the terminal without a heavier tool.

**Persona.**
- `PERSONA-USER` — a single person on their own machine, comfortable in a shell.

**Success criteria (measurable).**
- `SUCCESS-ROUNDTRIP` — a task added in one invocation is present in the next `list`.
- `SUCCESS-STABLE-IDS` — a task's id never changes and is never reused for a different task.

**Capabilities.**
- `CAP-ADD` — add a task by title.
- `CAP-LIST` — list all tasks with their state.
- `CAP-DONE` — mark a task done by id.
- `CAP-REMOVE` — remove a task by id.

**Constraints.** Python 3 standard library only — no third-party dependencies; a single source file.

**Non-goals.** Multi-user/sync; due dates, priorities, tags; editing a title; undo; concurrent access from multiple processes.
*Scoped out (kind: absent — see manifest):* market/competitive context, stakeholders, risks — a personal-scale tool with a single author-operator has none of these subjects.

## 2. Domain & Data

**Entities.**
- `ENTITY-TASK` — one to-do item.
  | field | type | notes |
  |---|---|---|
  | `id` | int | identity; assigned by the store |
  | `title` | str | free text, non-empty |
  | `done` | bool | completion state |
  | `created` | str | ISO-8601 UTC timestamp |
- `ENTITY-STORE` — the persisted collection.
  | field | type | notes |
  |---|---|---|
  | `seq` | int | highest id ever issued (monotonic counter) |
  | `tasks` | list\<`ENTITY-TASK`\> | current tasks |

**Invariants (checkable).**
- `INV-TASK-ID-UNIQUE` — no two tasks in a store share an `id`.
- `INV-TASK-ID-MONOTONIC` — a new task's `id` is strictly greater than every id ever issued; ids are never reused, even after a removal.

**Lifecycle.** A task is created open (`done=false`), may be marked done, and exists until removed; removal is permanent (no undo — see Non-goals §1).

**Classification.** No sensitive data; titles are user-authored free text with no protection requirement.

**Storage.** A single JSON object `{ "seq": int, "tasks": [...] }` at `$JOTDO_FILE` (default `~/.jotdo.json`). Created on first write.

**Non-goals.**
- *Migrations & versioning (kind: deferred):* the store format is frozen at v1. [FUTURE-SCOPE] If the store format ever changes, migrations re-enter scope.
- *Consistency & transactions (kind: absent):* single process, single writer — concurrent access is a product non-goal (§1); each command rewrites the whole store.
- *Reference / seed data (kind: absent):* there is none; every store starts empty.

## 3. Architecture

**Components.**
- `COMPONENT-CLI` — argument parsing + command dispatch + output (`jotdo.py`).
- `COMPONENT-STORE` — load/serialize the `ENTITY-STORE` to/from JSON, and own the `seq` counter (`jotdo.py`: `Store`, `load`, `save`).

**Technology.** Python 3, standard library only (see `ADR-JSON-FILE` and the §1 constraint).

**Decisions.**
- `ADR-MONOTONIC-SEQ` — the store carries a persisted `seq` rather than computing `max(id)+1`, so ids stay monotonic across removals (satisfies `INV-TASK-ID-MONOTONIC`).
- `ADR-JSON-FILE` — a flat JSON file (no DB) keeps the tool dependency-free and the store human-readable.

**Non-goals** *(kind: absent — see manifest)*: boundaries/isolation model, cross-cutting patterns, deployment topology, scalability/resilience patterns — a two-component single-process script has none of these subjects.

## 4. Interfaces & Contracts

CLI interface kind. Each command is owned by `COMPONENT-CLI`, reads/writes via `COMPONENT-STORE`, and exchanges `ENTITY-TASK` data.

- `CLI-ADD` — serves `CAP-ADD`.
  - **Invocation:** `jotdo add <title>`
  - **Effect:** appends a new `ENTITY-TASK` (`done=false`, fresh monotonic `id`).
  - **Output:** `added #<id>` to stdout; exit `0`.
- `CLI-LIST` — serves `CAP-LIST`.
  - **Invocation:** `jotdo list`
  - **Output:** one line per task `"<box> #<id> <title>"` where box is `[x]` if done else `[ ]`; `(no tasks)` if empty. Exit `0`.
- `CLI-DONE` — serves `CAP-DONE`.
  - **Invocation:** `jotdo done <id>` (`id`: int)
  - **Effect:** sets `done=true` for that task.
  - **Output:** `done #<id>`, exit `0`. **Error:** unknown id → `no task #<id>` to stderr, exit `1`.
- `CLI-RM` — serves `CAP-REMOVE`.
  - **Invocation:** `jotdo rm <id>` (`id`: int)
  - **Effect:** removes that task; `seq` is unchanged (monotonic).
  - **Output:** `removed #<id>`, exit `0`. **Error:** unknown id → `no task #<id>` to stderr, exit `1`.

**Error model.** Two outcomes per command: success (message to stdout, exit `0`) or unknown-id (`no task #<id>` to stderr, exit `1`); malformed usage is argparse's own usage error (exit `2`). No further error catalog is needed at this surface.

**Non-goals** *(kind: absent — see manifest)*: HTTP/RPC, library/SDK, event, and UI surfaces — the CLI is the only interface; versioning/compatibility and pagination/filtering/rate-limit conventions — a local single-user tool has no exposure surface to version or throttle.

## 5. Quality & Testing

**Test types.** One layer: CLI-level tests through the real entrypoint (below), plus direct store-level assertions for the two invariants. The product is small enough that this single layer is the whole pyramid.

**Coverage map** (every CAP/INV/CLI/SEC maps to an observable check; one invariant per test):
| Contract | Check |
|---|---|
| `CAP-ADD` / `CLI-ADD` | `test_add_and_list` |
| `CAP-LIST` / `CLI-LIST` | `test_add_and_list` |
| `CAP-DONE` / `CLI-DONE` | `test_done` |
| `CAP-REMOVE` / `CLI-RM` | `test_remove` |
| `INV-TASK-ID-UNIQUE` | `test_ids_unique` |
| `INV-TASK-ID-MONOTONIC` | `test_ids_monotonic` |
| `SEC-LOCAL-ONLY` | `test_local_only` |

- `E2E-STANDARD` — tests drive the real CLI entrypoint (`jotdo.main`) against a real temp JSON store — own code is never bypassed. No external dependencies to substitute.

**Quality bar.** `python3 -m unittest` is green; every contract above has a passing check.

**Test data.** Each test uses a fresh temp `JOTDO_FILE`; no shared state.

**Non-goals** *(kind: absent — see manifest)*: specialized (perf/security/a11y) testing — no trait activates it; test-stage/fidelity mapping — one environment, merge and release fidelity coincide (§6); manual/exploratory testing.

## 6. Delivery Process

**Slice rule.** A capability ships as a vertical slice: its `CLI-*` contract + `COMPONENT` wiring + a test in the coverage map. Work items are the slices themselves — no external tracker (see manifest); git history is the record.

**Definition of Done (fidelity-staged).**
- **Merge gate:** `python3 -m unittest` green at the highest local fidelity; the real store file is exercised (own code real).
- **Release gate:** same suite on a clean checkout. No external infra → merge and release fidelity coincide for jotdo.

**Build playbook.** Author contracts (this doc) → implement each slice with its test → run the suite → done. No deferred phases.

**Build status.** All four capability slices are built and Verified by the coverage-map suite (single-session build; the suite run is the verification record at this scale).

**Build-ready gate.** Every in-scope concern at Contract-grade (tracked in `manifest.yaml`), set published.

**Non-goals** *(kind: absent — see manifest)*: external tracker binding — no tracker mirrors this build; branching/release/versioning process — the deliverable is a single file, distributed as-is.

## 7. Security & Privacy

**Trust boundary.** Single local user; the only data sink is a file under the user's own home/`$JOTDO_FILE`. **Secrets:** none.

**Threat model (negative assertion).** For a minimal-risk product the threat model states what is *not* a threat here, contractually:
- `SEC-LOCAL-ONLY` — jotdo performs no network I/O of any kind; its only side effect is reading/writing the store file at `$JOTDO_FILE`. Asserted by `test_local_only` (coverage map, §5).

**Non-goals** *(kind: absent — see manifest)*: authentication, authorization, sessions, per-field protection, encryption — jotdo has no remote surface, no multi-user model, and no sensitive fields.

## 8. Governance & Compliance

**License / IP.** MIT (own code). No third-party dependencies, so no third-party license obligations.

**Non-goals** *(kind: absent — see manifest)*: data-handling policy, audit requirements, framework mapping, retention/residency, consent — jotdo processes no regulated or sensitive data.
