# Content Search

## Frameworks Definition

* **[Sphinx] (http://sphinxsearch.com/)** : A search engine designed for indexing database content. It natively supports MySQL, PostgreSQL, and XML pipe interfaces. It is written in C++ and has a GPL license.

* **[Apache Solr] (http://lucene.apache.org/solr/)** : Solr is the popular, blazing fast open source enterprise search platform from the Apache Lucene project. Its major features include powerful full-text search, hit highlighting, faceted search, dynamic clustering, database integration, and rich document (e.g., Word, PDF) handling. Solr is highly scalable, providing distributed search and index replication, and it powers the search and navigation features of many of the world's largest internet sites. 

* **[Elastic Search] (http://www.elasticsearch.com/)** : ElasticSearch could be opted if, We want our search solution to be fast, we want a painless setup and a completely free search schema, we want to be able to index data simply using JSON over HTTP, we want our search server to be always available, we want to be able to start with one machine and scale to hundreds, we want real-time search, we want simple multi-tenancy, and we want a solution that is built for the cloud.
* 
## Experiment Design

- The execution time
- Memory consumption
- Tests with 5 queries the number of correct results obtained.
- Stress tests with [JMETER](http://jmeter.apache.org/) or [Gatling](http://gatling.io/)


I will use [Docker] (https://www.docker.com/) for a fast deploy of the infrastructure as elasticsearch, solr, and sphinx. Each one in a docker container.
