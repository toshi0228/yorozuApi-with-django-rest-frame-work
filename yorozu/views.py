
from .serializer import MyUserSerializer
from .models import MyUser
from rest_framework import viewsets
from rest_framework import status, views


# ======================================================================

# うまくできたもの

class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

# ======================================================================
