from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.compat import StringField
from elasticsearch_dsl import MetaField, analyzer

from lost_objects.models import HeritageLostObject

keyword_lowercase = analyzer(
    'keyword_lowercase',
    tokenizer="keyword",
    filter='lowercase'
)


@registry.register_document
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

    class Index:
        name = 'heritage_lost_objects'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            "max_result_window": 20000
        }

    class Django:
        model = HeritageLostObject

    class Meta:
        dynamic = MetaField('true')
        numeric_detection = MetaField('true')
