import math
import datetime
from nltk.corpus import stopwords
from textblob import TextBlob as tb

files = ['/Users/ruben/Desktop/_test/contrato.txt', '/Users/ruben/Desktop/_test/extractocuenta.txt',
         '/Users/ruben/Desktop/_test/registromercantil.txt']


custom_stop = ["caja", "efectos", "cobro", "cedente", "cuenta", "cuentas", "remesa", "efecto", "total", "valor", "dia",
               "saldo"]

def get_time():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

def clean(text):
    return ' '.join([word for word in text.split() if word not in stopwords.words("spanish") or word not in custom_stop])

def timeit(method):
    def timed(*args, **kw):
        ts = get_time()
        result = method(*args, **kw)
        te = get_time()

        print '%r %2.2f milliseconds\n' % \
              (method.__name__, te - ts)
        return result

    return timed

bloblist = [tb(clean(str(unicode(open(files[0], 'r').read(), errors='ignore')))),
            tb(clean(str(unicode(open(files[1], 'r').read(), errors='ignore')))),
            tb(clean(str(unicode(open(files[2], 'r').read(), errors='ignore'))))]


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    try:
        re = math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
    except:
        re = 0
    return re


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


@timeit
def total():
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

total()