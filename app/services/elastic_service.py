from elasticsearch import Elasticsearch
from app.config import settings

elastic = Elasticsearch(settings.ELASTICSEARCH_HOST)
