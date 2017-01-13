from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from .forms import WordCountForm

# Create your views here.


def index(request):
    form = WordCountForm()
    return render(request, 'graphs/index.html', {"form": form})


@login_required
def count(request):
    if request.method == "POST":
        form = WordCountForm(request.POST)
    else:
        redirect('index')

@login_required
def token(request):
    uToken = Token.objects.get_or_create(user=request.user)
    return render(request, 'graphs/token.html', {'token': uToken[0].key})

@login_required
def client_script(request):
    uToken = Token.objects.get_or_create(user=request.user)
    return render(request, 'graphs/thesis_graph.sh', {'token': uToken[0].key}, content_type="text/x-shellscript")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-username")
    serializer_class = UserSerializer
