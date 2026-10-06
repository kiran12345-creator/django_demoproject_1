from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from django.views import View
class Home(View):
    def get(self,request):
      return  HttpResponse('welcome to portfolio home page')
class About(View):
    def get(self,request):
        data={'id':31,'name':'lalu','title':'tester','DOB':'feb-08',
              'Email':'lalu@gmail.com','phn':1234567890,
              'git':'lalu@git','linkdin':'lalu@linkdin'}
        return JsonResponse(data)
class    Education(View) :
    def get(self,request):
        data={'id':31,'institution':'luminar','course':'tester',
              'university':'ktu','location':'kochi',
              'startyear':2026,'endyear':2027,
              'grade':'A+','description':'passonate software tester'}
        return JsonResponse(data)
class Project(View):
    def get(self,request):
        data=[{
            'id':31,'project_name':'selenium','description':'advanced technology for testing and finding bugs',
            'technologies':'java,sql','duration':'5 months','live_url':'lalu_the_tester'}
]
        return JsonResponse(data,safe=False)