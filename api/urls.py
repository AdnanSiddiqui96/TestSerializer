from django.urls import path,include
from api.views import *

urlpatterns = [

#web urls  home
path('add',depart.as_view()),
path('emp',employees.as_view()),

]