from django.db import models

# Create your models here.
class Track1(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

    @classmethod
    def GetChoces(cls):
        return [(track.id,track.name) for track in cls.objects.all()]
