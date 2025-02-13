import boto3
import os 


# we are creating a s3 client using the boto3, with our aws account. But this should
# be institutions aws account.
def create_s3_client() :
    S3_CLIENT = boto3.client(
            's3',
            region_name = 'ap-south-1',
            aws_access_key_id = os.env['ACCESS_KEY'],
            aws_secret_access_key = os.env['SECRET_ACCESS_KEY'],
                          )
    return S3_CLIENT

session = boto3.Session(
    aws_access_key_id = os.env['ACCESS_KEY'],
    aws_secret_access_key = os.env['SECRET_ACCESS_KEY']  
                        )

# Helper function for post_url
def generate_url(folder_name, filename) :
    S3_CLIENT = create_s3_client()
    # generating the pre-signed-url from the s3 aws.
    url = S3_CLIENT.generate_presigned_url(
        ClientMethod = 'put_object',
        Params = {'Bucket': f'student.videos.bucket', 'Key': f"{folder_name}/{filename}.mp4"},
        ExpiresIn = 60,
    )
    return url

