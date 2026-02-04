import re

TASKS_FILE = "tasks.md"
README_FILE = "README.md"


with open(TASKS_FILE, "r", encoding="utf-8") as f:
    tasks = f.read().strip()


with open(README_FILE, "r", encoding="utf-8") as f:
    readme = f.read()


pattern = re.compile(
    r"<!-- TASKS_START -->.*?<!-- TASKS_END -->",
    re.DOTALL
)

replacement = f"""<!-- TASKS_START -->
{tasks}
<!-- TASKS_END -->"""


new_readme = pattern.sub(replacement, readme)


with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_readme)
