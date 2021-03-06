from django.conf.urls import url, include
from rest_framework import routers

from api.users.views import UserCreateViewSet

router = routers.DefaultRouter()
router.register('create', UserCreateViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
