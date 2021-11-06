from rest_framework import serializers
from .models import Movies, GENRES


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['name', 'genre', 'release_date', 'up_votes', 'down_votes', 'reviews']


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        if(validated_data.get('up_votes')):
                instance.up_votes += 1
        if(validated_data.get('down_votes')):
                instance.down_votes -= 1
        instance.reviews = validated_data.get('reviews', instance.reviews)
        instance.save()
        return instance



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['name']

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)
