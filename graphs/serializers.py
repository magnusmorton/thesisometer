from django.contrib.auth.models import User
from .models import WordCount
from rest_framework import serializers


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        date_req = self.context['request'].GET.get('counts__date__gt', None)
        if date_req:
            print(date_req)
            data = data.filter(date__gt=date_req)
        return super(FilteredListSerializer, self).to_representation(data)


class WordCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordCount
        list_serializer_class = FilteredListSerializer
        fields = ('count', 'date')


class UserSerializer(serializers.ModelSerializer):
    counts = WordCountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'counts')
