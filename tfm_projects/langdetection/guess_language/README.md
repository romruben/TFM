# Guess Language framework

## Installation

Dependencies, install before (if installing for Python 2):

*3to2*
```
sudo pip install 3to2
```


```
cd /tmp/
hg clone ssh://hg@bitbucket.org/spirit/guess_language or https://bitbucket.org/spirit/guess_language/get/0a8285e2752a.zip
cd guess_language/
python setup.py install
cd ../
rm -rf guess_language/
```

## Execution

The default properties are:

* TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/" (files to test)
* LANGUAGES_TO_TEST = "English,Spanish" (languates to test)
* FILES_BY_LANGUAGE = "filesByLanguage.properties" (the language of each test file)
* LANGUAGES_IDS     = "profiles.properties" (identifier of each language e.g. sp = 'Spanish')


The basic execution with these properties is:

```Shell
python guess_language.py
```

If you want to customize these properties, you can do it with the following options:

```Shell
usage: guess_language.py [-h] [-t TESTDIR] [-l LANGUAGES] [-f FILESBYLANG]

Ruben TFM language detection with guess_language.py

optional arguments:
  -h, --help            show this help message and exit
  -t TESTDIR, --testdir TESTDIR
                        testdir
  -l LANGUAGES, --languages LANGUAGES
                        Languages to tests
  -f FILESBYLANG, --filesByLang FILESBYLANG
                        filesByLang
```