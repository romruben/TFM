# Mallet Framework

## Default props

```
//Test file
TEST_FILE = abs.path + example.txt

//Regex to tokenizer
REGEX = "\\w+";
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
mvn test -Dtestfile=<absolute path of test file>
         -Dregex=<regex to separate tokens>
```
