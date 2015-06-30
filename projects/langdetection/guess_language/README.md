# Guess Language framework

## Execution

The default properties are:

```
TEST_FILES_DIR     = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/" (_files to test_)
LANGUAGES_TO_TEST  = "English,Spanish" (_languates to test_)
FILES_BY_LANGUAGE  = "resources/filesByLanguage.properties" (_the language of each test file_)
LANGUAGES_IDS      = "resources/profiles.properties" (_identifier of each language e.g. sp = 'Spanish'_)
```

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
