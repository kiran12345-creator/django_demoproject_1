from django.shortcuts import render

# Create your views here
from django.http import JsonResponse,HttpResponse
from django.views import View
class Home(View):
    def get(self,request):
        data=['kiran ','eldho ','akshay ']
        return  HttpResponse(data)
class Studentdetails(View):

    def get(self,request):
        data = {'name': 'kiran', 'age': 23, 'mark': 78, 'course': 'python'}
        return JsonResponse(data)
class  StudentList(View):
    def get(self,request):
        l=[
            {'name': 'kiran', 'age': 23, 'mark': 78, 'course': 'python'},
            {'name': 'eldho', 'age': 22, 'mark': 88, 'course': 'python-django'},
            {'name': 'akshay', 'age': 21, 'mark': 98, 'course': 'python-react'}

        ]
        return JsonResponse(l,safe=False)