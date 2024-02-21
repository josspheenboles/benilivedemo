from django.db import models

# Create your models here.
class Trainee(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    age=models.IntegerField(default=22)
    image=models.CharField(max_length=100)
    createdate=models.DateTimeField(auto_now_add=True)#
    updatedate=models.DateTimeField(auto_now=True)
