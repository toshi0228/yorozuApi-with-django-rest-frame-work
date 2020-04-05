from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        # fields = ('name')

    # def create(self, validated_data):
    #     print(validated_data)
    #     tag = .objects.get_or_create(**validated_data)
        # if not created:
        #     raise exceptions.ValidationError(
        #         validated_data['name']+" already exists.")
        # return tag
