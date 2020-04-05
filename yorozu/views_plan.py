from rest_framework import viewsets
from .models import Plan
from .serializer_plan import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
