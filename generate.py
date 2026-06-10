import json, shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

OUTPUT_DIR = Path("output")


def load(filename):
    return json.loads(Path(filename).read_text())


def main() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir()
    shutil.copytree("data/certs", OUTPUT_DIR / "certs")

    content = load("data/content.json")
    abbrev, achievements = load("data/abbrev.json"), load("data/achievements.json")

    env = Environment(loader=FileSystemLoader("input"))
    index_html = env.get_template("index.html.j2")

    print(abbrev, achievements[0]["items"])
    output = index_html.render(**content, abbrev=abbrev, achievements=achievements)
    Path("output/index.html").write_text(output)


if __name__ == "__main__":
    main()
