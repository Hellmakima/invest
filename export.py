import re
import csv

input_file = "halal_stocks filtered.html"
output_file = "halal_stocks2.csv"

td_pattern = re.compile(r"<td.*?>(.*?)</td>")
href_pattern = re.compile(r'href="(.*?)"')
tag_strip = re.compile(r"<.*?>")

with open(input_file, "r", encoding="utf-8") as f, \
     open(output_file, "w", newline="", encoding="utf-8") as out:

    writer = csv.writer(out)

    for line in f:
        matches = td_pattern.findall(line)
        if matches:
            row = []
            for cell in matches:
                href = href_pattern.search(cell)
                if href:
                    row.append(href.group(1))
                else:
                    clean = tag_strip.sub("", cell).strip()
                    row.append(clean)

            writer.writerow(row)

