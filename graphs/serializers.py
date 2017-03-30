from datetime import date, timedelta
from django.contrib.auth.models import User
from .models import WordCount
from rest_framework import serializers


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        date_req = self.context['request'].GET.get('date_range', None)
        if date_req:
            if date_req == "all":
                delta = None
            elif date_req == "year":
                delta = timedelta(days=365)
            elif date_req == "month":
                delta = timedelta(days=30)
            elif date_req == "quarter":
                delta = timedelta(days=90)

            if delta:
                data = data.filter(date__gt=date.today() - delta)

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
