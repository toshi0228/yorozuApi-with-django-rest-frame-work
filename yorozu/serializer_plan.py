from rest_framework import serializers
from .models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('title', 'description', 'image', 'price', 'tags')

    def create(self, validated_data):
        print(validated_data)
        tag = Plan.objects.get_or_create(**validated_data)
        # if not created:
        #     raise exceptions.ValidationError(
        #         validated_data['name']+" already exists.")
        # return tag
