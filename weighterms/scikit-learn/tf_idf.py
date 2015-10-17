import codecs
import datetime
import nltk
import string
import os
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = '/Users/ruben/Desktop/_test'
token_dict = {}
stemmer = PorterStemmer()

custom_stop = ["caja", "efectos", "cobro", "cedente", "cuenta", "cuentas", "remesa", "efecto", "total", "valor", "dia",
               "saldo"]


def get_time():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


def clean(text):
    return ' '.join(
        [word for word in text.split() if word not in stopwords.words("spanish") or unicode(word) not in custom_stop])


def timeit(method):
    def timed(*args, **kw):
        ts = get_time()
        result = method(*args, **kw)
        te = get_time()

        print '%r %2.2f milliseconds\n' % \
              (method.__name__, te - ts)
        return result

    return timed


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


for subdir, dirs, files in os.walk(path):
    for file in files:
        if file != ".DS_Store":
            file_path = subdir + os.path.sep + file
            shakes = codecs.open(file_path, 'r')
            text = shakes.read()
            lowers = text.lower()
            # no_punctuation = lowers.replace(string.punctuation, '')
            token_dict[file] = lowers


# this can take some time

@timeit
def test():
    tfidf = TfidfVectorizer(tokenizer=tokenize)
    tfs = tfidf.fit(token_dict.values())
    feature_names = tfidf.get_feature_names()

    result = []
    for col in tfs.nonzero()[1]:
        result.append((feature_names[col], tfs[0, col]))

    result.sort(reverse=False)
    print result[:5]


test()
