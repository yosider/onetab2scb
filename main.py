import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="OneTab export file name")
parser.add_argument(
    "-o",
    "--output",
    default="import.json",
    help="Output file name (saved in the same directory as the input file)",
)
parser.add_argument(
    "--num_line_per_page", default=400, type=int, help="Number of lines per page"
)
args = parser.parse_args()

load_dotenv()

root = Path(os.getenv("ROOT_PATH"))
in_path = root / args.filename
out_path = root / args.output

with in_path.open() as f:
    lines = f.readlines()

# create pages
line_chunks = [
    lines[i : i + args.num_line_per_page]
    for i in range(0, len(lines), args.num_line_per_page)
]
data = {
    "pages": [
        {
            "title": f"{in_path.stem} - {i}",
            "lines": chunk,
        }
        for i, chunk in enumerate(line_chunks)
    ]
}

with out_path.open("w") as f:
    json.dump(data, f, indent=2)
