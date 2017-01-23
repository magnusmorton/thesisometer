"""thesisometer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import GraphsRedirectView

urlpatterns = [
    url(r"^graphs/", include('graphs.urls', namespace='graphs')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', GraphsRedirectView.as_view(), name='registration_register'),
    url(r'^accounts/register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'),
                          name='registration_disallowed'),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
