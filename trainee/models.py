from django.db import models
from track.models import *
# Create your models here.
class Trainee(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    age=models.IntegerField(default=22)
    # image=models.CharField(max_length=100)
    image=models.ImageField(upload_to='trainee/images',blank=True,null=True)
    createdate=models.DateTimeField(auto_now_add=True)#
    updatedate=models.DateTimeField(auto_now=True)
    # track=models.ForeignKey(Track1,on_delete=models.CASCADE)
    track2=models.ForeignKey(Track1,on_delete=models.CASCADE)#object model track
    # track=Track1()

    @classmethod
    def GetAllTrainee(cls):
        return cls.objects.all()
    @classmethod
    def GetByID(cls,id):
        return cls.objects.get(id=id)

    @classmethod
    def creat(self,name,email,image,trackid,age=22):

        trackobj=Track1.objects.get(id=trackid)
        Trainee.objects.create(name=name, email=email, image=image,age=age,track=trackobj)
        return 'added'

    def GetImageURl(self):
        print(f'/media/{self.image}')
        return f'/media/{self.image}'

    # def __str__(self):
    #     return self.name

