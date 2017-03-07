from rest_framework import serializers

from .models import Author, Publication


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ('title', 'pub_date', 'author')
