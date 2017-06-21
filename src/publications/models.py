# -*- coding:utf-8 -*-
# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.db import models


class Author(models.Model):
    """This class represents an author in the institutional archive."""
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Publication(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.IntegerField(blank=True, null=True)
    doi = models.CharField(max_length=60, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    imported_datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
