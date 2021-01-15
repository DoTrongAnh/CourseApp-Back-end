from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from api.serializers import *
from api.models import *
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import renderers

class EchoViewSet(viewsets.ModelViewSet):
    queryset = Echo.objects.all()
    serializer_class = EchoSerializer
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
"""
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def echos_list(request):
    if request.method == 'GET':
        echos = Echo.objects.all()
        serializer = EchoSerializer(echos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EchoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def echo_details(request, pk):
    try:
        echo = Echo.objects.get(pk=pk)
    except Echo.DoesNotExist:
        return HttpResponse("Echo not found.", status=404)
    if request.method == 'GET':
        serializer = EchoSerializer(echo)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EchoSerializer(echo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        echo.delete()
        return HttpResponse(status=204)
"""            

class CourseOutlineViewSet(viewsets.ModelViewSet):
    queryset = CourseOutline.objects.all()
    serializer_class = CourseOutlineSerializer

class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class AUViewSet(viewsets.ModelViewSet):
    queryset = AU.objects.all()
    serializer_class = AUSerializer