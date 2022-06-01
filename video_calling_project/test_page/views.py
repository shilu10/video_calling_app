from django.shortcuts import render
import boto3
import csv
from django.http import JsonResponse, HttpResponse
from .aws_connections import *
import io, os
import glob
from django.views.decorators.csrf import csrf_exempt


# creating a s3 client connection using boto3.
S3_CLIENT = create_s3_client()


# This will send the json response to the frontend
def post_url(request) :
    folder_name = request.GET.get('folder_name')
    filename = request.GET.get('name')

    # this will generate a url from the bucket he/she writing the exam.  
    url = generate_url(folder_name, filename)
    return JsonResponse(url, safe = False)


# this is just a home page(dummy home page)
def test_page(request) :
    return render(request, 'test_page/test_page.html')

@csrf_exempt
def videos_page(request) :
    return render(request, 'test_page/view_videos.html')

def take_tst(request) :
    return render(request, 'test_page/test_home.html')

def test_info(request):
    return render(request, 'test_page/test_info.html')