from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSaveViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class ReviewViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['GET', 'POST'], detail=True)
    def review(self, request):
        pass


