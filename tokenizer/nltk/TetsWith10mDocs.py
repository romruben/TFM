DOCS_TXT_ROOT = "/Users/ruben/Desktop/txt/"
__author__ = 'ruben'

import datetime
import os
import argparse

from nltk.tokenize import TreebankWordTokenizer, RegexpTokenizer, WhitespaceTokenizer, TextTilingTokenizer, \
    PunktSentenceTokenizer, word_tokenize
from nltk.tokenize.simple import SpaceTokenizer
from nltk.tokenize.stanford import StanfordTokenizer

os.environ['STANFORD_POSTAGGER'] = os.path.dirname(__file__) + "/stanford-postagger.jar"


def get_time():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


def timeit(method):
    def timed(*args, **kw):
        ts = get_time()
        result = method(*args, **kw)
        te = get_time()

        print '%r %2.5f milliseconds' % \
              (method.__name__, te - ts)
        return result

    return timed


def readfile(path):
    return open(path, 'r').read()


@timeit
def test_treebank_word_tokenizer():
    files = os.listdir(DOCS_TXT_ROOT)
    total = sum(len(TreebankWordTokenizer().tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)
    print "\nTreebankWordTokenizer total: " + str(total)


@timeit
def test_regexp_tokenizer():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    total = sum(len(RegexpTokenizer(r'\w+').tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)
    print "\nRegxpTokenizer total: " + str(total)


@timeit
def test_whitespace_tokenizer():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    total = sum(len(WhitespaceTokenizer().tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)
    print "\nWhitespaceTokenizer total: " + str(total)


@timeit
def test_word_tokenize():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    total = sum(len(word_tokenize(readfile(DOCS_TXT_ROOT + f), language='english')) for f in files)
    print "\nword_tokenize total " + str(total)


@timeit
def test_space_tokenizer():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    total = sum(len(SpaceTokenizer().tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)

    print "\nSpaceTokenizer total: " + str(total)


@timeit
def test_stanford_tokenizer():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    standfor = StanfordTokenizer()
    total = sum(len(standfor.tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)

    print "\nStanfordTokenizer total " + str(total)


# @timeit
# def test_text_tiling_tokenizer():
#     files = os.listdir("/Users/ruben/Desktop/txt/")
#     total = sum(len() for f in files)
#
#     s, ss, d, b = TextTilingTokenizer(demo_mode=True).tokenize(content)
#     print "\n"
#     # print s, ss, d, b


@timeit
def test_punkt_sentence_tokenizer():
    files = os.listdir("/Users/ruben/Desktop/txt/")
    total = sum(len(PunktSentenceTokenizer().tokenize(readfile(DOCS_TXT_ROOT + f))) for f in files)

    print "\nPunktSentenceTokenizer total " + str(total)


def run_all_tests():
    test_treebank_word_tokenizer()
    test_regexp_tokenizer()
    test_whitespace_tokenizer()
    test_word_tokenize()
    test_space_tokenizer()
    # test_stanford_tokenizer()
    # test_text_tiling_tokenizer()
    test_punkt_sentence_tokenizer()


run_all_tests()
