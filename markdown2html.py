#!/usr/bin/python3
"""
markdown2html module
"""


import sys
import os


def markdown_to_html(markdown: str, output_file: str):
    """
    Converts a Markdown file to an HTML file.

    Args:
        markdown (str): Path to the Markdown input file.
        output_file (str): Path to the HTML output file.

    Returns:
        nothing
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    if not os.path.exists(markdown):
        print("Missing ", markdown, file=sys.stderr)
        exit(1)
    exit(0)
