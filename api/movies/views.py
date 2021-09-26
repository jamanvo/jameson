from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from movies.models import Movie, Review
from movies.serializers import MovieSerializer, ReviewSerializer


class MovieViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSaveViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class ReviewViewSet(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['GET', 'POST'], detail=True)
    def review(self, request, pk=None):
        if request.method == 'GET':
            movie = self.get_object()
            serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.movie = self.get_object()
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    def get_serializer_class(self):
        return ReviewSerializer
