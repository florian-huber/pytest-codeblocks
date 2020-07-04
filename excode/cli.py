import argparse
import sys

from .main import extract, write


def _main():
    args = _parse_cmd_arguments()
    code_blocks = extract(args.infile, filter=args.filter)
    write(args.outfile, code_blocks)


def _parse_cmd_arguments():
    parser = argparse.ArgumentParser(
        description="Extract code blocks from markdown files."
    )
    parser.add_argument(
        "infile",
        # Force utf-8 encoding on input. Otherwise we're running into trouble
        # with files containing non-ASCII characters on platforms where ASCII
        # is the default encoding (e.g., circleci).
        type=argparse.FileType("r", encoding="UTF-8"),
        default=sys.stdin,
        help="input markdown file (default: stdin)",
    )
    parser.add_argument(
        "outfile",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="output file (default: stdout)",
    )
    parser.add_argument("-f", "--filter", type=str, help="filter string", default=None)
    return parser.parse_args()
