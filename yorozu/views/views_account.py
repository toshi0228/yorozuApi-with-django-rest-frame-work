from rest_framework import viewsets
from rest_framework import status, views
from ..serializers.serializer_account import MyUserSerializer
from ..models import MyUser


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()


# veiesのフォルダーを分けた方が良い
# modelsフォルダーの中に入れる
# pip freeze te
