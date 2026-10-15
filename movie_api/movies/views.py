from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
class  Movielist(View):
    def get(self,request):

# Create your views here.
