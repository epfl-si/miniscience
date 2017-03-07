from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
