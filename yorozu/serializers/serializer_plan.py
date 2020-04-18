from rest_framework import serializers
from .serializer_tag import TagSerializer
from ..models import Plan, Tag


class PlanSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        # fields = ('title', 'description', 'image', 'price',)
        fields = ('title', 'tags',)

        # "{"title":"ファ","description":"ファ","image":"電話.jpg","price":"12","tags":["インスターグラマー","aaaa"]}"

    # {'title': '試し1', 'tags': [OrderedDict([('name', 'try1')])]}
    # {'title': '試し2', 'tags': [OrderedDict([('name', 'try2')]), OrderedDict([('name', 'try3')])]}
    def create(self, validated_data):
        print(f'{"="*125}')
        print("PlanSerializer(serializers.ModelSerializer")
        print(validated_data)

        # タグの保存のクラスメソッド
        # ex)tags:[<Tag: 試し1>,<Tag: 試し2>]
        tags = Tag.multi_get_or_create(validated_data)

        # タグを削除して新たなオブジェクトを作成する
        # {'title': '試し67', 'tags': [OrderedDict([('name', 'try67')])]}
        validated_data.pop('tags')

        # **validated_data {'title': '試し67'} => 'titile'='試し67'
        plan = Plan.objects.create(**validated_data)

        # セットの場合は配列にしないといけない
        plan.tags.set(tags)

        return plan
