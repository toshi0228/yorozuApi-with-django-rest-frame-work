from rest_framework import viewsets, authentication
# from rest_framework import status, views
from ..serializers.serializer_profile import ProfileSerializer
from ..models import Profile
# from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = ()

    def get(self, request):
        print(f'{"="*25}')
        print(request)


# veiesのフォルダーを分けた方が良い
# modelsフォルダーの中に入れる
# pip freeze te
