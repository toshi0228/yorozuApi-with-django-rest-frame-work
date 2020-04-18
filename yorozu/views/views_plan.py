from rest_framework import viewsets
from ..models import Plan
from ..serializers.serializer_plan import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# def create(self, validated_data):
#     print(f'{"="*125}')
#     print("PlanViewSet")
#     print(validated_data)
