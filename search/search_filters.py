from django_elasticsearch_dsl_drf.filter_backends import BaseSearchFilterBackend
from django_elasticsearch_dsl_drf.filter_backends.search.query_backends import MatchPhrasePrefixQueryBackend


class PrefixSearchFilterBackend(BaseSearchFilterBackend):
    query_backends = [
        MatchPhrasePrefixQueryBackend
    ]
