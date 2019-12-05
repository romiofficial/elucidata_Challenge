from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import quiz_portal
from .serializers import quiz_portal_Serializer

class quiz(APIView):

    def get(self,request):
        cat=quiz_portal.objects.all()
        serializer=quiz_portal_Serializer(cat,many=True)
        return Response(serializer.data)


    def post(self):
        pass

def home(request):
    return HttpResponse("<h1>welcome to Quiz portal  </h1> <h3> by Rahul Trivedi</h3> ")

def privacypolicy(request):
    template="<h1>PAGE NOT FOUND</h1>"
    return HttpResponse(template)
