from rest_framework import serializers
from .serializer_tag import TagSerializer
from ..models import Plan, Tag


class PlanSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        fields = ('title', 'tags',)

        # "{"title":"ファ","description":"ファ","image":"電話.jpg","price":"12","tags":["インスターグラマー","aaaa"]}"

    def create(self, validated_data):
        print(f'{"="*125}')
        print("PlanSerializer(serializers.ModelSerializer")
        print(validated_data)

        res_dict = {}
        # タグの保存のクラスメソッド
        tags = Tag.multi_get_or_create(validated_data)
        print(tags)

        tags = validated_data.pop('tags')
        print(validated_data)

        plan = Plan.objects.create(**validated_data)
        print("作成されたもの")
        print(plan)
        res_dict['title'] = plan.title
        res_dict['tags'] = tags
        print(res_dict)
        return res_dict

        # tag = Tag.objects.all()
        # ko = Plan.objects.get(**validated_data)

        # plan = Plan.objects.get_or_create(**validated_data)
        # # plan = Plan.objects.all()
        # print(plan)
        # plan, created = Plan.objects.get_or_create(**validated_data)
        # print(plan)
        # print(created)

    # def create(self, validated_data):
    #     print(validated_data)
    #     res_dict = {}
    #     tags = validated_data.pop('tags')
    #     plan = Plan.objects.get_or_create(**validated_data)
    #     res_dict['plan'] = plan
    #     res_dict['plan']['tags'] = []
    #     for tag_data in tags:
    #         tag = Tag.objects.create(plan=plan, **tag_data)
    #         res_dict['plan']['tags'].append(tag)
    #     return res_dict
