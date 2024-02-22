from django import forms
from track.models import *
class TraineeAddForm(forms.Form):
    name=forms.CharField(label='Full Name',max_length=50)
    email=forms.EmailField(label='acadmic Email')
    # track=forms.ChoiceField(choices=[(1,'os'),(2,'iot')])
    # track=forms.ChoiceField(choices=[(track.id,track.name) for track in Track1.objects.all()])
    track=forms.ChoiceField(choices=Track1.GetChoces())
    # def clean(self):
    #     if(self.name=='ali'):
    #         return  False
