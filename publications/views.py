from django.shortcuts import render

from .models import Author, Publication


def index(request):
    context = {
        'authors': Author.objects.all(),
        'publications': Publication.objects.all()
    }
    return render(request, 'publications/index.html', context)
