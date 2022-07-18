from tkinter import ACTIVE
from django.shortcuts import render
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models 
from . import serializers

import datetime 

# Create your views here.
class  PostListApi:
    queryset =  "Link_object.filter" (active=True)
    serializer_class = "LinkSerializer" 

class PostCreateApi:
    queryset = "Link.objects.filter" (active=True)
    serializer_class = "LinkSerializer"

class PostDetailApi:
    queryset = "Link.objects.filter"(active=True)
    serializer_class = "LinkSerializer"

class PostUpdateApi:
    queryset = "Link.object.filter"(active=True)
    serializer_class = "LinkSerializer"

class PostDeleteApi:
    queryset= "Link.objects.filter"(active=True)
    serializer_class = "LinkSerializer"

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

