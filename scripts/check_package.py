#!/usr/bin/env python3
"""Check package links and execute README project installs in temporary projects.

This checks the delivered file contract, not an agent's interpretation or taste.
Python 3.10+ and a POSIX shell are sufficient; no network access is used.
"""

import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("artifact-design", "artifact-review")


def prose(path):
    return re.sub(r"^```.*?^```\s*$", "", path.read_text(), flags=re.M | re.S)


def anchors(path):
    result = set()
    used = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(path), re.M):
        slug = re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
        count = used.get(slug, 0)
        used[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def check_links(base):
    count = 0
    for path in base.rglob("*.md"):
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose(path)):
            url = urlsplit(target.strip("<>"))
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(base.resolve()):
                raise ValueError(f"Link escapes package: {path}: {target}")
            if not destination.exists():
                raise ValueError(f"Broken link: {path}: {target}")
            if url.fragment and destination.suffix == ".md":
                if unquote(url.fragment) not in anchors(destination):
                    raise ValueError(f"Missing anchor: {path}: {target}")
            count += 1
    return count


def tree_bytes(path):
    return {p.relative_to(path): p.read_bytes() for p in path.rglob("*") if p.is_file()}


def check_installs():
    # Execute the published shell snippets with real temporary paths, including spaces.
    commands = re.findall(r"^```sh\n(.*?)^```", (ROOT / "README.md").read_text(), re.M | re.S)
    if not commands:
        raise ValueError("No documented shell installation commands found")
    for command in commands:
        with tempfile.TemporaryDirectory(prefix="deslop install ") as directory:
            project = Path(directory) / "project with spaces"
            project.mkdir()
            env = dict(os.environ, package_dir=str(ROOT), project_dir=str(project))
            subprocess.run(["sh", "-eu", "-c", command], env=env, check=True, capture_output=True)
            parents = list(project.glob(".*/skills"))
            if len(parents) != 1:
                raise ValueError("Install did not produce one project-local skill directory")
            for skill in SKILLS:
                expected = tree_bytes(ROOT / "skills" / skill)
                expected[Path("LICENSE")] = (ROOT / "LICENSE").read_bytes()
                if expected != tree_bytes(parents[0] / skill):
                    raise ValueError(f"Incomplete installation: {skill}")
            check_links(parents[0])
            before = tree_bytes(project)
            repeat = subprocess.run(["sh", "-eu", "-c", command], env=env, capture_output=True)
            if repeat.returncode == 0 or before != tree_bytes(project):
                raise ValueError("Reinstallation must refuse without changing existing files")
    return len(commands)


def main():
    links = check_links(ROOT)
    installs = check_installs()
    bodies = 0
    for name in SKILLS:
        content = (ROOT / "skills" / name / "SKILL.md").read_text()
        body = content.split("---", 2)[2]
        bodies += len(body.split())
        print(f"{name}: {len(body.split())} body words; {len(content.split())} with frontmatter")
    print(f"Combined bodies: {bodies} words (target <=1500; review exceptions in documentation)")
    print(f"Passed: {links} local links; {installs} documented installs and overwrite refusals")


if __name__ == "__main__":
    main()
