from nltk import tag
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import brown
from nltk.corpus import treebank
from nltk.corpus import reader
from nltk import tbl
from nltk.tokenize import word_tokenize
import os
import datetime
import nltk.data
import codecs
from tabulate import tabulate

# backoff pregunta a otro tagger cuando este no encuentra la forma
# nltk da soporte a collocations: http://www.nltk.org/howto/collocations.html, bigram, trigram, etc..
# usa reglas de sustitucion
# clasificadores tras etiquetacion

TAGGER_ENGLISH_MODEL = nltk.data.load('nltk:taggers/maxent_treebank_pos_tagger/english.pickle')
CORPUS_ORIGIN_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/detroit.txt"
CORPUS_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/processed_corpus/processed_text.txt"
CORPUS_TAG_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/corpus/processed_corpus/tags.txt"

resultados = []


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

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = tag.pos_tag(content)

        print "StandarPOSTagger"
        tagged.insert(0, "StandarPOSTagger")
        resultados.append(tagged)

    @timeit
    def test_affix_tagger(self, allfiles):
        aft = tag.AffixTagger(train=trained_collection)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = aft.tag(content)

        print "AffixPOSTagger"
        tagged.insert(0, "AffixPOSTagger")
        resultados.append(tagged)

    @timeit
    def test_default_postagger(self, allfiles):
        dt = tag.DefaultTagger('NN')

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = dt.tag(content)

        print "DefaultPOSTagger (Only nouns)"
        tagged.insert(0, "DefaultPOSTagger (Only nouns)")
        resultados.append(tagged)

    @timeit
    def test_classifierbased_postagger(self, allfiles):
        classifier = tag.ClassifierBasedPOSTagger(train=trained_collection)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = classifier.tag(content)

        print "ClassifierBasedPOSTagger"
        tagged.insert(0, "ClassifierBasedPOSTagger")
        resultados.append(tagged)

    @timeit
    def test_unigram_tagger(self, allfiles):
        unigram = tag.UnigramTagger(train=trained_collection)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = unigram.tag(content)

        print "UnigramTagger"
        tagged.insert(0, "UnigramTagger")
        resultados.append(tagged)

    @timeit
    def test_bigram_tagger(self, allfiles):
        t0 = tag.UnigramTagger(train=trained_collection)
        bigram = tag.BigramTagger(train=trained_collection, backoff=t0)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = bigram.tag(content)

        print "BigramTagger backoff=unigramtagger"
        tagged.insert(0, "BigramTagger backoff = unigramtagger")
        resultados.append(tagged)

    @timeit
    def test_trigram_tagger(self, allfiles):
        t0 = tag.UnigramTagger(train=trained_collection)
        trigram = tag.TrigramTagger(train=trained_collection, backoff=t0)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = trigram.tag(content)

        print "TrigramTagger backoff=unigramtagger"
        tagged.insert(0, "TrigramTagger backoff=unigramtagger")
        resultados.append(tagged)

    @timeit
    def test_ngram_tagger(self, allfiles):
        t0 = tag.UnigramTagger(train=trained_collection)
        ngram = tag.NgramTagger(5, train=trained_collection, backoff=t0)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = ngram.tag(content)

        print "Ngram detected backoff=unigramtagger"
        tagged.insert(0, "Ngram detected backoff=unigramtagger")
        resultados.append(tagged)

    @timeit
    def test_regexp_tagger(self, allfiles):
        t0 = nltk.DefaultTagger('NN')
        regexp = tag.RegexpTagger({"NN"}, backoff=t0)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = regexp.tag(content)

        print "RegexpTagger using backoff = DefaultTagger, only 'NN'"
        tagged.insert(0, "RegexpTagger using backoff = DefaultTagger, only 'NN'")
        resultados.append(tagged)

    @timeit
    # anyadir fichero stanford-postagger.jar
    def test_stanford_postagger(self, allfiles):
        model = os.getcwd() + "/models/stanford/english-bidirectional-distsim.tagger"
        postagger_jar = os.getcwd() + "/models/stanford/stanford-postagger.jar"
        stanforTagger = tag.StanfordPOSTagger(model, path_to_jar=postagger_jar)

        for file in allfiles:
            content = word_tokenize(readfile(file))
            tagged = stanforTagger.tag(content)

        print "StanfordPOSTagger (english-bidirectional-distsim) using backoff = DefaultTagger, only 'NN'"
        tagged.insert(0, "StanfordPOSTagger (english-bidirectional-distsim) using backoff = DefaultTagger, only 'NN'")
        resultados.append(tagged)

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
candidates.append('/Users/ruben/Desktop/postaggers.txt')

