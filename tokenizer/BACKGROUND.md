In the first documentation round, i found the following info of Tokenizer:

## Tokenizer

* **[A Comparison of 13 Tokenizers on MEDLINE] (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.216.2433&rep=rep1&type=pdf)** : This report describes a study on tokenization of MEDLINE abstracts by 13 different software packages that are freely available.

> Of this study it could extract 13 tools and some ideas for experiments design to analyze tokenizer tools.


* **[Towards Tokenization Evaluation] (https://perso.limsi.fr/gabrieli/CV/Publis/Articles/habert-et-al98b.pdf)**

>This study does a  comparative evaluation of Tokenizer tools based on quantitative methods. From it, I could extract some ideas for the experiment design with quantitative approach.

* **[Tweet NLP] (http://www.ark.cs.cmu.edu/TweetNLP/)**: Just another tokenizer tool.

* **[NLP Stack](https://github.com/allenai/nlpstack)**: Basic stack of NLP tools.

> Very important link, due to it is a NLP stack that uses many frameworks with differents languages over a facade (stack) written in Python.

---------------

Next, it show a provisional list of Tokenizer frameworks. The main aim is that this list can evolve, from a big list of tools, to a minimum number of tools (5-6 max), limiting the scope of the proofs.

## Tokenizer

- **[NLTK Tokenizer](http://www.nltk.org/api/nltk.tokenize.html)**
- **[OpenNLP Tokenizer](http://opennlp.apache.org/documentation/manual/opennlp.html#tools.tokenizer)**
- **[Mallet Tokenizer](http://mallet.cs.umass.edu/api/cc/mallet/extract/Tokenization.html)**
- ~~**[Specialist NLP Tokenizer](http://lsg3.nlm.nih.gov/LexSysGroup/Projects/textTools/current/apiDoc/gov/nih/nlm/nls/nlp/tokenizer/package-frame.html)**~~ : Only for biomedical domain.
- ~~**Gump tokenizer**~~ : No doc.
- ~~**Dan Melamed’s tokenizer**~~ : No doc.
- ~~**Qtoken**~~ : No doc.
- ~~**UIUC word splitter**~~ : No doc.
- ~~**LT TTT tokenizer**~~ : no maintained since 2000.
- ~~**MedPost tokenizer**~~ : there aren't sufficient info
- ~~**Brill’s POS tagger**~~
- **[Stanford NLP Tokenizer] (http://nlp.stanford.edu/software/tokenizer.shtml)**
- ~~**MXPOST tagger**~~
- ~~**[Tweet NLP](https://github.com/brendano/ark-tweet-nlp/blob/master/src/cmu/arktweetnlp/Twokenize.java)**~~: too oriented to tweets.
- **[Deeplearning4j’s](https://github.com/deeplearning4j/deeplearning4j/blob/master/deeplearning4j-scaleout/deeplearning4j-nlp/src/main/java/org/deeplearning4j/text/tokenization/tokenizer/Tokenizer.java)**
- **[spaCy] (http://honnibal.github.io/spaCy/)**
