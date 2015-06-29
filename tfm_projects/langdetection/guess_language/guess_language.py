import csv
import argparse
import time
import os
from guess_language import *

TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/"
LANGUAGES_TO_TEST = "English,Spanish"
FILES_BY_LANGUAGE = "filesByLanguage.properties"
LANGUAGES_IDS = "profiles.properties"


def mergeDefaultWithCLArgs(testdir, languages, filesByLang):
    global TEST_FILES_DIR
    global LANGUAGES_TO_TEST
    global FILES_BY_LANGUAGE

    if testdir != None: TEST_FILES_DIR = testdir
    if languages != LANGUAGES_TO_TEST and languages != None: LANGUAGES_TO_TEST = languages
    if filesByLang != None: FILES_BY_LANGUAGE = filesByLang


def testLangidPy(testdir, languages, filesByLang):
    mergeDefaultWithCLArgs(testdir, languages, filesByLang)

    # Reference vars
    testFilesReference = dict([(row[0], row[1]) for row in csv.reader(open(FILES_BY_LANGUAGE, 'rU'), delimiter='=')])
    languagesIds = dict([(row[0], row[1]) for row in csv.reader(open(LANGUAGES_IDS, 'rU'), delimiter='=')])
    languagesSupported = LANGUAGES_TO_TEST.split(",")

    # files to filter
    filesToFilter = [file for file in testFilesReference.keys() if
                     testFilesReference.get(file) not in languagesSupported]
    filesToFilter.append(".DS_Store")

    # files to test
    filesToTest = [file for file in os.listdir(TEST_FILES_DIR) if file not in filesToFilter]

    # well detected files
    detected = sum(1 for file in filesToTest if
                   guessLanguageName(open(TEST_FILES_DIR + file, 'r').read()) == testFilesReference.get(file))

    # testing
    print "Expected %r Detected %r" %(len(filesToTest), detected)


parser = argparse.ArgumentParser(description='Ruben TFM language detection with guess_language')
parser.add_argument('-t', '--testdir', help='testdir', required=False)
parser.add_argument('-l', '--languages', help='Languages to tests', required=False)
parser.add_argument('-f', '--filesByLang', help='filesByLang', required=False)
args = parser.parse_args()

start_time = time.time()
testLangidPy(args.testdir, args.languages, args.filesByLang)
print("Time spent: %.2f seconds" % (time.time() - start_time))
