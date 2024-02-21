from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
def Traineeupdate(request,id):
    context={}
    #post===>update save
    if(request.method=='POST'):
        Trainee.objects.filter(id=id).update(
            name=request.POST['tname'],
            email=request.POST['temail'],
            image=request.POST['timg'],
        )
        return HttpResponseRedirect(reverse('Trainees'))
    #get--->update.html
    trainee=Trainee.objects.get(id=id)
    context['trainee']=trainee
    return render(request,'trainee/update.html',context)
def Traineedelete(request,id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('Trainees'))
def Traineeadd(request):
    # print(request.method)
    # print(request.POST)#POST
    # print(request.GET)#GET
    if(request.method=='POST'):
        tname=request.POST['tname']
        temail=request.POST['temail']
        timg=request.POST['timg']
        Trainee.objects.create(name=tname,email=temail,image=timg)
        return HttpResponseRedirect(reverse('Trainees'))
    return render(request,'trainee/insert.html')
def Traineegetall(request):
    print(Trainee.objects.all())
    context={'data':Trainee.objects.all()}
    return render(request,'trainee/list.html',context)
def Traineeshow(request,id):
    trainee=Trainee.objects.get(id=id)
    context={'trainee':trainee}
    return render(request,'trainee/show.html',context)