from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import UserSerializer

# Create your views here.

def index(request):
    return  render(request, 'graphs/index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-username")
    serializer_class = UserSerializer
