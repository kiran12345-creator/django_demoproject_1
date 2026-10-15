from django.shortcuts import render

# Create your views here
from django.http import JsonResponse,HttpResponse
from django.views import View
from app.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
class Home(View):
    def get(self,request):
        data=['kiran ','eldho ','akshay ']
        return  HttpResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class Studentdetails(View):

    def get(self,request):
        data = {'name': 'kiran', 'age': 23, 'mark': 78, 'course': 'python'}
        return JsonResponse(data)
class  StudentList(View):
    def get(self,request):
        l=list(Student.objects.all().values()) #query set to python native type

        return JsonResponse(l,safe=False)  #convert python native to json response


@method_decorator(csrf_exempt,name='dispatch')
class Studentcreate(View):

    def post(self,request):
        form_data=request.body
        data=loads(form_data)
        print(data)
        n=data['name']
        a=data['age']
        c=data['course']
        m=data['marks']


        #storesthe data into table using orm query
        s=Student.objects.create(name=n,age=a,course=c,marks=m)
        s.save()

        return JsonResponse({'Message':'Created'})
    #api view for reading  a specific record
class StudentDetail(View):
    def get(self,request,i):          #request cheyyunna id aan i

        #reads the record matching the id from db table
        qs=Student.objects.filter(id=i)
        #convert the data(model object) into python native
        data=list(qs.values())

        #sends respopnse
        return JsonResponse(data,safe=False)
#api view for deleting  a specific record
@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
    def delete(self,reqest,i):
        #reads corresponding data
          s=Student.objects.get(id=i)
        #deleting data
          s.delete()
        #message
          return JsonResponse({'deleted':'successfully'})
class StudentUpdate(View) :
    def put(self,request,i):


