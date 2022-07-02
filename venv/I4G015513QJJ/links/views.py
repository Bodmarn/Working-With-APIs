from tkinter import ACTIVE
from django.shortcuts import render

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

