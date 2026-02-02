import os
import calendar
from datetime import datetime

YEAR = 2026
MONTH = 2   # Feb

FOLDER = "2026/Feb"
OUTPUT = f"{FOLDER}/calendar.md"

cal = calendar.Calendar(calendar.MONDAY)

days = cal.monthdayscalendar(YEAR, MONTH)

files = set(f.split(".")[0] for f in os.listdir(FOLDER) if f.endswith(".md"))

with open(OUTPUT, "w") as f:

    f.write(f"# February {YEAR}\n\n")

    f.write("| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n")
    f.write("|-----|-----|-----|-----|-----|-----|-----|\n")

    for week in days:
        row = "|"
        for d in week:
            if d == 0:
                row += "     |"
            else:
                key = f"{d:02d}"
                if key in files:
                    row += f" [{d}]({key}.md) |"
                else:
                    row += f" {d} |"
        f.write(row + "\n")
