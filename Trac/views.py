from django.shortcuts import render
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def TracHome(request):
    return render(request,'Trac/TracHome.html')



