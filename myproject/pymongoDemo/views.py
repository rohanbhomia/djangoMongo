from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
database = myclient["db1"]
collection = database["table1"]



class PymongoView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self,request,*args):
        todo_id = request.query_params.get('todo_id')
        if todo_id is not None:
            data = self.get_one(request,todo_id)
               
        else:
            data = list(collection.find({}, {'_id': False}))
            data = {'data':data}

        return Response(data)

    def post(self,request):
        result = collection.find_one({"todo_id": request.data['todo_id']})
        if result is None:
            collection.insert_one(request.data)
            data = {'status':200}
            return Response(data)
        else:
            data = {'status':400}
            return Response(data)
    
    def get_one(self,request,todo_id):
        data = collection.find_one({"todo_id": int(todo_id)}, {'_id': False}) 
        if data is None:
            data = {'status':400,
            'message':'Record not found'}
        return data



@api_view()
@permission_classes([IsAuthenticated])
def get_todo(request):
    data = list(collection.find({}, {'_id': False}))
    data = {'data':data}
    return Response(data)
    return Response({"message": "Hello, world!"})
