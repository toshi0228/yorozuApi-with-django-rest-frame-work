from rest_framework import serializers
from .serializer_tag import TagSerializer
from ..models import Plan, Tag
from collections import OrderedDict


class PlanSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        fields = ('title', 'description', 'image', 'price', "tags")
        # fields = ('title', 'tags',)
        # extra_kwargs = {
        #     # モデル上は必須フィールドだけれど、シリアライザでは Not必須にしたい場合は、required を上書きする
        #     'tags': {'required': False}
        # }
