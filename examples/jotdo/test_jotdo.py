"""jotdo test suite (stdlib unittest). One invariant per test (Dictum Quality & Testing)."""
import ast
import contextlib
import io
import os
import tempfile
import unittest

import jotdo


def run(*argv):
    """Invoke the CLI, swallowing stdout, returning the exit code."""
    with contextlib.redirect_stdout(io.StringIO()):
        return jotdo.main(list(argv))


class JotdoTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)  # start with no store
        os.environ["JOTDO_FILE"] = self.path

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        os.environ.pop("JOTDO_FILE", None)

    def test_add_and_list(self):
        run("add", "buy milk")
        run("add", "walk dog")
        tasks = jotdo.load().tasks
        self.assertEqual([t.title for t in tasks], ["buy milk", "walk dog"])
        self.assertEqual([t.done for t in tasks], [False, False])

    def test_done(self):
        run("add", "task")
        run("done", "1")
        self.assertTrue(jotdo.load().tasks[0].done)

    def test_remove(self):
        run("add", "task")
        run("rm", "1")
        self.assertEqual(jotdo.load().tasks, [])

    # DICT: INV-TASK-ID-UNIQUE (asserts this invariant only)
    def test_ids_unique(self):
        store = jotdo.Store()
        for i in range(3):
            store.add(f"t{i}")
        store.remove(2)
        store.add("t3")
        ids = [t.id for t in store.tasks]
        self.assertEqual(len(set(ids)), len(ids))

    # DICT: INV-TASK-ID-MONOTONIC (asserts this invariant only)
    def test_ids_monotonic(self):
        store = jotdo.Store()
        for i in range(3):
            store.add(f"t{i}")           # ids 1, 2, 3
        store.remove(3)                  # remove the highest
        store.add("t4")
        self.assertEqual(store.tasks[-1].id, 4)  # must not reuse 3

    # DICT: SEC-LOCAL-ONLY (asserts the zero-network negative assertion)
    def test_local_only(self):
        forbidden = {"socket", "ssl", "http", "urllib", "ftplib", "smtplib",
                     "poplib", "imaplib", "telnetlib", "xmlrpc", "asyncio"}
        with open(jotdo.__file__) as f:
            tree = ast.parse(f.read())
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertFalse(imported & forbidden,
                         "network-capable module imported; SEC-LOCAL-ONLY broken")


if __name__ == "__main__":
    unittest.main()
