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
CORPUS_ORIGIN_PATH = os.path.dirname(os.getcwd()) + "/corpus/detroit.txt"
CORPUS_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/processed_corpus/processed_text.txt"
CORPUS_TAG_FILE_PATH = os.path.dirname(os.getcwd()) + "/corpus/processed_corpus/tags.txt"


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


def origin_collection_tokenized():
    origin_collection = []
    for token in WhitespaceTokenizer().tokenize(readfile(CORPUS_ORIGIN_PATH).replace("\n", ""))[:-1]:
        listtoken = token.split("_")
        origin_collection.append((listtoken[0], listtoken[1]))
    return origin_collection


def extra_condition(condition, param):
    return True if condition is None else condition == param


def calculate_total(condition):
    return sum(1 for i in range(0, len(corpus_origin) - 1) if corpus_origin[i][1] == condition)


def compare_tagger_with_default(tagged, condition=None):
    obtained = sum(1 for i in range(0, len(tagged) - 1) if
                   tagged[i][1] == corpus_origin[i][1] and extra_condition(condition, tagged[i][1]))

    total = len(corpus_origin) if condition is None else calculate_total(condition)
    print "Total {}, Obtained {}, Accuracy {:.2f} %".format(total, obtained, obtained / float(total) * 100)


class TestingTaggers:

    @timeit
    def test_standar_postagger(self):
        compare_tagger_with_default(tag.pos_tag(corpus))

    @timeit
    def test_affix_tagger(self):
        compare_tagger_with_default(tag.AffixTagger(train=trained_collection).tag(corpus))

    @timeit
    def test_default_postagger(self):
        compare_tagger_with_default(tag.DefaultTagger('NN').tag(corpus), condition='NN')

    @timeit
    def test_classifierbased_postagger(self):
        compare_tagger_with_default(tag.ClassifierBasedPOSTagger(train=trained_collection).tag(corpus))

    # Esto de momento no es de utilidad, puesto que lo que hace es establecer un tagger inicial y una serie de reglas
    # de sustitucion de etiquetas y luego las aplica mediante el brilltagger de una manera 'eficiente'
    @timeit
    def test_brill_tagger(self):
        default_tag = tag.DefaultTagger('NN')
        tag_rule = [tbl.rule.TagRule('NN', 'NN')]
        compare_tagger_with_default(tag.BrillTagger(default_tag, tag_rule).tag(corpus))

    @timeit
    def test_unigram_tagger(self):
        compare_tagger_with_default(tag.UnigramTagger(train=trained_collection).tag(corpus))

    @timeit
    def test_bigram_tagger(self):
        t0 = tag.UnigramTagger(train=trained_collection)
        compare_tagger_with_default(tag.BigramTagger(train=trained_collection, backoff=t0).tag(corpus))

    @timeit
    def test_trigram_tagger(self):
        t0 = tag.UnigramTagger(train=trained_collection)
        compare_tagger_with_default(tag.TrigramTagger(train=trained_collection, backoff=t0).tag(corpus))

    @timeit
    def test_ngram_tagger(self):
        t0 = tag.UnigramTagger(train=trained_collection)
        compare_tagger_with_default(tag.NgramTagger(5, train=trained_collection, backoff=t0).tag(corpus))

    @timeit
    def test_regexp_tagger(self):
        t0 = nltk.DefaultTagger('NN')
        compare_tagger_with_default(tag.RegexpTagger({"NN"}, backoff=t0).tag(corpus), condition="NN")

    @timeit
    # requiere "pip install python-crfsuite"
    def test_crft_tagger(self):
        crft = tag.CRFTagger(verbose=True)
        crft.train(trained_collection, 'model.crf.tagger')

    # GRAFOS -> de momento no nos interesa
    @timeit
    def test_hidden_markovmodel_tagger(self):
        # tag.HiddenMarkovModelTagger(symbols=,states=,transitions=,outputs=,priors=,transform=)
        pass

    @timeit
    # TODO VER EL FALLO DE BROKEN PIPE
    # descargar https://code.google.com/p/hunpos/downloads/list
    def test_hunpos_tagger(self):
        os.environ['HUNPOS_TAGGER'] = os.getcwd() + '/models/hunpos/'
        hunpos = tag.HunposTagger('hunpos-tag', encoding='utf-8')
        compare_tagger_with_default(hunpos.tag(corpus))

    # descargar : http://ronan.collobert.com/senna/download.html
    # puede analizar como mucho 1024 tokens totales, para aumentar este numero hay que ir a SENNA_main.c
    # y cambiar la macro MAX_SENTENCE_SIZE. No ha surtido efecto cambiandolo y recompilandolo.
    @timeit
    def test_senna_tagger(self):
        tagger = tag.SennaTagger(os.getcwd() + '/models/senna/')
        tokens = readfile(CORPUS_FILE_PATH).encode('utf-8').split()
        result = []

        for i in xrange(0, len(tokens) - 1, 200):
            if (i - len(tokens)) < 200:
                result.append(tagger.tag(tokens[i:]))
                print str(i)
            else:
                result.append(tagger.tag(tokens[i:i + 200]))
                print str(i + 200)

                # Error el maximo de tokens

    # descargar : http://ronan.collobert.com/senna/download.html
    # pasa lo mismo que el anterior
    @timeit
    def test_senna_chunk_tagger(self):
        compare_tagger_with_default(tag.SennaChunkTagger(os.getcwd() + '/models/senna/').tag(corpus))

    # descargar : http://ronan.collobert.com/senna/download.html
    # pasa lo mismo que el anterior
    @timeit
    def test_senna_ner_tagger(self):
        compare_tagger_with_default(tag.SennaNERTagger(os.getcwd() + '/models/senna/').tag(corpus))

    # @timeit
    # # anyadir fichero stanfor-ner.jar
    # No es un pos tagger en si, es un tagger que por ejemplo detecta nombres de ciudades, organizaciones, etc
    def test_stanford_ner_tagger(self):
        model = os.getcwd() + "/models/stanford/english.all.3class.distsim.crf.ser.gz"
        nertagger_jar = os.getcwd() + "/models/stanford/stanford-ner.jar"
        print tag.StanfordNERTagger(model, path_to_jar=nertagger_jar).tag(corpus)
        # compare_tagger_with_default(tag.StanfordNERTagger(model, path_to_jar=jar).tag(corpus))

    @timeit
    # anyadir fichero stanford-postagger.jar
    def test_stanford_postagger(self):
        model = os.getcwd() + "/models/stanford/english-bidirectional-distsim.tagger"
        postagger_jar = os.getcwd() + "/models/stanford/stanford-postagger.jar"
        compare_tagger_with_default(tag.StanfordPOSTagger(model, path_to_jar=postagger_jar).tag(corpus))

    @timeit
    # anyadir fichero stanford-tagger.jar y el model
    # este es el punto de entrada al Stanford-ner o Stanford-postagger
    def test_stanfor_tagger(self):
        model = os.getcwd() + "/models/stanford/english-bidirectional-distsim.tagger"
        postagger_jar = os.getcwd() + "/models/stanford/stanford-postagger.jar"
        compare_tagger_with_default(tag.StanfordTagger(model, path_to_jar=postagger_jar).tag(corpus))

    @timeit
    def test_tnt_postagger(self):
        tnt_tagger = tag.TnT(Trained=True)
        tnt_tagger.train(trained_collection)

        compare_tagger_with_default(tnt_tagger.tag(corpus))

    def testing_all(self):
        self.test_standar_postagger()
        self.test_affix_tagger()
        self.test_default_postagger()
        self.test_classifierbased_postagger()
        self.test_brill_tagger()
        self.test_unigram_tagger()
        self.test_bigram_tagger()
        self.test_trigram_tagger()
        self.test_ngram_tagger()
        self.test_regexp_tagger()
        self.test_crft_tagger()
        self.test_hidden_markovmodel_tagger()
        self.test_hunpos_tagger()
        self.test_senna_tagger()
        self.test_senna_chunk_tagger()
        self.test_senna_ner_tagger()
        self.test_stanford_ner_tagger()
        self.test_stanford_postagger()
        self.test_stanfor_tagger()
        self.test_tnt_postagger()


trained_collection = train_collection()
corpus = WhitespaceTokenizer().tokenize(readfile(CORPUS_FILE_PATH))
corpus_origin = origin_collection_tokenized()

testing = TestingTaggers()
testing.testing_all()