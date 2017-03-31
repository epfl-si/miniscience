# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api/authors/$', views.AuthorList.as_view(), name='author-list'),
    url(r'^api/authors/(?P<pk>[0-9]+)/publications/$', views.author_publications),
    url(r'^api/authors/(?P<pk_author>[0-9]+)/publications/(?P<pk_publication>[0-9]+)/$', views.delete_link),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
