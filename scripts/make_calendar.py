import os
import calendar

YEAR = 2026
MONTH = 2   # February

MONTH_NAME = "Feb"
BASE = f"2026/{MONTH_NAME}"
OUTPUT = f"{BASE}/calendar.md"

cal = calendar.Calendar(calendar.MONDAY)
weeks = cal.monthdayscalendar(YEAR, MONTH)

# Find existing day files
files = set()

if os.path.exists(BASE):
    for f in os.listdir(BASE):
        if f.endswith(".md") and f != "calendar.md":
            files.add(f.replace(".md", ""))

with open(OUTPUT, "w") as out:

    out.write(f"# February {YEAR}\n\n")

    out.write("| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n")
    out.write("|-----|-----|-----|-----|-----|-----|-----|\n")

    for week in weeks:
        row = "|"
        for day in week:

            if day == 0:
                row += "     |"
            else:
                d = f"{day:02d}"

                if d in files:
                    row += f" [{day}]({d}.md) |"
                else:
                    row += f" {day} |"

        out.write(row + "\n")