# trained_collection = train_collection()
#
# testing = TestingTaggers()
# testing.testing_all(candidates)

verifier = ['Verifier', (u'1', 'CD'), (u'1', 'CD'), (u'950324', 'CD'), (u'1', 'CD'), (u'Pisek', 'NNP'),
            (u'south', 'NN'),
            (u'Bohemia', 'NNP'), (u'Type', 'NN'), (u'Credit', 'NN'), (u'Operation', 'NN'), (u'credit', 'NN'),
            (u'in', 'IN'), (u'cash', 'NN'), (u'Bank', 'NN'), (u'Amount', 'nn'), (u'1000', 'CD'), (u'00', 'CD'),
            (u'Balance', 'NN'), (u'1000', 'CD'), (u'0010', 'CD'), (u'1', 'CD'), (u'950913', 'CD'), (u'1', 'CD'),
            (u'Pisek', 'NNP'), (u'south', 'NN'), (u'Bohemia', 'NNP'), (u'Type', 'NN'), (u'Credit', 'NN'),
            (u'Operation', 'NN'), (u'collection', 'NN'), (u'from', 'IN'), (u'another', 'DT'), (u'bank', 'NN'),
            (u'Bank', 'NN'), (u'AB', 'None'), (u'Amount', 'NN'), (u'3679', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'),
            (u'22714', 'CD'), (u'3010000', 'CD'), (u'34', 'CD'), (u'960930', 'CD'), (u'42', 'CD'), (u'Frydek', 'NNP'),
            (u'Mistek', 'NNP'), (u'north', 'NN'), (u'Moravia', 'NNP'), (u'Type', 'NN'), (u'withdrawal', 'NN'),
            (u'Operation', 'NN'), (u'withdrawal', 'NN'), (u'in', 'IN'), (u'cash', 'NN'), (u'stands', 'NNS'),
            (u'for', 'IN'), (u'payment', 'NN'), (u'for', 'IN'), (u'statement', 'NN'), (u'Bank', 'NN'),
            (u'Amount', 'NN'), (u'30', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'), (u'62953', 'CD'),
            (u'60100008', 'CD'),
            (u'342', 'CD'), (u'970310', 'CD'), (u'419', 'CD'), (u'Zlin', 'NNP'), (u'south', 'NN'), (u'Moravia', 'NNP'),
            (u'Type', 'NN'), (u'withdrawal', 'NN'), (u'Operation', 'NN'), (u'remittance', 'NN'), (u'to', 'TO'),
            (u'another', 'DT'), (u'bank', 'NN'), (u'Bank', 'NN'), (u'KL', 'None'), (u'Amount', 'NN'), (u'2332', 'CD'),
            (u'00', 'CD'), (u'Balance', 'NN'), (u'16158', 'CD'), (u'00100009', 'CD'), (u'342', 'CD'),
            (u'970410', 'CD'),
            (u'419', 'CD'), (u'Zlin', 'NNP'), (u'south', 'NN'), (u'Moravia', 'NNP'), (u'Type', 'NN'),
            (u'withdrawal', 'NN'), (u'Operation', 'NN'), (u'remittance', 'NN'), (u'to', 'TO'), (u'another', 'DT'),
            (u'bank', 'NN'), (u'Bank', 'NN'), (u'KL', 'None'), (u'Amount', 'NN'), (u'2332', 'CD'), (u'00', 'CD'),
            (u'Balance', 'NN'), (u'17357', 'CD'), (u'2010001', 'CD'), (u'34', 'CD'), (u'961031', 'CD'), (u'42', 'CD'),
            (u'Frydek', 'NNP'), (u'Mistek', 'NNP'), (u'north', 'NN'), (u'Moravia', 'NNP'), (u'Type', 'NN'),
            (u'withdrawal', 'NN'), (u'Operation', 'NN'), (u'withdrawal', 'NN'), (u'in', 'IN'), (u'cash', 'NN'),
            (u'stands', 'NNS'), (u'for', 'IN'), (u'payment', 'NN'), (u'for', 'IN'), (u'statement', 'NN'),
            (u'Bank', 'NN'), (u'Amount', 'NN'), (u'30', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'), (u'34441', 'CD'),
            (u'10100010', 'CD'), (u'342', 'CD'), (u'970510', 'CD'), (u'419', 'CD'), (u'Zlin', 'NNP'), (u'south', 'NN'),
            (u'Moravia', 'NNP'), (u'Type', 'NN'), (u'withdrawal', 'NN'), (u'Operation', 'NN'), (u'remittance', 'NN'),
            (u'to', 'TO'), (u'another', 'DT'), (u'bank', 'NN'), (u'Bank', 'NN'), (u'KL', 'None'), (u'Amount', 'NN'),
            (u'2332', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'), (u'16475', 'CD'), (u'90100011', 'CD'), (u'342', 'CD'),
            (u'970610', 'CD'), (u'419', 'CD'), (u'Zlin', 'NNP'), (u'south', 'NN'), (u'Moravia', 'NNP'),
            (u'Type', 'NN'),
            (u'withdrawal', 'NN'), (u'Operation', 'NN'), (u'remittance', 'NN'), (u'to', 'TO'), (u'another', 'DT'),
            (u'bank', 'NN'), (u'Bank', 'NN'), (u'KL', 'None'), (u'Amount', 'NN'), (u'2332', 'CD'), (u'00', 'CD'),
            (u'Balance', 'NN'), (u'17694', 'CD'), (u'60100012', 'CD'), (u'342', 'CD'), (u'970710', 'CD'),
            (u'419', 'CD'),
            (u'Zlin', 'NNP'), (u'south', 'NN'), (u'Moravia', 'NNP'), (u'Type', 'NN'), (u'withdrawal', 'NN'),
            (u'Operation', 'NN'), (u'remittance', 'NN'), (u'to', 'TO'), (u'another', 'DT'), (u'bank', 'NN'),
            (u'Bank', 'NN'), (u'KL', 'None'), (u'Amount', 'NN'), (u'2332', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'),
            (u'18918', 'CD'), (u'30100013', 'CD'), (u'342', 'CD'), (u'970810', 'CD'), (u'419', 'CD'), (u'Zlin', 'NNP'),
            (u'south', 'NN'), (u'Moravia', 'NNP'), (u'Type', 'NN'), (u'withdrawal', 'NN'), (u'Operation', 'NN'),
            (u'remittance', 'NN'), (u'to', 'TO'), (u'another', 'DT'), (u'bank', 'NN'), (u'Bank', 'NN'), (u'KL', 'None'),
            (u'Amount', 'NN'), (u'2332', 'CD'), (u'00', 'CD'), (u'Balance', 'NN'), (u'19647', 'CD'), (u'10', 'CD')]

# resultados.append(verifier)
# print tabulate(resultados, headers=[])

all = 217
onlyNN = 94
#
# # del resultados[-1]
# for r in resultados:
#     if (r[0] == 'DefaultPOSTagger (Only nouns)' or r[0] == 'RegexpTagger using backoff = DefaultTagger, only \'NN\''):
#         print r[0] + ": obtained: " + str(
#             len([i for i, j in zip(verifier, r) if i == j])) + " expected: 94 acurancy: " + str(
#             (float(len([i for i, j in zip(verifier, r) if i == j])) / onlyNN) * 100) + " %"
#     else:
#         print r[0] + ": obtained: " + str(
#             len([i for i, j in zip(verifier, r) if i == j])) + " expected: 217 acurancy: " + str(
#             (float(len([i for i, j in zip(verifier, r) if i == j])) / all) * 100) + " %"


# for r in resultados:
#     print float(len(set(verifier).intersection(r)))/217 * 100


# print "\n" + str(len(verifier)-1)


#lingpipe

totest = ["MarkovModel" , ('1', 'CD'), ('1', 'CD'), ('950324', 'CD'), ('1', 'CD'), ('Pisek', 'NP'), ('south', 'NR'), ('Bohemia', 'NP'),
          ('Type', 'NN'), ('Credit', 'NN'), ('Operation', 'NN'), ('credit', 'NN'), ('in', 'IN'), ('cash', 'NN'),
          ('Bank', 'NN'), ('Amount', 'NN'), ('1000', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('1000', 'CD'),
          ('0010', 'CD'), ('1', 'CD'), ('950913', 'CD'), ('1', 'CD'), ('Pisek', 'NP'), ('south', 'NR'),
          ('Bohemia', 'NP'), ('Type', 'NN'), ('Credit', 'NN'), ('Operation', 'NN'), ('collection', 'NN'),
          ('from', 'IN'), ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'), ('AB', 'NN'), ('Amount', 'NN'),
          ('3679', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('22714', 'CD'), ('3010000', 'CD'), ('34', 'CD'),
          ('960930', 'CD'), ('42', 'CD'), ('Frydek', 'NP'), ('Mistek', 'NP'), ('north', 'NR'), ('Moravia', 'NP'),
          ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'), ('withdrawal', 'NN'), ('in', 'IN'), ('cash', 'NN'),
          ('stands', 'VBZ'), ('for', 'IN'), ('payment', 'NN'), ('for', 'IN'), ('statement', 'NN'), ('Bank', 'NN'),
          ('Amount', 'NN'), ('30', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('62953', 'CD'), ('60100008', 'CD'),
          ('342', 'CD'), ('970310', 'CD'), ('419', 'CD'), ('Zlin', 'NP'), ('south', 'NR'), ('Moravia', 'NP'),
          ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'), ('remittance', 'NN'), ('to', 'IN'),
          ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'), ('KL', 'NP$'), ('Amount', 'NN'), ('2332', 'CD'),
          ('00', 'CD'), ('Balance', 'NN'), ('16158', 'CD'), ('00100009', 'CD'), ('342', 'CD'), ('970410', 'CD'),
          ('419', 'CD'), ('Zlin', 'NP'), ('south', 'NR'), ('Moravia', 'NP'), ('Type', 'NN'), ('withdrawal', 'NN'),
          ('Operation', 'NN'), ('remittance', 'NN'), ('to', 'IN'), ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'),
          ('KL', 'NP$'), ('Amount', 'NN'), ('2332', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('17357', 'CD'),
          ('2010001', 'CD'), ('34', 'CD'), ('961031', 'CD'), ('42', 'CD'), ('Frydek', 'NP'), ('Mistek', 'NP'),
          ('north', 'NR'), ('Moravia', 'NP'), ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'),
          ('withdrawal', 'NN'), ('in', 'IN'), ('cash', 'NN'), ('stands', 'VBZ'), ('for', 'IN'), ('payment', 'NN'),
          ('for', 'IN'), ('statement', 'NN'), ('Bank', 'NN'), ('Amount', 'NN'), ('30', 'CD'), ('00', 'CD'),
          ('Balance', 'NN'), ('34441', 'CD'), ('10100010', 'CD'), ('342', 'CD'), ('970510', 'CD'), ('419', 'CD'),
          ('Zlin', 'NP'), ('south', 'NR'), ('Moravia', 'NP'), ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'),
          ('remittance', 'NN'), ('to', 'IN'), ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'), ('KL', 'NP$'),
          ('Amount', 'NN'), ('2332', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('16475', 'CD'), ('90100011', 'CD'),
          ('342', 'CD'), ('970610', 'CD'), ('419', 'CD'), ('Zlin', 'NP'), ('south', 'NR'), ('Moravia', 'NP'),
          ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'), ('remittance', 'NN'), ('to', 'IN'),
          ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'), ('KL', 'NP$'), ('Amount', 'NN'), ('2332', 'CD'),
          ('00', 'CD'), ('Balance', 'NN'), ('17694', 'CD'), ('60100012', 'CD'), ('342', 'CD'), ('970710', 'CD'),
          ('419', 'CD'), ('Zlin', 'NP'), ('south', 'NR'), ('Moravia', 'NP'), ('Type', 'NN'), ('withdrawal', 'NN'),
          ('Operation', 'NN'), ('remittance', 'NN'), ('to', 'IN'), ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'),
          ('KL', 'NP$'), ('Amount', 'NN'), ('2332', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('18918', 'CD'),
          ('30100013', 'CD'), ('342', 'CD'), ('970810', 'CD'), ('419', 'CD'), ('Zlin', 'NP'), ('south', 'NR'),
          ('Moravia', 'NP'), ('Type', 'NN'), ('withdrawal', 'NN'), ('Operation', 'NN'), ('remittance', 'NN'),
          ('to', 'IN'), ('another', 'DT'), ('bank', 'NN'), ('Bank', 'NN'), ('KL', 'NP$'), ('Amount', 'NN'),
          ('2332', 'CD'), ('00', 'CD'), ('Balance', 'NN'), ('19647', 'CD'), ('10', 'CD')]


# print totest[0] + ": obtained: " + str(
#             len([i for i, j in zip(verifier, totest) if i == j])) + " expected: 217 acurancy: " + str(
#             (float(len([i for i, j in zip(verifier, totest) if i == j])) / all) * 100) + " %"

#opennlp

verifier_2 = [v[1] for v in verifier]
del verifier_2[0]

maxent =     ['CD', 'CD', 'CD', 'CD', 'NNP', 'NN', 'NNP', 'NNP', 'NNP', 'NNP', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'NN', 'NNP', 'NNP', 'NNP', 'NNP', 'NN', 'IN', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'IN', 'NN', 'NNS', 'IN', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'JJ', 'CD', 'NNP', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'IN', 'NN', 'NNS', 'IN', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'IN', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD']
perceptron = ['CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NNP', 'NNP', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', '``', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NNP', 'NNP', 'NN', 'IN', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'IN', 'NN', 'NNS', 'IN', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NNP', '``', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'IN', 'NN', 'NNS', 'IN', 'NN', 'IN', 'NN', 'NNP', 'NNP', 'CD', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NN', 'NN', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NNP', '``', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NNP', '``', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD', 'CD', 'CD', 'CD', 'NNP', 'RB', 'NNP', 'NNP', 'NN', 'NNP', '``', 'TO', 'DT', 'NN', 'NNP', 'NNP', 'NNP', '``', 'CD', 'NNP', 'CD', 'CD']

print verifier_2

print "MAXENT: obtained: " + str(
            len([i for i, j in zip(verifier_2, maxent) if i == j])) + " expected: 217 acurancy: " + str(
            (float(len([i for i, j in zip(verifier_2, maxent) if i == j])) / all) * 100) + " %"

print "PERCEPTRON: obtained: " + str(
            len([i for i, j in zip(verifier_2, perceptron) if i == j])) + " expected: 217 acurancy: " + str(
            (float(len([i for i, j in zip(verifier_2, perceptron) if i == j])) / all) * 100) + " %"