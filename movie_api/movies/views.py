from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
from movies.models import Movie
class  MovieList(View):
    def get(self,request):
        data=Movie.objects.all().values()
        form_data=list(data)
        return JsonResponse(form_data,safe=False)
# Create your views here.
    def get(self,request,i):
        data=Movie.objects.filter(id=i).values()
        form_data=list(data)
        return JsonResponse(form_data,safe=False)
    def post(self,request):

