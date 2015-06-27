#!/usr/bin/env python3
"""Generate a trigrams file from plain text files.

Input may be files extracted with Wikipedia Extractor:
http://medialab.di.unipi.it/wiki/Wikipedia_Extractor
"""

import argparse
import os
import re
import sys

from collections import defaultdict
from guess_language import WORD_RE, MAX_GRAMS


TAG_RE = re.compile(r"<.*?>|\{.*?\}|\\\w+")


class OrderedModelBuilder:
    def __init__(self):
        self.trigrams = defaultdict(int)

    def feed(self, text):
        words = WORD_RE.findall(text.replace("’", "'"))
        content = " ".join(words).lower()
        for n in range(len(content) - 2):
            self.trigrams[content[n:n+3]] += 1

    @property
    def ordered_model(self):
        return sorted(self.trigrams.keys(),
                      key=lambda k: (-self.trigrams[k], k))[:MAX_GRAMS]


def parse(builder, path):
    lines = []
    with open(path) as f:
        for line in f:
            if line.startswith("<doc"):
                lines[:] = []
            elif line.startswith("</doc"):
                builder.feed(" ".join(lines))
                lines[:] = []
            else:
                lines.append(TAG_RE.sub("", line))
    if lines:
        builder.feed(" ".join(lines))


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "txt_dir",
        help="directory of plain text files"
    )
    parser.add_argument(
        "output",
        help="output trigrams file"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    builder = OrderedModelBuilder()

    for dirpath, dirnames, filenames in os.walk(args.txt_dir):
        for filename in sorted(filenames):
            path = os.path.join(dirpath, filename)
            print(path)
            parse(builder, path)

    with open(args.output, "w") as f:
        for n, trigram in enumerate(builder.ordered_model):
            print("{}\t\t\t{}".format(trigram, n), file=f)


if __name__ == "__main__":
    sys.exit(main())
