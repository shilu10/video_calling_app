from django.shortcuts import render
import boto3
import csv
from django.http import JsonResponse, HttpResponse
from .models import computer_bsc
from .aws_connections import *
import io, os
import glob


# creating a s3 client connection using boto3.
S3_CLIENT = create_s3_client()

# pretend it is english exam
current_exam = 'english'


# This will send the json response to the frontend

def post_url(request) :

    # bucketname for storing the video filenames

    bucket_name = 'b.n'

    # this is the video filename
    name = "shilash.bscit1" 


    # instead of using the database, we could just use the csv file to store the filename
    # and upload it to the s3.

    # first checking whether there is already a file exist in the s3.

    # example filename ---> subject + dept

    videos_filenames_file = "computer_bscit.csv"

    # checking is there is filename(key_ present in this name in s3 bucket.

    #Creating Session With Boto3. to put new file or new content.
   
    # this is for the safety purpose, we are uploading the students file to the 
    # s3 bucket
#    try :
        

        #S3_CLIENT.head_object(Bucket = bucket_name, Key = videos_filenames_file)

 #   except :
    v_filepath = os.path.join('files', videos_filenames_file)
    if not os.path.isfile(v_filepath) : 
        print("yea")
        with open(f'files/{videos_filenames_file}', 'wb') as f :
            writer = csv.writer(f)
            writer.writerow(name)
        
    else :
        print(":E")
        name_ = list(name.split(" "))
        with open(f'files/{videos_filenames_file}', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(name_)
        
 #   finally :
  #      file_ = f'files/{videos_filenames_file}.csv'
   #     S3_CLIENT.upload_file(file_, bucket_name, videos_filenames_file)

    # Saving the filename into the table, so we can use it later.
   # record = computer_bsc(filename = name)
    #record.save()
    #console.log(name, "name")
    url = generate_url(name)
    return JsonResponse(url, safe = False)


# this is just a home page(dummy home page)
def test_page(request) :
    return render(request, 'test_page/test_page.html')


def videos_page(request) :
    return render(request, 'test_page/view_videos.html')


def get_filenames(request) :
    filename = request.GET.get('name')
    filepath = os.path.join('files', filename)

   # /django_projects/video_calling_project/files
    try:    
        with open(filepath, 'r') as f:
            csv_reader = csv.reader(f)
            
            filenames_ = [ ]
            for content_list in csv_reader :
                print(csv_reader, str(content_list))
                content = ''.join(content_list) + ','
               # print(c)
                filenames_.append(content)
                       
        file_data = filenames_

        # sending response 
        response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
    

    




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