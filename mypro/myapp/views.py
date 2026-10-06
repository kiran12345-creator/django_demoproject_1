from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     if(request.method=='GET'):
#         return HttpResponse('home page')
# def first(request):
#     if(request.method=='GET'):
#         return HttpResponse('first page')
# def second(request):
#     if(request.method=='GET'):
#         return HttpResponse('second page')
from django.views import View
class Home(View):
    def get(self,request):
        return HttpResponse('home')
class First(View):
    def get(self,request):
        return HttpResponse('first page')
class Second(View):
    def get(self,request):
       return HttpResponse('second page')