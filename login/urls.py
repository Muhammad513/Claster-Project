from django.urls import path
from .views import*

urlpatterns=[
    path('',log,name='login'),
    
]