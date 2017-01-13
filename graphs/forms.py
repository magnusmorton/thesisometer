from django import forms

from .models import WordCount


class WordCountForm(forms.ModelForm):

    class Meta:
        model = WordCount
        fields = "count",

