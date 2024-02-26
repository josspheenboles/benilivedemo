from django.urls import path
from django.contrib.auth.decorators import login_required
from trainee.views import *

urlpatterns = [
   path('List/',login_required(TraineeList.as_view()),name='Trainees'),
   path('<int:pk>/',TraineeDetails.as_view(),name='traineeshow'),
   path('Delete/<int:pk>/',TraineeDelet.as_view(),name='Traineedelete'),
   # path('Update/<int:id>/',Traineeupdate,name='Traineeupdate'),
   path('Update/<int:pk>/',TraineeUpdate.as_view(),name='Traineeupdate'),
   path('Add/',TraineeList.as_view(),name='Traineeadd'),
   path('Addform/',Traineeadd.as_view(),name='Traineeaddusingform'),
   # path('AddformModel/',Traineeaddusingformmodel,name='Traineeaddusingformmodel'),
   path('AddformModel/',TraineeList.as_view(),name='Traineeaddusingformmodel'),
]
