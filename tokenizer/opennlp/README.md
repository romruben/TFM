# OpenNLP Tokenizer

## Default props

```
//Test file
TEST_FILE = "example.txt"

//Trained on opennlp training data.
TOKEN_MODEL = "en-token.bin"
```

## Build

```
mvn clean install -DskipTests
```

(-DskipTests, We don't want the tests to run at this moment)

## Execute tests

```
mvn test
```

### Parameterization

All these params are optional.

```
mvn test -Dtestfile=<test file>
         -Dtokenmodel=<Trained on opennlp training data.>
```