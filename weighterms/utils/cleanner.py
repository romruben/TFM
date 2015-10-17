import codecs
import re
import enchant

pathdest = '/Users/ruben/Desktop/_test/contrato.txt'
# pathdest = '/Users/ruben/Desktop/_test/extractocuenta.txt'
# pathdest = '/Users/ruben/Desktop/_test/registromercantil.txt'

path = '/Users/ruben/Desktop/_test/dst/con.txt'
# path = '/Users/ruben/Desktop/_test/dst/ext.txt'
# path = '/Users/ruben/Desktop/_test/dst/rem.txt'

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('spanish'))
dict = enchant.Dict("es_ES")

with codecs.open(path, "r", "utf-8") as text_file:
    tokens = word_tokenize(text_file.read().lower())

    tokens = [w for w in tokens
              if not w in stopset
              and re.sub(r'[?|$|.|!|%|,|.|-|(|)|*]',r'',w)
              and len(w)>=3]
    codecs.open(pathdest, "w", "utf-8").write(" ".join(tokens))
