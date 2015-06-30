# LC4J Framework

## Default props

```
//Standard profile Directory
PROFILE_DIR = "/var/tmp/tfm/language_detection/frameworks/lc4j/models/";

//Directory in which are the files to test
TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/lc4j/testfiles/";

//Maps the pair languages id with theirs long name
FILES_BY_LANGUAGE = "src/test/resources/filesByLanguage.properties";

//Languages to tests
LANGUAGES_T0_TEST = "English,Spanish";
```

## Build

```
mvn clean install -DskipTests
```

(-DskipTests, We don't want the tests to run at this moment)

## Execute tests

```
mvn test -Dtest=TestWithDefaultProfiles
```

### Parameterization

All these params are optional.

```
mvn test -Dtest=<testName>
         -Dprofile.dir=<Changes the Profile Directory>
         -Dtest.dir=<Changes the directory in which are the tests files>
         -Dsupported.languages=<Defining the languages to detect, e.g. all Spanish,English>
```

The last option: -Dsupported.languages is very util in the case of we want to test
if the framework, is detecting a concrete language in all documents tagged with that language.
