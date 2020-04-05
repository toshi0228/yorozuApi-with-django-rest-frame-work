from rest_framework import serializers
from .models import Plan, Tag


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('title', 'description', 'image', 'price', 'tags')

    def create(self, validated_data):
        print(validated_data)
        # tag = Plan.objects.get_or_create(**validated_data)
        print(f'{"="*25}')
        tags = Tag.multi_get_or_create(validated_data)
        print(tags)
        return tags

        # if not created:
        #     raise exceptions.ValidationError(
        #         validated_data['name']+" already exists.")
        # return tag
