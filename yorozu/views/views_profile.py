from rest_framework import viewsets
# from rest_framework import status, views
from ..serializers.serializer_profile import ProfileSerializer
from ..models import Profile


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


# veiesのフォルダーを分けた方が良い
# modelsフォルダーの中に入れる
# pip freeze te
