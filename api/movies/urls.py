from django.conf.urls import url, include
from rest_framework import routers

from api.movies.views import MovieViewSet, MovieSaveViewSet

router = routers.DefaultRouter()
router.register('view', MovieViewSet)
router.register('save', MovieSaveViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
