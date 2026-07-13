#!/usr/bin/env python3
"""jotdo — a tiny task-list CLI that persists to a JSON file.

Realizes the contracts in docs/SPEC.md (a Dictum doc set, single-file
packaging). Contract IDs are tagged at their realizing sites with the
in-code annotation convention (`# DICT: <ID>`); the canonical contract is
the doc, and the contract->code map is bindings.yaml.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

DEFAULT_FILE = os.path.expanduser("~/.jotdo.json")


def store_path() -> str:
    return os.environ.get("JOTDO_FILE", DEFAULT_FILE)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# DICT: ENTITY-TASK
@dataclass
class Task:
    id: int
    title: str
    done: bool
    created: str  # ISO-8601 UTC timestamp


# DICT: ENTITY-STORE — owns the monotonic id sequence
@dataclass
class Store:
    seq: int = 0                       # highest id ever issued
    tasks: list[Task] = field(default_factory=list)

    def add(self, title: str) -> Task:
        # DICT: INV-TASK-ID-UNIQUE / INV-TASK-ID-MONOTONIC — seq only ever
        # increases, so ids are unique and never reused, even after removals.
        self.seq += 1
        task = Task(id=self.seq, title=title, done=False, created=_now())
        self.tasks.append(task)
        return task

    def mark_done(self, task_id: int) -> bool:
        for t in self.tasks:
            if t.id == task_id:
                t.done = True
                return True
        return False

    def remove(self, task_id: int) -> bool:
        before = len(self.tasks)
        self.tasks[:] = [t for t in self.tasks if t.id != task_id]
        return len(self.tasks) != before


def load() -> Store:
    path = store_path()
    if not os.path.exists(path):
        return Store()
    with open(path) as f:
        raw = json.load(f)
    return Store(seq=raw.get("seq", 0),
                 tasks=[Task(**row) for row in raw.get("tasks", [])])


def save(store: Store) -> None:
    with open(store_path(), "w") as f:
        json.dump({"seq": store.seq, "tasks": [asdict(t) for t in store.tasks]},
                  f, indent=2)


# DICT: CLI-ADD
def cmd_add(args: argparse.Namespace) -> int:
    store = load()
    task = store.add(args.title)
    save(store)
    print(f"added #{task.id}")
    return 0


# DICT: CLI-LIST
def cmd_list(args: argparse.Namespace) -> int:
    store = load()
    if not store.tasks:
        print("(no tasks)")
        return 0
    for t in store.tasks:
        box = "[x]" if t.done else "[ ]"
        print(f"{box} #{t.id} {t.title}")
    return 0


# DICT: CLI-DONE
def cmd_done(args: argparse.Namespace) -> int:
    store = load()
    if not store.mark_done(args.id):
        print(f"no task #{args.id}", file=sys.stderr)
        return 1
    save(store)
    print(f"done #{args.id}")
    return 0


# DICT: CLI-RM
def cmd_rm(args: argparse.Namespace) -> int:
    store = load()
    if not store.remove(args.id):
        print(f"no task #{args.id}", file=sys.stderr)
        return 1
    save(store)
    print(f"removed #{args.id}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="jotdo", description="a tiny task list")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a task done")
    p_done.add_argument("id", type=int)
    p_done.set_defaults(func=cmd_done)

    p_rm = sub.add_parser("rm", help="remove a task")
    p_rm.add_argument("id", type=int)
    p_rm.set_defaults(func=cmd_rm)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
