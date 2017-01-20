import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class WordCount(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counts")

    def save(self, *args, **kwargs):
        try:
            self.validate_unique()
        except ValidationError:
            wc = WordCount.objects.filter(date=self.date, user=self.user).first()
            wc.count = self.count
            wc.save()
            return
        super(WordCount, self).save(*args, **kwargs)


    class Meta:
        unique_together = ("date", "user")
