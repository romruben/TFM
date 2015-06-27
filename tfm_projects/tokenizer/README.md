# Tokenizer

## Frameworks Definition

- **[NLTK Tokenizer](http://www.nltk.org/api/nltk.tokenize.html)**
- **[OpenNLP Tokenizer](http://opennlp.apache.org/documentation/manual/opennlp.html#tools.tokenizer)**
- **[Mallet Tokenizer](http://mallet.cs.umass.edu/api/cc/mallet/extract/Tokenization.html)**
- **[Stanford NLP Tokenizer] (http://nlp.stanford.edu/software/tokenizer.shtml)**
- **[Deeplearning4j’s](https://github.com/deeplearning4j/deeplearning4j/blob/master/deeplearning4j-scaleout/deeplearning4j-nlp/src/main/java/org/deeplearning4j/text/tokenization/tokenizer/Tokenizer.java)**

## Experiment Design

- The execution time
- Memory consumption
- String evaluations:
    * Words with hyphenated compound words (e.g. credit-card)
    * Words with letters and slashes (e.g. insertion/deletion)
    * Words with letters and apostrophes (e.g. Ruben's master thesis)
    * Words with letters and brackets (e.g. CDSS (Clinical Decision support system))
    * Words with letters and numbers (e.g. 12th)
    * Words with numbers and one type of puntuationes (e.g. 1.30483,10)
    * Aritmetical expressions as 8.4-10%
    * A hypertext markup symbol (e.g. &lt)
    * URLs (http://www.smile.uclm.es)
    * Abbreviations (C.D.S.S. / CDSS)
    * Quoted text ("production costs")

Acknowledgement:

* [A Comparison of 13 Tokenizers on MEDLINE](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.216.2433&rep=rep1&type=pdf)
