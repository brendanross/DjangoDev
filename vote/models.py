from django.db import models
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish():
      self.save()
    
    def __str__(self):
        return self.title
    