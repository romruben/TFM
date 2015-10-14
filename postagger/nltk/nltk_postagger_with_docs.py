from nltk import tag
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import brown
from nltk.corpus import treebank
from nltk.corpus import reader
from nltk import tbl
import os
import datetime
import nltk.data
import codecs

# backoff pregunta a otro tagger cuando este no encuentra la forma
# nltk da soporte a collocations: http://www.nltk.org/howto/collocations.html, bigram, trigram, etc..
# usa reglas de sustitucion
# clasificadores tras etiquetacion

TAGGER_ENGLISH_MODEL = nltk.data.load('nltk:taggers/maxent_treebank_pos_tagger/english.pickle')
CORPUS_ORIGIN_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/detroit.txt"
CORPUS_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/processed_corpus/processed_text.txt"
CORPUS_TAG_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/processed_corpus/tags.txt"


def get_time():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


def timeit(method):
    def timed(*args, **kw):
        ts = get_time()
        result = method(*args, **kw)
        te = get_time()

        print '%r %2.2f milliseconds\n' % \
              (method.__name__, te - ts)
        return result

    return timed


def train_collection():
    return list(brown.tagged_sents(categories='news')[:100000])

def readfile(path):
    return codecs.open(path, 'r', encoding='utf-8').read()

def extra_condition(condition, param):
    return True if condition is None else condition == param


class TestingTaggers:

    @timeit
    def test_standar_postagger(self, allfiles):
        detected = 0
        obtained = 0

        for file in allfiles:
            content = readfile(file)
            obtained += len(tag.pos_tag(content))
            detected += len(content.split(" "))

        print "StandarPOSTagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_affix_tagger(self, allfiles):
        detected = 0
        obtained = 0
        aft = tag.AffixTagger(train=trained_collection)

        for file in allfiles:
            content = readfile(file)
            obtained += len(aft.tag(content))
            detected += len(content.split(" "))

        print "AffixPOSTagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_default_postagger(self, allfiles):
        detected = 0
        obtained = 0
        dt = tag.DefaultTagger('NN')

        for file in allfiles:
            content = readfile(file)
            obtained += len(dt.tag(content))
            detected += len(content.split(" "))

        print "DefaultPOSTagger (Only nouns) detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_classifierbased_postagger(self, allfiles):
        detected = 0
        obtained = 0
        classifier = tag.ClassifierBasedPOSTagger(train=trained_collection)

        for file in allfiles:
            content = readfile(file)
            obtained += len(classifier.tag(content))
            detected += len(content.split(" "))

        print "ClassifierBasedPOSTagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_unigram_tagger(self, allfiles):
        detected = 0
        obtained = 0
        unigram = tag.UnigramTagger(train=trained_collection)

        for file in allfiles:
            content = readfile(file)
            obtained += len(unigram.tag(content))
            detected += len(content.split(" "))

        print "ClassifierBasedPOSTagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_bigram_tagger(self, allfiles):
        detected = 0
        obtained = 0
        t0 = tag.UnigramTagger(train=trained_collection)
        bigram = tag.BigramTagger(train=trained_collection, backoff=t0)

        for file in allfiles:
            content = readfile(file)
            obtained += len(bigram.tag(content))
            detected += len(content.split(" "))

        print "BigramTagger backoff=unigramtagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_trigram_tagger(self, allfiles):
        detected = 0
        obtained = 0
        t0 = tag.UnigramTagger(train=trained_collection)
        trigram = tag.TrigramTagger(train=trained_collection, backoff=t0)

        for file in allfiles:
            content = readfile(file)
            obtained += len(trigram.tag(content))
            detected += len(content.split(" "))

        print "TrigramTagger backoff=unigramtagger detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_ngram_tagger(self, allfiles):
        detected = 0
        obtained = 0
        t0 = tag.UnigramTagger(train=trained_collection)
        ngram = tag.NgramTagger(5, train=trained_collection, backoff=t0)

        for file in allfiles:
            content = readfile(file)
            obtained += len(ngram.tag(content))
            detected += len(content.split(" "))

        print "Ngram detected backoff=unigramtagger : " + str(detected) + " obtained: " + str(obtained)

    @timeit
    def test_regexp_tagger(self, allfiles):
        detected = 0
        obtained = 0
        t0 = nltk.DefaultTagger('NN')
        regexp = tag.RegexpTagger({"NN"}, backoff=t0)

        for file in allfiles:
            content = readfile(file)
            obtained += len(regexp.tag(content))
            detected += len(content.split(" "))

        print "RegexpTagger using backoff = DefaultTagger, only 'NN' :  detected: " + str(detected) + " obtained: " + str(obtained)

    @timeit
    # anyadir fichero stanford-postagger.jar
    def test_stanford_postagger(self, allfiles):
        detected = 0
        obtained = 0
        t0 = nltk.DefaultTagger('NN')
        model = os.getcwd() + "/models/stanford/english-bidirectional-distsim.tagger"
        postagger_jar = os.getcwd() + "/models/stanford/stanford-postagger.jar"
        stanforTagger = tag.StanfordPOSTagger(model, path_to_jar=postagger_jar)

        for file in allfiles:
            content = readfile(file)
            obtained += len(stanforTagger.tag(content))
            detected += len(content.split(" "))

        print "StanfordPOSTagger (english-bidirectional-distsim) using backoff = DefaultTagger, only 'NN' :  detected: " + str(detected) + " obtained: " + str(obtained)

    def testing_all(self, candidates):
        self.test_standar_postagger(candidates)
        self.test_affix_tagger(candidates)
        self.test_default_postagger(candidates)
        self.test_classifierbased_postagger(candidates)
        self.test_unigram_tagger(candidates)
        self.test_bigram_tagger(candidates)
        self.test_trigram_tagger(candidates)
        self.test_ngram_tagger(candidates)
        self.test_regexp_tagger(candidates)
        self.test_stanford_postagger(candidates)


candidates = []
for dirpath, dirnames, filenames in os.walk('/Users/ruben/Desktop/txt/', followlinks=True):
    for docname in filenames:
        candidates.append(os.path.join(dirpath, docname))

trained_collection = train_collection()


testing = TestingTaggers()
testing.testing_all(candidates)