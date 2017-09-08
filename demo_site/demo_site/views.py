from django.http import HttpResponse
from django.template import loader
import boto3
from botocore.client import Config

client = boto3.client("s3",
                      aws_access_key_id='<your id>',
                      aws_secret_access_key='<your secret>',
                      region_name="ap-northeast-2",
                      config=Config(s3={"signature_version":'s3v4',
                                    "addressing_style":'virtual'}))

def index(request):
    template = loader.get_template('index.html')
    key = "test.txt"
    creds = client.generate_presigned_post("eric-test", key)
    print(creds)
    context = {
        'creds': creds
    }
    return HttpResponse(template.render(context, request))