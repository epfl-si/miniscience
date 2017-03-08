# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.contrib import admin

from .models import Author, Publication

admin.site.register(Author)
admin.site.register(Publication)
