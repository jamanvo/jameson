from rest_framework import serializers

from movies.models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.Serializer):
    score_min = serializers.FloatField(default=0.0, min_value=0.0, max_value=5.0)
    score_max = serializers.FloatField(default=5.0, min_value=0.0, max_value=5.0)
    order = serializers.ChoiceField(choices=[f.name for f in Review._meta.get_fields()])
    direction = serializers.ChoiceField(choices=['asc', 'desc'])
