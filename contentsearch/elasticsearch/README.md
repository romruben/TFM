# Elasticsearch

This README contains a shot guide to install solr, and to create a collection and index files on it (with a only field: the file content).

## Installation

```
cd /var/tmp/
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.6.0.zip
unzip -q elasticsearch-1.6.0.zip
```

## Start Elasticsearch
```
/var/tmp/elasticsearch-1.6.0/bin/elasticsearch
```

## Create a collection
```
solr create -c <COLLECTION_NAME>
```
## Index files
```
/var/tmp/elasticsearch-1.6.0/bin/post -c <COLLECTION_NAME> <TEST_FILES_PATH>
```

## Configuration and Plugins

### Indexed data browser
```
 sudo /var/tmp/elasticsearch-1.6.0/bin/plugin -install OlegKunitsyn/elasticsearch-browser
```
 
* *URL*: [http://localhost:9200/_plugin/browser/?database=test&table=attachment](http://localhost:9200/_plugin/browser/?database=test&table=attachment)

## Uri Search

Example:

```
http://<ENDPOINT>/<INDEX>/_search?q=<FIELD>:<CONTENT>&...&fields=<FILTER BY FIELDS>

http://localhost:9200/test/_search?q=file:motorola&fields=_id
```


[https://www.elastic.co/guide/en/elasticsearch/reference/1.6/search-uri-request.html](https://www.elastic.co/guide/en/elasticsearch/reference/1.6/search-uri-request.html)
