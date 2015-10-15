from itertools import chain
import string
import datetime
from nltk import FreqDist, NaiveBayesClassifier
from nltk.corpus import stopwords, CategorizedPlaintextCorpusReader

__author__ = 'ruben'

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


@timeit
def nltk():
    #### FOR TRAINING DATA ####
    stop = stopwords.words('spanish')

    # Reads the training data.
    traindir = '/Users/ruben/Desktop/Formularios_clasificados/training'
    mr = CategorizedPlaintextCorpusReader(traindir, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*', encoding='utf-8')

    # Converts training data into tuples of [(words,label), ...]
    documents = [([w for w in mr.words(i) if w.lower() not in stop and w not in string.punctuation], i.split('/')[0]) for i
                 in mr.fileids()]
    # Extract training features.
    word_features = FreqDist(chain(*[i for i, j in documents]))
    word_features = word_features.keys()[:100]
    # Assuming that you're using full data set
    # since your test set is different.
    train_set = [({i: (i in tokens) for i in word_features}, tag) for tokens, tag in documents]

    #### TRAINS THE TAGGER ####
    # Train the tagger
    classifier = NaiveBayesClassifier.train(train_set)

    #### FOR TESTING DATA ####
    # Now do the same reading and processing for the testing data.
    testdir = '/Users/ruben/Desktop/Formularios_clasificados/testing'
    mr_test = CategorizedPlaintextCorpusReader(testdir, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*', encoding='utf-8')
    # Converts testing data into tuples of [(words,label), ...]
    test_documents = [
        ([w for w in mr_test.words(i) if w.lower() not in stop and w not in string.punctuation], i.split('/')[0]) for i in
        mr_test.fileids()]
    # Reads test data into features:
    test_set = [({i: (i in tokens) for i in word_features}, tag) for tokens, tag in test_documents]

    correct = 0
    wrong = 0
    #### Evaluate the classifier ####
    for doc, gold_label in test_set:
        tagged_label = classifier.classify(doc)
        if tagged_label == gold_label:
            correct += 1
        else:
            wrong += 1

    print correct, wrong, (float(correct) / wrong + correct)


nltk()