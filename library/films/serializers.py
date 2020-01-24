from django.contrib.auth.models import Group, User
from rest_framework import serializers
from films.models import Movie, Genre


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#
class GenreSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    Genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ("id", "name", "year", "created_on", "summary", "Genre")