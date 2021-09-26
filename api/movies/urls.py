from django.conf.urls import url, include
from rest_framework import routers

from api.movies.views import MovieViewSet, MovieSaveViewSet, ReviewViewSet, ReviewCreateViewSet

router = routers.DefaultRouter()
router.register('view', MovieViewSet)
router.register('save', MovieSaveViewSet)
router.register('reviews', ReviewViewSet)
router.register('reviews', ReviewCreateViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
