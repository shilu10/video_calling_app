
import boto3

# Aws credentials 

ACCESS_KEY = 'AKIAUPDHPMAWFKG6OG6P'
SECRET_ACCESS_KEY = '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'

# we are creating a s3 client using the boto3, with our aws account. But this should
# be institutions aws account.

def create_s3_client() :
    S3_CLIENT = boto3.client(
            's3',
            region_name = 'ap-south-1',
            aws_access_key_id = ACCESS_KEY,
            aws_secret_access_key = SECRET_ACCESS_KEY,
        )
    return S3_CLIENT


session = boto3.Session(

    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_ACCESS_KEY  
    
                            )

# Helper function for post_url
def generate_url(filename) :
    S3_CLIENT = create_s3_client()
    
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

