"""
URL configuration for examinationsystems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from track.views import  *
from track.views import *
from trainee.views import *
urlpatterns = [
    #view--->route
    path('admin/', admin.site.urls),
    # path('urlstatickeyword',views,name='d')
    path('',hello),
    path('Tracks/',include('track.urls')),
    path('Trainees/',include('trainee.urls')),
    # path('Trainee/',include('trainee.urls')),
    # path('Tracks/',tracks),
    # path('Tracks/<int:id>/',gettrackbyid),#wait data
    # path('Tracks/<str:name>/',gettrackbyname),#wait data

]
#slud-->ascii,letter,_,number
#uuid---->uuid
#r-path()--->12.3