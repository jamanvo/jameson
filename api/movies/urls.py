from django.conf.urls import url, include
from rest_framework import routers

from api.movies.views import MovieViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
