import enum
import os
import subprocess
import sys
import tomllib

from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

PYPROJECT_SECTION = "zettelkasten"
DESTINATION_OPTION = "destination"


class GeneratorErrorMessage(enum.StrEnum):
    """ Collection of error messages """
    PYPROJECT_MISSING = "pyproject.toml not found"
    INCOMPLETE_CONFIG = f"Missing [tool.{PYPROJECT_SECTION}] {DESTINATION_OPTION} in pyproject.toml"
    MISSING_ARGUMENT = "Usage: new-note \"Title of the note\""
    DEST_NOT_EXISTS = "Error destination folder does not exist on the filesystem!"

def load_config() -> str:
    """ Read destination path from pyproject.toml """
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    assert pyproject_path.exists(), GeneratorErrorMessage.PYPROJECT_MISSING
    with open(pyproject_path, 'rb') as file:
        config = tomllib.load(file)
    try:
        return Path(config["tool"][PYPROJECT_SECTION][DESTINATION_OPTION])
    except KeyError:
        sys.exit(GeneratorErrorMessage.INCOMPLETE_CONFIG)

def open_in_editor(file_path: Path, line_number: int = 1) -> None:
    """ Conditionally open new note in editor, if any """
    if not (editor:= os.environ.get("EDITOR")):
        sys.exit(0)

    match editor:
        case "code":
            cmd = [editor, "-g", f"{file_path}:{line_number}"]
        case e if e in ("vim", "nvim", "nano", "emacs"):
            cmd = [e, f"+{line_number}", str(file_path)]
        case _:
            sys.exit(0)

    subprocess.run(cmd, check=False)


def main():
    """ Takes in a quoted string as a argument.
    Create a new note with the same value as a title """
    if len(sys.argv) < 2:
        sys.exit(GeneratorErrorMessage.MISSING_ARGUMENT)

    dest = load_config()
    title = " ".join(sys.argv[1:])

    assert dest.exists(), GeneratorErrorMessage.DEST_NOT_EXISTS

    ids = [
        int(str(path.name).split("_")[0].replace("-", ""))
        for path in dest.glob("*.md")
    ]
    next_id = f"{max(ids, default=0) + 1:011_}".replace("_","-")

    filename_title = title.lower().replace(" ", "-")
    outfile = dest / f"{next_id}_{filename_title}.md"

    env = Environment(loader=FileSystemLoader(Path(__file__).parent))
    template = env.get_template("note.md.j2")
    rendered = template.render(
        id=next_id,
        title=title,
        date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    )

    outfile.write_text(rendered, encoding="utf-8")
    open_in_editor(outfile, 9)


if __name__ == "__main__":
    main()
