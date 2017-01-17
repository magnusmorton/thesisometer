from django.contrib.auth.models import User
from .models import WordCount
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    counts = serializers.PrimaryKeyRelatedField(many=True, queryset=WordCount.objects.all())


    class Meta:
        model = User
        fields = ('username', 'counts')


class WordCountSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = WordCount
        fields = ('count', 'date',)# 'user')
