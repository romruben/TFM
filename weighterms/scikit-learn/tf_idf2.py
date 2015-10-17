import datetime
import nltk
import string
import os
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = '/Users/ruben/Desktop/_test'
token_dict = {}


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

for dirpath, dirs, files in os.walk(path):
    for f in files:
        fname = os.path.join(dirpath, f)
        print "fname=", fname
        with open(fname) as pearl:
            text = str(unicode(pearl.read(), errors='ignore'))
            token_dict[f] = text.lower().translate(None, string.punctuation)

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

@timeit
def test():

    tfidf = TfidfVectorizer(tokenizer=tokenize)
    response = tfidf.fit_transform(token_dict.values())

    str = 'all great and precious things are lonely.'
    # response = tfidf.transform([str])
    # print response

    feature_names = tfidf.get_feature_names()
    r = []
    for col in response.nonzero()[1]:
        r.append((feature_names[col],response[0, col]))

    r.sort(key=lambda x: x[1], reverse=True)
    print r[:15]

test()