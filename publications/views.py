from django.shortcuts import render

from rest_framework import viewsets

from .models import Author, Publication
from .serializers import AuthorSerializer, PublicationSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all().order_by('-first_name')
    serializer_class = AuthorSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


def index(request):
    context = {
        'authors': Author.objects.all(),
        'publications': Publication.objects.all()
    }
    return render(request, 'publications/index.html', context)
