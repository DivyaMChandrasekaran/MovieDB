from rest_framework import serializers
from movies.models import GENRES
from .models import MovieUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieUser
        fields = ['username', 'password', 'fav_genre']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MovieUser.objects.create_user(validated_data['username'], validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.fav_genre = validated_data.get('fav_genre', instance.fav_genre)
        instance.save()
        return instance