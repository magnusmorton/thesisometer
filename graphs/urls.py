from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'wordcount', views.WordCountViewSet)


urlpatterns = [
    url(r'api/', include(router.urls, namespace="api")),
    url(r'^$', views.index, name="index"),
    url(r'token/', views.token, name="token"),
    url(r'clientscript\.sh$', views.client_script, name="client_script"),
    url(r'count', views.count, name="count")
]
