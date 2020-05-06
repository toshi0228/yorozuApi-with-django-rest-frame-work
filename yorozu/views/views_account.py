from rest_framework import viewsets
from rest_framework import status, views
from ..serializers.serializer_account import AccountSerializer
from ..models import Account


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()


# veiesのフォルダーを分けた方が良い
# modelsフォルダーの中に入れる
# pip freeze te
