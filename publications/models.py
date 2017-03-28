# -*- coding:utf-8 -*-
# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.db import models


class Author(models.Model):
    """ EPFL author? Cluster result ?
        This class represents an author in the institutional archive.
    """
    # XXX: names length might be too small. Confirm from query on Infoscience DB (ask mysql dump to CFR or JD)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        """ Standard function used to compute the “informal” string representation of an object.
        """
        return "%s %s (%s)" % (self.first_name, self.last_name, self.email)


class Publication(models.Model):
    """ Record from Infoscience: set of metadata
        TODO: add signatures and explain briefly difference between signatures and authors
        TODO: add DOI to be able to identify a publication
    """
    # XXX: title length might be too small.
    title = models.CharField(max_length=200)
    pub_date = models.DateField(null=True, blank=True)
    # XXX: add quotes to avoid error: ManyToManyField("Author")
    author = models.ManyToManyField(Author)

    def __str__(self):
        """ Standard function used to compute the “informal” string representation of an object.
        TODO: add DOI, (pub_date ?)"""
        return "%s, %s" % (self.title, self.pub_date)
