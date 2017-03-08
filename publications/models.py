# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Publication(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(null=True, blank=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
