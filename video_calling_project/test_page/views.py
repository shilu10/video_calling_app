from django.shortcuts import render
import boto3
import csv
from django.http import JsonResponse, HttpResponse
from .models import computer_bsc
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





# tomorrow 

# We need to add every bucket key into our csv file we need a different csv file and
# object for each subject
# eg :
    # if subject = "english" -> need sepearate bucket and database 

# it is even good, we have seperate bucket based on the department, subject. 

# we need to stream the videos based on the request
# eg :
   # if user asks a subject english, for department- xyz.
     # we need to stream that information only.
    
  # if user asks a subject tamil, for department - abc.
    # we need to stream that videos only 

# we will do this by querying the database and getting the keys, for specific subject
# and class. and stream it in fronted. because of cloudfront we just need to change
# the endpoints, which is filename(keys). 

# so we will do it dynamically, by having a dropdown boxes for the subject and dept
# whatever user chooses, we will stream those videos from the bucket.

# we need to stream the video dynamic content. so it html pages, should not contain
# anything. we should dynamically create the things.





# tomorrow ------> ttry to connect the idea with data ingestion and try to get the 
# csv file from the clients and try to create a bucket and everything according to
# it.
# because we neednot have to handle the file at the backend.
# try to implement the code, to create the bucket automatically from the 
# users input and use, it, in the cloudfront we can specify the folders and filename
# to get the video, so we can just use it, for the easier purpose.