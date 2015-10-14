#!/usr/bin/python

import langid
import os
import time

TEST_FILES_DIR = "/Users/ruben/Desktop/lang/"

start_time = time.time()

detected = 0
total = 0

langs = os.listdir(TEST_FILES_DIR)
del langs[0]

for lang in langs:
    for file in os.listdir(TEST_FILES_DIR + lang):
        total += 1
        ltype = langid.classify(open(TEST_FILES_DIR + lang + "/" + file, 'r').read())[0]
        if ltype == lang:
            detected += 1

print("Total " + str(total) + " detected " + str(detected) + " Time spent: %.2f seconds" % (time.time() - start_time))
