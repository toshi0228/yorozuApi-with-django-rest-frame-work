from rest_framework import viewsets
from ..models import Message
from ..serializers.serializer_message import MessageSerializer

# from ..serializers.serializer_plan import PlanSerializer


# !!ModelViewSetのviwsのVは大文字
class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
