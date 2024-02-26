from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from track.models import *
from django.views import View
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
class TraineeList(ListView):
    model=Trainee
    template_name='trainee/list.html'
    context_object_name='data'
class TraineeDelet(DeleteView):
    model=Trainee
    template_name='trainee/delete.html' #msg(are you sure you want to delete)
    # context_object_name='data'
    success_url = reverse_lazy('Trainees')
class TraineeDetails(DetailView):
    model=Trainee
    template_name='trainee/show.html'
    context_object_name='trainee'
class TraineeUpdate(UpdateView):
    model=Trainee
    template_name='trainee/update.html'
    context_object_name='tracks'#tracks,trainee
    fields='__all__'
class Traineeadd(CreateView):
    model=Trainee
    template_name='trainee/insertform.html'
    Form_class='form'#tracks,trainee
    fields='__all__'
    # exclude=['age']
    success_url=reverse_lazy('Trainees')
# Create your views here.
# class Traineeupdateclass(View):
#     def get(self,request,id):
#         context={}
#         trainee = Trainee.objects.get(id=id)
#         context['trainee'] = trainee
#         context['tracks'] = Track1.objects.all()
#         return render(request, 'trainee/update.html', context)
#     def post(self,request,id):
#         Trainee.objects.filter(id=id).update(
#             name=request.POST['tname'],
#             email=request.POST['temail'],
#             image=request.POST['timg'],
#         )
#         return HttpResponseRedirect(reverse('Trainees'))
# def Traineeupdate(request,id):
#     context={}
#     #post===>update save
#     if(request.method=='POST'):
#         Trainee.objects.filter(id=id).update(
#             name=request.POST['tname'],
#             email=request.POST['temail'],
#             image=request.POST['timg'],
#         )
#         return HttpResponseRedirect(reverse('Trainees'))
#     #get--->update.html
#     trainee=Trainee.objects.get(id=id)
#     context['trainee']=trainee
#     context ['tracks']= Track1.objects.all()
#     return render(request,'trainee/update.html',context)
# def Traineedelete(request,id):
#     Trainee.objects.filter(id=id).delete()
#     return HttpResponseRedirect(reverse('Trainees'))
# def Traineeaddusingform(request):
#     form=TraineeAddForm()
#     context={'form':form}
#     if(request.method=='POST'):
#         form=TraineeAddForm(request.POST)
#         if(form.is_valid()):
#             # form.save()
#             Trainee.creat(request.POST['name'],email=request.POST['email'],image=None,trackid=request.POST['track'])
#             return HttpResponseRedirect(reverse('Trainees'))
#     return render(request, 'trainee/insertform.html',context)
# class Traineeaddclass(View):
#     def get(self,request):
#         form = TraineeAddFormModel()
#         context = {'form': form}
#         return render(request, 'trainee/insertform.html',context)
#     def post(self,request):
#         form = TraineeAddFormModel(request.POST)
#         if (form.is_valid()):
#             form.save()
#             # Trainee.creat(request.POST['name'],email=request.POST['email'],image=None,trackid=request.POST['track'])
#             return HttpResponseRedirect(reverse('Trainees'))
# def Traineeaddusingformmodel(request):
#     form=TraineeAddFormModel()
#     context={'form':form}
#     if(request.method=='POST'):
#         form=TraineeAddFormModel(request.POST)
#         if(form.is_valid()):
#             form.save()
#             # Trainee.creat(request.POST['name'],email=request.POST['email'],image=None,trackid=request.POST['track'])
#             return HttpResponseRedirect(reverse('Trainees'))
#     return render(request, 'trainee/insertform.html',context)
# def Traineeadd(request):
#     # print(request.method)
#     # print(request.POST)#POST
#     # print(request.GET)#GET
#     # print(request.POST)
#     # print(request.FILES)
#     if(request.method=='POST'):
#         if(request.POST['tname']!=''):
#
#             tname=request.POST['tname']
#             temail=request.POST['temail']
#             #timg=request.POST['timg']
#             timg=request.FILES['timg']
#             Trainee.creat(tname,temail,timg)
#
#             return HttpResponseRedirect(reverse('Trainees'))
#         else:
#             context={'msg':'name must be enter'}
#             return render(request, 'trainee/insert.html',context)
#     context={'tracks':Track1.objects.all()}
#     return render(request,'trainee/insert.html',context)
# def Traineegetall(request):
#     # print(Trainee.objects.all())
#     # context={'data':Trainee.objects.all()}
#     context={'data':Trainee.GetAllTrainee()}
#     return render(request,'trainee/list.html',context)
# def Traineeshow(request,id):
#     # trainee=Trainee.objects.get(id=id)
#     context={'trainee':Trainee.GetByID(id)}
#     print(Trainee.GetByID(id).track)
#     return render(request,'trainee/show.html',context)