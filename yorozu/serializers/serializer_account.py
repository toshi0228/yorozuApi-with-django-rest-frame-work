from rest_framework import serializers
from ..models import Plan
from ..models import Account
from .serializer_profile import ProfileSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        # fields = "__all__"
        fielfs = ('email', 'password')
        exclude = ('first_name', 'last_name', "username",
                   "is_active", "is_staff", "last_login")

    # 上書きでユーザーを作成する
    # シリアライザーでcreateを使うことでオーバーライドできる
    # 引数には、入力項目が入ってくる
    def create(self, validated_data):
        user = Account.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
