from elasticsearch import Elasticsearch 
from elasticsearch import helpers
from elasticsearch_dsl.connections import connections
import csv

filename = 'final.csv'


es = Elasticsearch(hosts=["http://18.188.160.132:9200"], timeout=5000) # Define a default Elasticsearch client

with open(filename, "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='tweets', doc_type='mytweets')
