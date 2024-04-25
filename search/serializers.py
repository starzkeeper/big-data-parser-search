from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import HeritageLostObjectDocument


class HeritageLostObjectDocumentSerializer(DocumentSerializer):
    class Meta:
        document = HeritageLostObjectDocument

        fields = (
            'date_reg',
            'reg_number',
            'name',
            'classification',
            'category',
            'state',
            'height',
            'width',
            'length',
            'weight'
        )
