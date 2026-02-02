import os
import calendar

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

BASE = os.getcwd()


def make_calendar(year, month_name):

    month = MONTHS[month_name]
    folder = os.path.join(str(year), month_name)
    output = os.path.join(folder, "calendar.md")

    cal = calendar.Calendar(calendar.SUNDAY)
    weeks = cal.monthdayscalendar(year, month)

    files = set()

    for f in os.listdir(folder):
        if f.endswith(".md") and f != "calendar.md":
            files.add(f.replace(".md", ""))

    with open(output, "w") as out:

        out.write(f"# {month_name} {year}\n\n")

        out.write("| Sun | Mon | Tue | Wed | Thu | Fri | Sat |\n")
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


for year in os.listdir(BASE):

    if not year.isdigit():
        continue

    year_path = os.path.join(BASE, year)

    if not os.path.isdir(year_path):
        continue

    for month in os.listdir(year_path):

        if month not in MONTHS:
            continue

        make_calendar(int(year), month)
