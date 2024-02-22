from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
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
def Traineeaddusingform(request):
    form=TraineeAddForm()
    context={'form':form}
    if(request.method=='POST'):
        form=TraineeAddForm(request.POST)
        if(form.is_valid()):
            # form.save()
            Trainee.creat(request.POST['name'],email=request.POST['email'],image=None,trackid=request.POST['track'])
            return HttpResponseRedirect(reverse('Trainees'))
    return render(request, 'trainee/insertform.html',context)
def Traineeadd(request):
    # print(request.method)
    # print(request.POST)#POST
    # print(request.GET)#GET
    print(request.POST)
    print(request.FILES)
    if(request.method=='POST'):
        if(request.POST['tname']!=''):

            tname=request.POST['tname']
            temail=request.POST['temail']
            #timg=request.POST['timg']
            timg=request.FILES['timg']
            Trainee.creat(tname,temail,timg)

            return HttpResponseRedirect(reverse('Trainees'))
        else:
            context={'msg':'name must be enter'}
            return render(request, 'trainee/insert.html',context)
    return render(request,'trainee/insert.html')
def Traineegetall(request):
    # print(Trainee.objects.all())
    # context={'data':Trainee.objects.all()}
    context={'data':Trainee.GetAllTrainee()}
    return render(request,'trainee/list.html',context)
def Traineeshow(request,id):
    # trainee=Trainee.objects.get(id=id)
    context={'trainee':Trainee.GetByID(id)}
    print(Trainee.GetByID(id).track)
    return render(request,'trainee/show.html',context)