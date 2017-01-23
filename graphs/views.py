from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer, WordCountSerializer
from .forms import WordCountForm
from .models import WordCount

# Create your views here.


def index(request):
    form = WordCountForm()
    return render(request, 'graphs/index.html', {"form": form})


@login_required
def count(request):
    if request.method == "POST":
        form = WordCountForm(request.POST)
        if form.is_valid():
            wc = form.save(commit=False)
            wc.user = request.user
            wc.save()
            return redirect('graphs:index')
    else:
        return redirect('graphs:index')

@login_required
def token(request):
    uToken = Token.objects.get_or_create(user=request.user)
    return render(request, 'graphs/token.html', {'token': uToken[0].key})


@login_required
def client_script(request):
    u_token = Token.objects.get_or_create(user=request.user)
    return render(request, 'graphs/thesis_graph.sh', {'token': u_token[0].key, 'host': request.get_host()},
                  content_type="text/plain  ")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-username")
    serializer_class = UserSerializer
    http_method_names = ['get', 'head', 'options']


class WordCountViewSet(viewsets.ModelViewSet):
    queryset = WordCount.objects.all()
    serializer_class = WordCountSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,

    def create(self, request):
        serializer = WordCountSerializer(data=request.data)
        if serializer.is_valid():
            wc = serializer.save(user=request.user)
            wc.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
