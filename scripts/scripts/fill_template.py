import os

TEMPLATE = "template.md"


def fill_file(path):

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        text = f.read()

    parts = path.split(os.sep)

    # Expected: YEAR / MON / DAY.md
    year = parts[-3]
    month = parts[-2]
    day = parts[-1].replace(".md", "")

    text = text.replace("{{DAY}}", day)
    text = text.replace("{{MONTH}}", month)
    text = text.replace("{{YEAR}}", year)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


for root, _, files in os.walk("."):

    for file in files:

        if not file.endswith(".md"):
            continue

        if file in ["calendar.md", "template.md", "README.md"]:
            continue

        path = os.path.join(root, file)

        # Only fill empty files
        if os.path.getsize(path) == 0:
            fill_file(path)
