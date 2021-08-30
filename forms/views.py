from django.shortcuts import render,HttpResponse

# Create your views here.
def HomeForm(request):
    return render(request,'forms/FormLink.html')