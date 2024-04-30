from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search.documents.heritage_lost_objects import HeritageLostObjectDocument


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
