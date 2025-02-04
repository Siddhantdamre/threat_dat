from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_log(index_name, log_data):
    """
    Index log data into Elasticsearch.
    :param index_name: Name of the Elasticsearch index.
    :param log_data: Dictionary containing log information.
    """
    es.index(index=index_name, document=log_data)

def search_logs(index_name, query):
    """
    Search for logs in Elasticsearch.
    :param index_name: Name of the Elasticsearch index.
    :param query: Elasticsearch query.
    :return: Search results.
    """
    response = es.search(index=index_name, query=query)
    return response["hits"]["hits"]
