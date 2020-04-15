from rest_framework import serializers
from ..models import Plan, Tag


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        fields = ('title', 'description', 'image', 'price',)

        # "{"title":"ファ","description":"ファ","image":"電話.jpg","price":"12","tags":["インスターグラマー","aaaa"]}"

    # def create(self, validated_data):
    #     print(validated_data)
        #     print(f'{"="*125}')
        #     print("やるぞPlanSerializer(serializers.ModelSerializer")
        #     print(validated_data)

        #     # tag = Plan.objects.get_or_create(**validated_data)
        #     print(f'{"="*25}')
        #     tags = Tag.multi_get_or_create(validated_data)
        #     print(tags)
        #     return tags

        # print(f'{"="*125}')
        # print("やるぞPlanViewSet(viewsets.ModelViewSet")
        # print(request.data)
        # print(request.POST)

        # if not created:
        #     raise exceptions.ValidationError(
        #         validated_data['name']+" already exists.")
        # return tag
