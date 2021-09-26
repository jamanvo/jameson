from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from movies.models import Movie, Review
from movies.serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer


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

    @action(methods=['POST'], detail=True)
    def reviews(self, request, pk=None):
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid():
            movie = self.get_object()
            queryset = movie.get_reviews(serializer.validated_data)
            return Response(ReviewSerializer(queryset, many=True).data)
        return Response(serializer.errors, status=400)

    def get_serializer_class(self):
        return ReviewListSerializer


class ReviewCreateViewSet(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['POST'], detail=True)
    def new(self, request, pk=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.movie = self.get_object()
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_serializer_class(self):
        return ReviewSerializer
