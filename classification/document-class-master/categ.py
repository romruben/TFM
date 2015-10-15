#!/usr/bin/python
# -*-coding:utf-8-*

import codecs
import fnmatch
import os
import datetime

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn import metrics

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import Perceptron

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


################################################################################
# Functions
################################################################################

def features(words):
    features = {}
    for word in words:
        features[word] = True

    # print features
    return features


def buildSet(t_set, docs):
    for doc in docs:
        t_set.append(
            (features(codecs.open(doc, 'r', errors='ignore', encoding='utf-8').read().split(" ")), doc.split("/")[6]))
        # print features(nltk.word_tokenize(codecs.open(doc, 'r', errors='ignore', encoding='utf-8').read()))


def classify(features_selection, classification_method):
    pipeline = []

    if features_selection == "tf-idf":
        pipeline.append((features_selection, TfidfTransformer()))
    elif features_selection == "chi2":
        pipeline.append((features_selection, SelectKBest(chi2, k='all')))

    if classification_method == "M-NB":
        pipeline.append((classification_method, MultinomialNB()))
    if classification_method == "B-NB":
        pipeline.append((classification_method, BernoulliNB()))
    elif classification_method == "SVM":
        pipeline.append((classification_method, LinearSVC()))
    # elif classification_method == "Decision Tree":
    #	pipeline.append((classification_method, DecisionTreeClassifier()))
    #	classifier = SklearnClassifier(Pipeline(pipeline),sparse=False)
    elif classification_method == "KNN":
        pipeline.append((classification_method, KNeighborsClassifier()))
    elif classification_method == "Rocchio":
        pipeline.append((classification_method, NearestCentroid()))
    elif classification_method == "Perceptron":
        pipeline.append((classification_method, Perceptron()))

    return SklearnClassifier(Pipeline(pipeline))


def getResults(classifier, test_set, precisions, recalls):
    test = []
    truth = []
    for (feat, cat) in test_set:
        test.append(feat)
        truth.append(cat)
    categories = classifier.classify_many(test)

    precision = metrics.precision_score(truth, categories)
    #
    # # recall = metrics.recall_score(truth, categories)
    # # fmeasure = 2.0 * (precision * recall) / (precision + recall)
    #
    # precisions.append(precision)
    # # recalls.append(recall)
    #
    print '\tPrecision =', precision
    # # print '\tRecall =', recall
    # # print '\tF-measure =', fmeasure, '\n'
    # precision, recall, fscore, support = score(truth, categories)

    # precision2 = precision_score(truth, categories)
    # print('precision: {}'.format(precision))
    # print('precision: {}'.format(precision))
    # print('recall: {}'.format(recall))
    # print('fscore: {}'.format(fscore))
    # print('support: {}'.format(support))


################################################################################



################################################################################
# Main
################################################################################

def givemyfiles(dir):
    matches = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, '*.txt'):
            matches.append(os.path.join(root, filename))
    return matches


@timeit
def testcateg():
    print 'Loading docs...'
    training = "/Users/ruben/Desktop/Formularios_clasificados/training/"
    testing = "/Users/ruben/Desktop/Formularios_clasificados/testing/"

    train_docs = givemyfiles(training)
    test_docs = givemyfiles(testing)

    print 'Building training set...'
    training_set = []
    buildSet(training_set, train_docs)

    print 'Building test set...'
    test_set = []
    buildSet(test_set, test_docs)

    precisions_tfidf = []
    recalls_tfidf = []
    precisions_chi2 = []
    recalls_chi2 = []

    print '\n################################################################################'
    print '# TF-IDF'
    print '################################################################################\n'

    print 'Training the Multinomial Naive Bayes classifier...'
    classifier = classify("tf-idf", "M-NB")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the Bernoulli Naive Bayes classifier...'
    classifier = classify("tf-idf", "B-NB")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the SVM classifier...'
    classifier = classify("tf-idf", "SVM")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the K-nearest Neighbors classifier...'
    classifier = classify("tf-idf", "KNN")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the Rocchio\'s classifier...'
    classifier = classify("tf-idf", "Rocchio")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the Perceptron classifier...'
    classifier = classify("tf-idf", "Perceptron")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_tfidf, recalls_tfidf)

    print 'Training the Decision Tree classifier...'
    classifier = classify("tf-idf", "Decision Tree")
    classifier.train(training_set)
    getResults(classifier, test_set)

    print '\n################################################################################'
    print '# Chi squared'
    print '################################################################################\n'

    print 'Training the Bernoulli Naive Bayes classifier...'
    classifier = classify("chi2", "B-NB")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Training the Multinomial Naive Bayes classifier...'
    classifier = classify("chi2", "M-NB")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Training the SVM classifier...'
    classifier = classify("chi2", "SVM")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Training the K-nearest Neighbors classifier...'
    classifier = classify("chi2", "KNN")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Training the Rocchio\'s classifier...'
    classifier = classify("chi2", "Rocchio")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Training the Perceptron classifier...'
    classifier = classify("chi2", "Perceptron")
    classifier.train(training_set)
    getResults(classifier, test_set, precisions_chi2, recalls_chi2)

    print 'Displaying plot...'
    # plt.plot(recalls_tfidf, precisions_tfidf, 'ro', label='Tf-idf')
    # plt.plot(recalls_chi2, precisions_chi2, 'b^', label='Chi2')
    # plt.ylabel('Precision')
    # plt.xlabel('Recall')
    # methods = ["M-NB", "B-NB", "SVM", "KNN", "Rocchio", "Perceptron"]
    # for i in range(len(precisions_tfidf)):
    #     plt.text(recalls_tfidf[i], precisions_tfidf[i], methods[i])
    # for i in range(len(precisions_chi2)):
    #     plt.text(recalls_chi2[i], precisions_chi2[i], methods[i])
    # plt.legend(loc='upper left')
    # plt.show()

    ################################################################################


testcateg()
