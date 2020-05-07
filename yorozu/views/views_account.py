from rest_framework import viewsets
from rest_framework import status, views
from ..serializers.serializer_account import AccountSerializer
from ..models import Account


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    # jwtの場合、これは使わなくなる
    # permission_classes = (IsAuthenticated,)
