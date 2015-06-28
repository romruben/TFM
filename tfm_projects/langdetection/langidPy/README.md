# LangId.py frameworks

## Installation

The first way is via code:

```
cd /tmp/
git clone --bare https://github.com/saffsd/langid.py.git
cd langid.py.git/
python setup.py install
cd ../
rm -rf langid.py.git/
```

the second:

```Shell
pip install langid
```

## Execution

The default properties are:

* TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/" (files to test)
* LANGUAGES_TO_TEST = "English,Spanish" (languates to test)
* FILES_BY_LANGUAGE = "filesByLanguage.properties" (the language of each test file)
* LANGUAGES_IDS     = "profiles.properties" (identifier of each language e.g. sp = 'Spanish')


The basic execution with these properties is:

```Shell
python langidPyTest.py
```

If you want to customize these properties, you can do it with the following options:

```Shell
usage: langidPyTest.py [-h] [-t TESTDIR] [-l LANGUAGES] [-f FILESBYLANG]

Ruben TFM language detection with langid.py

optional arguments:
  -h, --help            show this help message and exit
  -t TESTDIR, --testdir TESTDIR
                        testdir
  -l LANGUAGES, --languages LANGUAGES
                        Languages to tests
  -f FILESBYLANG, --filesByLang FILESBYLANG
                        filesByLang
```