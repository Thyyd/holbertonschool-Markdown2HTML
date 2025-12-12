#!/usr/bin/python3
"""
markdown2html module
"""


import sys
import os


def markdown_to_html(markdown_file: str, output_file: str):
    """
    Converts a Markdown file to an HTML file.

    Args:
        markdown (str): Path to the Markdown input file.
        output_file (str): Path to the HTML output file.

    Returns:
        nothing
    """
    if not os.path.exists(markdown_file):
        print("Missing ", markdown_file, file=sys.stderr)
        exit(1)
    exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
