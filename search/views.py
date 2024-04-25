from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from lost_objects.models import HeritageLostObject
from .serializers import HeritageLostObjectDocumentSerializer
from .documents import HeritageLostObjectDocument
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend, FilteringFilterBackend, \
    OrderingFilterBackend
from .search_filters import PrefixSearchFilterBackend
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination


class HeritageLostObjectDocumentView(DocumentViewSet):
    queryset = HeritageLostObject.objects.all()
    document = HeritageLostObjectDocument
    serializer_class = HeritageLostObjectDocumentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        PrefixSearchFilterBackend,
        FilteringFilterBackend,
        OrderingFilterBackend,
    ]

    search_fields = {
        'date_reg.search': None,
        'reg_number.search': None,
        'name': None,
        'classification': None,
        'category': None,
        'state': None,
        'height': None,
        'width': None,
        'length': None,
        'weight': None
    }

    ordering_fields = {
        'date_reg': 'date_reg',
        'reg_number': 'reg_number',
        'name': 'name.raw',
        'classification': 'classification.raw',
        'category': 'category.raw',
        'state': 'state.raw',
        'height': 'height.raw',
        'width': 'width.raw',
        'length': 'length.raw',
        'weight': 'weight.raw'
    }

    filter_fields = {
        'date_reg': 'date_reg.raw',
        'reg_number': 'reg_number.raw',
        'name': 'name.raw',
        'classification': 'classification.raw',
        'category': 'category.raw',
        'state': 'state.raw',
        'height': 'height.raw',
        'width': 'width.raw',
        'length': 'length.raw',
        'weight': 'weight.raw'
    }
