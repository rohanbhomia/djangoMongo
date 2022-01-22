from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import Todo
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def index(request):
    if request.method == 'GET':
        obj = Todo.objects.get(id=9)
        print(obj.title)
        print(obj.description)
        print(obj.demo)
        return HttpResponse("1")
    if request.methd == 'POST':
        obj = Todo(title="rohan",description="demo descriptionsaddddddddddddddddddddddddddddddddd",gender='male',demo={'hello':'world'}
        )
        obj.save()
        return HttpResponse("hellow world")


class TestView(APIView):
    def get(self,request,*args,**kwargs):
        data = {'name':'rohan','age':26}
        return Response(data)