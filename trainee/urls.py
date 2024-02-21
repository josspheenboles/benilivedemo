from django.urls import path
from trainee.views import *
urlpatterns = [
   path('List/',Traineegetall,name='Trainees'),
   path('<int:id>/',Traineeshow,name='traineeshow'),
   path('Delete/<int:id>/',Traineedelete,name='Traineedelete'),
   path('Update/<int:id>/',Traineeupdate,name='Traineeupdate'),
   path('Add/',Traineeadd,name='Traineeadd'),
]
