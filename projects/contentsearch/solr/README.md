# Solr

This README contains a shot guide to install solr, and to create a collection and index files on it (with a only field: the file content).

## Installation
```
cd /var/tmp/
wget http://download.nextag.com/apache//lucene/solr/5.2.1/solr-5.2.1.zip
unzip -q solr-5.2.1.zip
cd solr-5.2.1/
````

## Start Solr
```
/var/tmp/solr-5.2.1/bin/solr start -e cloud -noprompt
````

## Create a collection
```
/var/tmp/solr-5.2.1/bin/solr create -c <COLLECTION_NAME>
````

## Index files
```
/var/tmp/solr-5.2.1/bin/post -c <COLLECTION_NAME> <TEST_FILES_PATH>
```

## Search a content

```
http://localhost:8983/solr/<COLLECTION>/query?q=<QUERY>&fl=<FILTER BY FIELD>
```

Example:

```
http://localhost:8983/solr/tfm/query?q=motorola&fl=id
````
