from django.shortcuts import render
import boto3
from django.http import JsonResponse
from .models import computer_bsc

import io, os


# Aws credentials 

ACCESS_KEY = 'AKIAUPDHPMAWFKG6OG6P'
SECRET_ACCESS_KEY = '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'


# we are creating a s3 client using the boto3, with our aws account. But this should
# be institutions aws account.
S3_CLIENT = boto3.client(
        's3',
        region_name = 'ap-south-1',
        aws_access_key_id = ACCESS_KEY,
        aws_secret_access_key = SECRET_ACCESS_KEY,
    )


session = boto3.Session(

    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_ACCESS_KEY  
    
                            )




# pretend it is english exam
current_exam = 'english'


tables = {
    'computer_bsc' : computer_bsc
}


# Helper function for post_url
def generate_url(filename) :
    
    # Just specify folder_name:
    # key is just a name for the file in s3 bucket, in our case, name or key of the file
    # should be the student mailid or Rollno with current exam.


    # pretend count is the rollno of the student.
   
    # generating the pre-signed-url from the s3 aws.
    url = S3_CLIENT.generate_presigned_url(
        ClientMethod='put_object',
        Params={'Bucket': 'fromjs.upload', 'Key': f"{filename}.mp4"},
        ExpiresIn=60,
    )

    return url

# This will send the json response to the frontend

def post_url(request) :

    # bucketname for storing the video filenames

    bucket_name = 'b.n'

    # this is the video filename
    name = "shilash.bscit2" 


    # instead of using the database, we could just use the csv file to store the filename
    # and upload it to the s3.

    # first checking whether there is already a file exist in the s3.

    # example filename ---> subject + dept

    videos_filenames_file = "computer_bscit"

    # checking is there is filename(key_ present in this name in s3 bucket.

    #Creating Session With Boto3. to put new file or new content.
   

    try :
        print("ss")
        S3_CLIENT.head_object(Bucket = bucket_name, Key = videos_filenames_file)

    except :
        print("not succeed")
        with open('files/new.csv', 'wb') as f :
            name = bytes(name, 'utf-8')
            f.write(name)
        
    else :
        with open('files/new.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(name)

    finally :
        file_ = 'files/new.csv'
        S3_CLIENT.upload_file(file_, bucket_name, videos_filenames_file)

    # Saving the filename into the table, so we can use it later.
   # record = computer_bsc(filename = name)
    #record.save()
    url = generate_url(name)
    return JsonResponse(url, safe = False)


# this is just a home page(dummy home page)
def test_page(request) :
    return render(request, 'test_page/test_page.html')


def videos_page(request) :
    return render(request, 'test_page/view_videos.html')


# this will query the database for the filenames and give it to the frontend.
# this tablename is hardcoded from frontend, but we will soon keep a dropdown boxes 
# for it.
def get_filenames(request) :
    print(request, "request")
    tablename = request.GET.get('name')

    print(tablename, "tablema,e")

    records = tables[tablename].objects.all()
    print(records)




# tomorrow 

# We need to add every bucket key into our database, we need a different database and
# bucket for each subject
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