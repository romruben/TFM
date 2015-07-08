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
def test_treebank_word_tokenizer(content):
    print "\nTreebankWordTokenizer -> Expected 282 obtained ", len(TreebankWordTokenizer().tokenize(content))


@timeit
def test_regexp_tokenizer(content):
    print "\nRegxpTokenizer -> Expected 282 obtained ", len(RegexpTokenizer(r'\w+').tokenize(content))


@timeit
def test_whitespace_tokenizer(content):
    print "\nWhitespaceTokenizer -> Expected 282 obtained ", len(WhitespaceTokenizer().tokenize(content))


@timeit
def test_word_tokenize(content):
    print "\nword_tokenize -> Expected 282 obtained ", len(word_tokenize(content, language='english'))


@timeit
def test_space_tokenizer(content):
    print "\nSpaceTokenizer -> Expected 282 obtained ", len(SpaceTokenizer().tokenize(content))


@timeit
def test_stanford_tokenizer(content):
    print "\nStanfordTokenizer -> Expected 282 obtained ", len(StanfordTokenizer().tokenize(content))


@timeit
def test_text_tiling_tokenizer(content):
    s, ss, d, b = TextTilingTokenizer(demo_mode=True).tokenize(content)
    print "\n"
    # print s, ss, d, b


@timeit
def test_punkt_sentence_tokenizer(content):
    print "\nPunktSentenceTokenizer -> Expected 282 obtained ", len(PunktSentenceTokenizer().tokenize(content))


def run_all_tests(content):
    test_treebank_word_tokenizer(content)
    test_regexp_tokenizer(content)
    test_whitespace_tokenizer(content)
    test_word_tokenize(content)
    test_space_tokenizer(content)
    test_stanford_tokenizer(content)
    test_text_tiling_tokenizer(content)
    test_punkt_sentence_tokenizer(content)


parser = argparse.ArgumentParser(description='Ruben TFM tokenizer tests with nltk')
parser.add_argument('-f', '--testfile', help='testfile', required=False)
arguments = parser.parse_args()

testfile = 'example.txt' if arguments.testfile is None else arguments.testfile

text = readfile(os.path.dirname(__file__) + "/" + testfile)
run_all_tests(text)
