from rest_framework import serializers
from ..models import Plan
from ..models import MyUser
from .serializer_profile import ProfileSerializer


class MyUserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(default="aaa", null=True, blank=True)
    # plan_list = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        # fields = "__all__"
        fielfs = ('email', 'password')
        exclude = ('first_name', 'last_name', "username",
                   "is_active", "is_staff", "last_login")

    # 上書きでユーザーを作成する
    # シリアライザーでcreateを使うことでオーバーライドできる
    # 引数には、入力項目が入ってくる
    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    # def get_profile(self, instance):
    #     print("===========")
    #     print(instance)

# from .serializer_tag import TagSerializer


# class PlanSerializer(serializers.ModelSerializer):

#     # 以下のようにすることで、ネストした値を受け取ることができる
#     tags = TagSerializer(many=True, read_only=True)
