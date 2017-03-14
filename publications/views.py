# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.shortcuts import render
from rest_framework import status

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

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


@api_view(['GET', 'POST'])
def author_publications(request, pk):
    if request.method == 'GET':
        queryset = Publication.objects.filter(author__id=pk)
        serializer = PublicationSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_link(request, pk_author, pk_publication):
    try:
        author = Author.objects.get(pk=pk_author)
        publication = Publication.objects.get(pk=pk_publication)
    except (Author.DoesNotExist, Publication.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    publication.author.remove(author)
    return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    context = {
        'authors': Author.objects.all(),
        'publications': Publication.objects.all()
    }
    return render(request, 'publications/index.html', context)
