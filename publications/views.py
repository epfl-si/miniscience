from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['GET'])
def author_publications(request, pk):
    queryset = Publication.objects.filter(author__id=pk)
    serializer = PublicationSerializer(queryset, many=True, context={'request':request})
    return Response(serializer.data)


def index(request):
    context = {
        'authors': Author.objects.all(),
        'publications': Publication.objects.all()
    }
    return render(request, 'publications/index.html', context)
