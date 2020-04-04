from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fielfs = ('email', 'password', )
        exclude = ('first_name', 'last_name', "username",
                   'profile', "is_active", "is_staff", "last_login")

    # 上書きでユーザーを作成する
    # シリアライザーでcreateを使うことでオーバーライドできる
    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
