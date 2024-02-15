import argparse
import json
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="OneTab export file path")
parser.add_argument(
    "-o", "--output",
    default="import.json", type=str,
    help="Output file name (saved in the same directory as the input file)",
)
parser.add_argument(
    "-n", "--num_line_per_page",
    default=400, type=int, help="Number of lines per page",
)
args = parser.parse_args()

in_path = Path(args.filepath)
root = in_path.parent
out_path = root / args.output

with in_path.open() as f:
    lines = f.readlines()

# create pages
line_chunks = [
    lines[i : i + args.num_line_per_page]
    for i in range(0, len(lines), args.num_line_per_page)
]
titles = [f"{in_path.stem} - {i + 1}" for i in range(len(line_chunks))]
data = {
    "pages": [
    {
        "title": title,
        "lines": [title] + chunk + [""],  # add title line at the beginning & empty line at the end
    }
    for title, chunk in zip(titles, line_chunks)
]}

with out_path.open("w") as f:
    json.dump(data, f, indent=2)
