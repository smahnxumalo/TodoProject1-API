#from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework import generics 
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from .serializers import *

from .models import *

#CRUD Operations

class ListTask(generics.ListAPIView):   #Read
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetailTask(generics.RetrieveUpdateAPIView):  #update
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):     #Create
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(generics.DestroyAPIView):     #Delete
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


