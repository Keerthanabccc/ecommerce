from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('register/',reg),
    path('login/',log),
    path('upload/',up),
    path('display/',display),
    path('updatedata/ <int:id>',update_data),
    path('card/',car)




]