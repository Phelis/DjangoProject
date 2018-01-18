from django.shortcuts import render
from django.utils import timezone
from .models import Post

from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    print (posts)
    return render(request, 'blog/post_list.html',{ 'posts': posts } ,{})

def post_listA(request):
    print ("post_listA")
    return render(request, 'blog/blank.html', {})

# [GET] api/shares/
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def create(request):
    if request.method == 'GET':
        content = {
            'status': 'request was permitted'
        }
    else:
        content = {
            'status': 'request was permitted'
        }
    return Response(content)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def some_func(request):
    if request.method == 'GET':
        content = {
            'status': 'request was permitted'
        }
    else:
        content = {
            'status': 'request was permitted'
        }
    return Response(content)
