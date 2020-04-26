from rest_framework import serializers
from ..models import Profile

# from rest_framework import serializers
# from ..models import Tag


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


# class TagSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Tag
#         fields = "__all__"
#         # fields = ('name')
