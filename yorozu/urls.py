from django.urls import path, include
from yorozu import views_account, views_plan
from rest_framework import routers


# ======================================================================
# router
# router.register('register', views.AccountViewSet)
# router.register()の引数がurlになる エンドポイントになる
# ex)
# http://127.0.0.1:8081/account/register/
# ======================================================================

router = routers.DefaultRouter()
router.register('plan', views_plan.PlanViewSet)
router.register('account/register', views_account.AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
