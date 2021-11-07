from rest_framework import serializers
from .models import MovieReview, Movies, GENRES

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movies
        fields = '__all__'


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        if(validated_data.get('up_votes')):
                instance.up_votes += 1
        if(validated_data.get('down_votes')):
                instance.down_votes -= 1
        if(validated_data.get('reviews')):
                instance.reviews.add(MovieReview.objects.create(review=validated_data.get('reviews')[0]['review']))
        instance.save()
        return instance



class MovieListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def create(self, validated_data):
        reviews = validated_data.pop('reviews')
        movie = Movies.objects.create(**validated_data)
        moviereview = MovieReview.objects.create(review=reviews[0]['review'])
        movie.reviews.add(moviereview)  
        return movie

    def list(self):
        return Movies.objects.values_list('name')
