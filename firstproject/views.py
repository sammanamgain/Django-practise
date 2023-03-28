from django.http import HttpResponse;
from django.shortcuts import render;
def home(request):
    return HttpResponse("Hello, World!");

def dynamic(request):
    return HttpResponse("dynamic route");

def dynamicdetails(request,name):
    return HttpResponse(name);
def homepage(request):
    data = {
        'title': 'dynamic',
        'my_list': ['javascript', 'flutter', 'django']
                }
    return render(request,"index.html",data);