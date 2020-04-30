from rest_framework import serializers
from ..models import Profile
from .serializer_plan import PlanSerializer
# from .serializer_tag import TagSerializer


class ProfileSerializer(serializers.ModelSerializer):
    plan_list = PlanSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "nickname",
            "profile_image",
            "profile_description",
            "yorozuya_name",
            "profile_image",
            "profile_description",
            "yorozu_main_image",
            "review_score",
            "twitter_account",
            "instagram_account",
            "facebook_account",
            "plan_list"
        )
        # fields = "__all__"
