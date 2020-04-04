from django.urls import path, include
from yorozu import views
from rest_framework import routers

# ======================================================================

# うまくできたもの
router = routers.DefaultRouter()
router.register('register', views.AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# ======================================================================
