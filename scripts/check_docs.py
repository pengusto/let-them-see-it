"""Check local links, language navigation, and installation command parity."""
from pathlib import Path
import os
import re

root = Path(__file__).resolve().parents[1]
translations = root / "docs" / "readme"
readmes = [root / "README.md", *(translations / name for name in (
    "README.de.md", "README.zh-CN.md", "README.ja.md", "README.es.md",
    "README.ko.md", "README.pt-BR.md", "README.fr.md",
))]
source = readmes[0].read_text()
commands = re.findall(r"```sh\n(.*?)```", source, re.S)
assert commands, "Source README has no installation command"
for readme in readmes:
    content = readme.read_text()
    nav = content.splitlines()[2]
    assert re.findall(r"```sh\n(.*?)```", content, re.S) == commands, readme.name
    for target in readmes:
        relative = Path(os.path.relpath(target, readme.parent)).as_posix()
        assert f"]({relative})" in nav, f"Missing language link: {readme.name} -> {relative}"
links = 0
for document in [*root.glob("*.md"), *translations.glob("*.md")]:
    for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
        if "://" not in target and not target.startswith("#"):
            assert (document.parent / target.split("#")[0]).is_file(), (document.name, target)
            links += 1
print(f"PASS: {len(readmes)} READMEs, {links} local links, matching install commands")
