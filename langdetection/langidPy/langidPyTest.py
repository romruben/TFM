#!/usr/bin/python

import langid
import csv
import argparse
import os
import time

TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/"
LANGUAGES_TO_TEST = "English,Spanish"
FILES_BY_LANGUAGE = "resources/filesByLanguage.properties"
LANGUAGES_IDS = "resources/profiles.properties"


def merge_default_with_args(testdir, languages, files_by_lang):
    global TEST_FILES_DIR
    global LANGUAGES_TO_TEST
    global FILES_BY_LANGUAGE

    if testdir is not None: TEST_FILES_DIR = testdir
    if languages != LANGUAGES_TO_TEST and languages is not None: LANGUAGES_TO_TEST = languages
    if files_by_lang is not None: FILES_BY_LANGUAGE = files_by_lang


def test_langid(testdir, languages, filesByLang):
    merge_default_with_args(testdir, languages, filesByLang)

    # Reference vars
    languages_id, supported_languages, reference_files = release_default_vars_with_args()

    # files to filter
    filterfiles = file_filter(reference_files, supported_languages)

    # files to test
    testfiles = get_test_files(filterfiles)

    # well detected files
    detected = get_total_well_detected_langs(testfiles, languages_id, reference_files)

    # testing
    print "Expected %r Detected %r" % (len(testfiles), detected)


def get_total_well_detected_langs(filesToTest, languages_id, reference_files):
    return sum(1 for file in filesToTest if
               languages_id.get(langid.classify(open(TEST_FILES_DIR + file, 'r').read())[0]) == reference_files.get(
                   file))


def get_test_files(filterfiles):
    return [file for file in os.listdir(TEST_FILES_DIR) if file not in filterfiles]


def file_filter(reference_files, supported_languages):
    filtered_files = [file for file in reference_files.keys() if reference_files.get(file) not in supported_languages]
    filtered_files.append(".DS_Store")
    return filtered_files


def release_default_vars_with_args():
    reference_files = dict([(row[0], row[1]) for row in csv.reader(open(FILES_BY_LANGUAGE, 'rU'), delimiter='=')])
    languages_id = dict([(row[0], row[1]) for row in csv.reader(open(LANGUAGES_IDS, 'rU'), delimiter='=')])
    supported_languages = LANGUAGES_TO_TEST.split(",")
    return languages_id, supported_languages, reference_files


parser = argparse.ArgumentParser(description='Ruben TFM language detection with langid.py')
parser.add_argument('-t', '--testdir', help='testdir', required=False)
parser.add_argument('-l', '--languages', help='Languages to tests', required=False)
parser.add_argument('-f', '--filesByLang', help='filesByLang', required=False)
args = parser.parse_args()

start_time = time.time()
test_langid(args.testdir, args.languages, args.filesByLang)
print("Time spent: %.2f seconds" % (time.time() - start_time))
