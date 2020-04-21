from django.urls import path, include
from yorozu.views import views_account, views_plan, views_tag, views_plan_entry, api_view_plan
from rest_framework import routers


# ======================================================================
# router
# router.register('register', views.AccountViewSet)
# router.register()の引数がurlになる エンドポイントになる
# ex)
# http://127.0.0.1:8081/account/register/
# ======================================================================

router = routers.DefaultRouter()
router.register('account/register', views_account.AccountViewSet)
router.register('plan', views_plan.PlanViewSet)
router.register('tag', views_tag.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('entry', api_view_plan.PlanView.as_view())
]

# path('entry', views_plan_entry.api_entry),
