from rest_framework import viewsets
from ..models import Message
from ..serializers.serializer_message import MessageSerializer


# !!ModelViewSetのviwsのVは大文字
class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# ====================================
    # request.dataで中身を見れる
    # def create(self, request):
    #     print(request.data)
    #     return "aaa"
# ====================================
