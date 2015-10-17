import os

__author__ = 'ruben'

from topia.termextract import extract
extractor = extract.TermExtractor()


path = '/Users/ruben/Desktop/_test'

for dirpath, dirs, files in os.walk(path):
    for f in files:
        fname = os.path.join(dirpath, f)
        if(fname!='.DS_Store'):
            print "fname=", fname
            with open(fname) as pearl:
                text = str(unicode(pearl.read(), errors='ignore'))
                print sorted(extractor(text))[:5]