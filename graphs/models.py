import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WordCount(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counts")
