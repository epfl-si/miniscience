"""miniscience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from publications import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authors/(?P<author_id>[0-9]+)/publications/$', views.author_publications),
    url(r'^authors/(?P<author_id>[0-9]+)/publications/(?P<publication_id>[0-9]+)/$', views.author_publication),
    url(r'^importer_infoscience/$', views.importer_infoscience),
    url(r'^importer_wos/$', views.importer_wos),
    url(r'^importer_infoscience/(?P<timestamp>[0-9]+)/$', views.importer_infoscience),
    url(r'^importer_wos/(?P<timestamp>[0-9]+)/$', views.importer_wos),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
