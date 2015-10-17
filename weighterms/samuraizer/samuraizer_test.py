import codecs
import os
import datetime
from nltk.corpus import stopwords
import samuraizer

__author__ = 'ruben'

path = '/Users/ruben/Desktop/_test'

custom_stop = ["caja", "efectos", "cobro", "cedente", "cuenta", "cuentas", "remesa", "efecto", "total", "valor", "dia",
               "saldo"]

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
def getwords():
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(dirpath, f)
            if (fname != path+'/.DS_Store'):
                print "fname=", fname
                with codecs.open(fname, "r", "utf-8") as pearl:
                    text = pearl.read()
                    textcle = ' '.join([word for word in text.split() if word not in stopwords.words("spanish") or word not in custom_stop])
                    print samuraizer.extract_keywords(textcle)[:5]



getwords()