#!/usr/bin/python
from guess_language import *
import langid
import os
import time

TEST_FILES_DIR = "/Users/ruben/Desktop/lang/"

H = dict(line.strip().split('=') for line in open('resources/profiles_europarl.properties'))

start_time = time.time()
detected = 0
total = 0

langs = os.listdir(TEST_FILES_DIR)
del langs[0]

for lang in langs:
    for file in os.listdir(TEST_FILES_DIR + lang):
        total += 1
        ltype = guessLanguageName(open(TEST_FILES_DIR + lang + "/" + file, 'r').read())
        if ltype in H and H[ltype] == lang:
            detected += 1

print("Total " + str(total) + " detected " + str(detected) + " Time spent: %.2f seconds" % (time.time() - start_time))