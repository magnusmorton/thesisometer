from django.contrib.auth.models import User
from .models import WordCount
from rest_framework import serializers


class WordCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordCount
        fields = ('count', 'date')


class UserSerializer(serializers.ModelSerializer):
    #counts = serializers.HyperlinkedRelatedField(many=True, view_name="graphs:wordcount-detail", queryset=WordCount.objects.all())
    counts = WordCountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'counts')
