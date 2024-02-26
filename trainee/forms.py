from django import forms
from track.models import *
from .models import Trainee
class TraineeAddForm(forms.Form):
    name=forms.CharField(label='Full Name',max_length=50)
    email=forms.EmailField(label='acadmic Email')
    Profilepic=forms.ImageField()
    # track=forms.ChoiceField(choices=[(1,'os'),(2,'iot')])
    # track=forms.ChoiceField(choices=[(track.id,track.name) for track in Track1.objects.all()])
    track=forms.ChoiceField(choices=Track1.GetChoces())
    # def clean(self):
    #     if(self.name=='ali'):
    #         return  False
class TraineeAddFormModel(forms.ModelForm):
    # xx=forms.CharField()
    class Meta:
        model=Trainee
        fields  =['name','email','track2']
        # fields='__all__'
        # exclude=['age']
