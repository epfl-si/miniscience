from django.contrib import admin

from .models import Author, Publication

admin.site.register(Author)
admin.site.register(Publication)
