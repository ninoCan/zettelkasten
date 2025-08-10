import os
import sys
import re
import shutil
import tempfile
import unittest
from pathlib import Path

import generator.new_note as under_test

class TestNewNote(unittest.TestCase):
    real_project_dir = Path(__file__).resolve().parents[1]
    tmp_notes_dir = Path(tempfile.mkdtemp()) / "notes"
    _dest = None

    def setUp(self):
        self.tmp_notes_dir.mkdir()
        self._modify_destination(self.tmp_notes_dir)

    def _modify_destination(self, dest_folder=None):
        pyproject_path = self.real_project_dir / "pyproject.toml"
        pyproject_text = pyproject_path.read_text(encoding="utf-8").splitlines()
        destination_override = str(dest_folder) if self._dest is None else self._dest

        updated_lines = []
        within_zettelkasten_section = False
        for line in pyproject_text:
            if line.strip() == f"[tool.{under_test.PYPROJECT_SECTION}]":
                within_zettelkasten_section = True
                updated_lines.append(line)
                continue
            if within_zettelkasten_section and line.strip().startswith(under_test.DESTINATION_OPTION):
                self._dest = line.split("=")[-1].strip()
                updated_lines.append(f'{under_test.DESTINATION_OPTION} = "{destination_override}"')
                within_zettelkasten_section = False
                continue
            updated_lines.append(line)
        pyproject_path.write_text("\n".join(updated_lines), encoding="utf-8")

    def tearDown(self):
        os.unsetenv('EDITOR')
        shutil.rmtree(self.tmp_notes_dir)
        self._modify_destination("notes")


    def test_creates_new_note_with_incremented_id(self):
        _touch_one_file = (self.tmp_notes_dir / "000-000-001_my_first_note.md").touch()
        expected_filepath = self.tmp_notes_dir / "000-000-002_my-fancy-title.md"

        sys.argv = ["new-note", "My Fancy Title"]
        under_test.main()


        self.assertTrue(expected_filepath.exists(), "Expected new note file to be created")
        actual_content = expected_filepath.read_text(encoding="utf-8")


        self.assertIn("# 000-000-002: My Fancy Title", actual_content)

        date_match = re.search(r"date:\s+(\S+)", actual_content)
        self.assertIsNotNone(date_match, "Expected a date field in the header")
        iso_date = date_match.group(1)
        self.assertRegex(iso_date, r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*")

        self.assertIn("## connections:", actual_content)


if __name__ == "__main__":
    unittest.main()