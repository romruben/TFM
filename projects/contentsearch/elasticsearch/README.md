# Elasticsearch

This README contains a shot guide to install solr, and to create a collection and index files on it (with a only field: the file content).

## Installation

cd /var/tmp/
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.6.0.zip
unzip -q elasticsearch-1.6.0.zip

## Start Elasticsearch
/var/tmp/elasticsearch-1.6.0/bin/elasticsearch

## Create a collection
solr create -c <COLLECTION_NAME>

## Index files
/var/tmp/elasticsearch-1.6.0/bin/post -c <COLLECTION_NAME> <TEST_FILES_PATH>


## Configuration and Plugins

### Indexed data browser

 * sudo /var/tmp/elasticsearch-1.6.0/bin/plugin -install OlegKunitsyn/elasticsearch-browser

 * http://localhost:9200/_plugin/browser/?database=test&table=attachment
