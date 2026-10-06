from django.shortcuts import render

# Create your views here.




from django.http import HttpResponse
def Home(request):
    if(request.method=="GET"):
        return HttpResponse('welcome to django')
def Index(request):
    if(request.method=="GET"):
        return HttpResponse('Index')


