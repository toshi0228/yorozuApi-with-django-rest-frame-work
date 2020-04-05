
from .serializer_account import MyUserSerializer
from .models import MyUser
from rest_framework import viewsets
from rest_framework import status, views


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
