from django.shortcuts import render
import boto3
from django.http import JsonResponse
from .models import computer_bsc

# pretend it is english exam
current_exam = 'english'


tables = {
    'computer_bsc' : computer_bsc
}



# Helper function for post_url
def generate_url(filename) :
    # we are creating a s3 client using the boto3, with our aws account. But this should
    # be institutions aws account.
    s3_client = boto3.client(
        's3',
        region_name = 'ap-south-1',
        aws_access_key_id = 'AKIAUPDHPMAWFKG6OG6P',
        aws_secret_access_key = '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',
    )

    # Just specify folder_name:
    # key is just a name for the file in s3 bucket, in our case, name or key of the file
    # should be the student mailid or Rollno with current exam.


    # pretend count is the rollno of the student.
   
    # generating the pre-signed-url from the s3 aws.
    url = s3_client.generate_presigned_url(
        ClientMethod='put_object',
        Params={'Bucket': 'fromjs.upload', 'Key': f"{filename}.mp4"},
        ExpiresIn=60,
    )

    return url

# This will send the json response to the frontend

def post_url(request) :

    name = "shilash.bscit2" 
    

    # Saving the filename into the table, so we can use it later.
    record = computer_bsc(filename = name)
    record.save()

    print(record.query, "record")
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