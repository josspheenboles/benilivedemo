from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
data=[
        {'id': 1, 'name': 'os'},
        {'id': 2, 'name': 'IOT'}
    ]

@login_required()
def gettrackbyname(request,name):
    return HttpResponse(f'<h1> gettrackbyname track with name {name}</h1>')

def gettrackbyid(request,id):
    print('okok')
    trackinfo=list(filter(lambda t:t['id']==id,data))
    if(trackinfo):
        context={'track':trackinfo[0]}
        return render(request,'track/Track.html',context)
        # return HttpResponse(f'<h1> gettrackbyid track with id {trackinfo[0]}</h1>')
    else:
        return HttpResponse('track not found')
    # return HttpResponse('spsls')
# Create your views here.
#function view --->param httprequest  ==>return httrepsonse
# @login_required()
from django.views.decorators.http import require_http_methods
# from django.contrlib.auth.models import *

@require_http_methods(['GET','POST'])
def hello(request):
    request.SESSION['ben']='24-2'
    
    return HttpResponse('hello')
def tracks(req):
    context={'data':data}
    return render(req,'track/list.html',context)
    # str1='<table border=1 width=100%><tr><td>ID</td><td>Name</td></tr>'
    # for track in data:
    #     str1+=f"<tr><td>{track['id']}</td><td>{track['name']}</td></tr>"
    # str1+"</table>"
    # return HttpResponse(str1);
    # return HttpResponse('<h1>Track List</h1>')
    # return HttpResponse('{"msg":"track List"}')