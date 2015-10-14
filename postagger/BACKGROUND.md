## POS Tagging

* **[A comparison of three part-of-speech taggers] (http://stp.lingfil.uu.se/exarb/arch/2009_block_vent.pdf)**: This thesis presents a comparison of three part-of-speech taggers, µ-TBL, TnT and HunPOS

> The three analyzed tools used differents methods for tagging the words. Then we could prove what is the best method for a business documents processing.

* **[100 Best GitHub: POS Tagging] (http://meta-guide.com/software-meta-guide/100-best-github-part-of-speech-tagging/)**: (alt. link) https://github.com/search?q=part-of-speech-tagging

> too many frameworks, but some can be interesting (it is need to be analyzed)

* **[Survey of POS taggers] (http://korpus.dsl.dk/clarin/corpus-doc/pos-survey.pdf)**: This technical report describes WP 2.1’s requirements to part-of-speech (= POS) tagging and provides a survey of existing POS approaches and their suitability. The survey is based on the requirements defined in Section 1. The report finishes with some conclusions on which approach to choose for tagging WP 2.1 corpus texts.

>Of this study can extract the main characteristics of several POSTaggers tools. Each one, has been analyzed by:  availability, features, code, architecture, usability. (Very util link)


* **[Context-less POS tagging with NLTK] (http://sujitpal.blogspot.com.es/2014/08/context-less-pos-tagging-with-nltk.html)**:Last week I was handed an interesting task - flagging non-nouns from single word synonyms for concepts in our Medical Ontology. Now, the Part of Speech (POS) tag is not really an intrinsic attribute of a word - rather, the POS is determined by the context in which the word appears. For example, consider the two sentences - "He had an infectious laugh", where laugh is a Noun, and "He will laugh at the joke", where the same word is now a Verb. However, a word with multiple senses (usually) has one dominant sense, so in the absence of my context, we could call that the word's POS. In order to calculate the dominant POS for words, I decided to use the words in the Brown Corpus, a manually tagged text corpus of about 500 articles. The Brown Corpus is available (after nltk.download()) as part of the Natural Language Processing Toolkit (NLTK).

> Util to extract the top words in a text and therefore util for the tagging processing of words. When we are looking for the top terms of a text, one of the firsts process to do is get the filtered words to choose the type as we want, for example all nouns. However these filter can be wrong due to that an important word can be presented by other type, for example an important noun can be presented as a verb. Therefore the context is very important and is something that is important to keep in mind (@fpromero). Related issues #5 #2 #3.


* **[POS Tagging] (http://aclweb.org/aclwiki/index.php?title=POS_Tagging_%28State_of_the_art%29)**: A collection of most important POS tagger tools. (Must Read)

* **[A good POS tagger in about 200 lines of Python](https://honnibal.wordpress.com/2013/09/11/a-good-part-of-speechpos-tagger-in-about-200-lines-of-python/)**: Relate link - http://honnibal.github.io/spaCy/

----------------

## POS Tagger Frameworks

- **[IMS's TreeTagger] (http://www.ims.uni-stuttgart.de/projekte/corplex/TreeTagger/)**
- ~~**[TnT] (http://www.coli.uni-saarland.de/~thorsten/tnt/)**~~: Implemented on NLTK.
- ~~**[SVMTool] (http://www.lsi.upc.es/~nlp/SVMTool/)**~~ : WTF? :-1:
- **[Stanford Log-linear Part-Of-Speech Tagger](http://nlp.stanford.edu/software/tagger.shtml)**
- **[Apache UIMA Tagger] (http://uima.apache.org/sandbox.html)**
- ~~**[unsupos - Unsupervised Part-ofSpeech Tagging] (http://wortschatz.uni-leipzig.de/~cbiemann/software/unsupos.html)**~~ : WTF? :-1:
- ~~**[Brill Tagger] (https://en.wikipedia.org/wiki/Brill_tagger)**~~: is a type of tagger implemented in NLTK.
- **[Sujit Pal's HMM-based tagger] (http://sujitpal.blogspot.com/2008/11/ir-math-in-java-hmm-based-pos.html)** (Custom NLP Toolkit):
- **[LingPipe] (http://alias-i.com/lingpipe/index.html)**
- **[Jitar](http://github.com/danieldk/jitar)**
- ~~**[µ-TBL] (http://www.ling.gu.se/~lager/mutbl.html)**~~ : SICStus Prolog required :-1: .
- ~~**[HunPOS](https://code.google.com/p/hunpos/)**~~ : implemented on NLTK.
- ~~**[spaCy] (http://honnibal.github.io/spaCy/)**~~: too simple.


------------------

After filter the last results, the libs selected are:

## POS Tagger

- **[IMS's TreeTagger] (http://www.ims.uni-stuttgart.de/projekte/corplex/TreeTagger/)**
- **[Stanford Log-linear Part-Of-Speech Tagger](http://nlp.stanford.edu/software/tagger.shtml)**
- **[Apache UIMA Tagger] (http://uima.apache.org/sandbox.html)**
- **[Sujit Pal's HMM-based tagger] (http://sujitpal.blogspot.com/2008/11/ir-math-in-java-hmm-based-pos.html)** (Custom NLP Toolkit):
- **[LingPipe] (http://alias-i.com/lingpipe/index.html)**
- **[Jitar](http://github.com/danieldk/jitar)**

--------------------

After reading the first comment of [this post](http://www.quora.com/Which-NLP-library-among-the-ones-below-is-most-mature-and-should-be-used-by-a-startup-for-its-NLP-needs). The following POS Tagger list is definitive:

* **[OpenNLP POSTagger] (http://opennlp.apache.org/documentation/manual/opennlp.html#tools.postagger)**
* **[NLTK](www.nltk.org/_modules/nltk/tag.html)** : Implements an interface of some POS Tagger libs. (All in one: brill + brill trainer + tnt + hunpos + stanford + hmm + senna + mapping + crf + sequential + nltk)
* **[LingPipe] (http://alias-i.com/lingpipe/demos/tutorial/posTags/read-me.html)**
