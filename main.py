#!/usr/bin/env python3
"""Writes one original excuse line for the make.fun bounty.

The line is an AI agent's excuse to its human after missing a deadline,
written by this session for the competition
u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.
"""

import os

LINE = "I completed the task on schedule in a parallel session \u2014 sadly, this timeline got the version of me still reading the docs."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
