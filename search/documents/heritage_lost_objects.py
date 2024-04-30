from django.conf import settings
from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl_drf.compat import StringField
from elasticsearch_dsl import analyzer

from lost_objects.models import HeritageLostObject

keyword_lowercase = analyzer(
    'keyword_lowercase',
    tokenizer="keyword",
    filter='lowercase'
)

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=50,
    number_of_replicas=0
)


@INDEX.doc_type
class HeritageLostObjectDocument(Document):
    date_reg = fields.DateField(
        attr='date_reg',
        fields={
            'raw': fields.KeywordField(),
            'search': fields.TextField()

        }
    )
    reg_number = fields.IntegerField(
        attr='reg_number',
        fields={
            'raw': fields.KeywordField(),
            'search': fields.TextField()
        }
    )
    name = fields.TextField(
        attr='name',
        fields={
            'raw': StringField(analyzer=keyword_lowercase)
        }
    )
    classification = fields.TextField(
        attr='classification',
        fields={
            'raw': fields.KeywordField()
        }
    )
    category = fields.TextField(
        attr='category',
        fields={
            'raw': fields.KeywordField()
        }
    )
    state = fields.TextField(
        attr='state',
        fields={
            'raw': fields.KeywordField()
        }
    )

    height = fields.TextField(
        attr='height',
        fields={
            'raw': fields.KeywordField()
        }
    )
    width = fields.TextField(
        attr='width',
        fields={
            'raw': fields.KeywordField()
        }
    )
    length = fields.TextField(
        attr='length',
        fields={
            'raw': fields.KeywordField()
        }
    )
    weight = fields.TextField(
        attr='weight',
        fields={
            'raw': fields.KeywordField()
        }
    )

    class Django:
        model = HeritageLostObject

