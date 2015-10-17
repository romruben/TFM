"""
========================================================
Topics extraction with Non-Negative Matrix Factorization
========================================================

This is a proof of concept application of Non Negative Matrix
Factorization of the term frequency matrix of a corpus of documents so
as to extract an additive model of the topic structure of the corpus.
The output is a list of topics, each represented as a list of terms
(weights are not shown).

The default parameters (n_samples / n_features / n_topics) should make
the example runnable in a couple of tens of seconds. You can try to
increase the dimensions of the problem, but be aware than the time complexity
is polynomial.

"""
from __future__ import print_function

# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck <L.J.Buitinck@uva.nl>
# License: BSD 3 clause
import datetime
from nltk.corpus import stopwords
import os
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.datasets import fetch_20newsgroups


def get_time():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


def timeit(method):
    def timed(*args, **kw):
        ts = get_time()
        result = method(*args, **kw)
        te = get_time()

        print ('%r %2.2f milliseconds\n' % \
        (method.__name__, te - ts))
        return result

    return timed


n_samples = 2000
n_features = 1000
n_topics = 10
n_top_words = 20

# Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
# to filter out useless terms early on: the posts are stripped of headers,
# footers and quoted replies, and common English words, words occurring in
# only one document or in at least 95% of the documents are removed.


def test():
    path = '/Users/ruben/Desktop/_test'

    print("Loading dataset and extracting TF-IDF features...")
    token_dict = {}
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file!=".DS_Store":
                file_path = subdir + os.path.sep + file
                shakes = open(file_path, 'r')
                text = shakes.read()
                lowers = unicode(text.lower(), errors='ignore')
                # no_punctuation = lowers.replace(string.punctuation, '')
                token_dict[file] = lowers

    t0 = time()
    print("Loading dataset and extracting TF-IDF features...")

    vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, max_features=n_features)

    print(type(token_dict.values()))
    tfidf = vectorizer.fit_transform(token_dict)
    print("done in %0.3fs." % (time() - t0))

    # Fit the NMF model
    print("Fitting the NMF model with n_samples=%d and n_features=%d..."
          % (n_samples, n_features))

    nmf = NMF(n_components=5, random_state=1).fit(tfidf)
    print("done in %0.3fs." % (time() - t0))

    feature_names = vectorizer.get_feature_names()

    print(feature_names[:15])

    for topic_idx, topic in enumerate(nmf.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()


test()
