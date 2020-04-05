from django.urls import path, include
from yorozu import views_account
from rest_framework import routers


# ======================================================================
# router
# router.register('register', views.AccountViewSet)
# router.register()の引数がurlになる エンドポイントになる
# ex)
# http://127.0.0.1:8081/account/register/
# ======================================================================

router = routers.DefaultRouter()
router.register('register', views_account.AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]
