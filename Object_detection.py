import csv
import boto3


with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'hot_air_baloon.jpg'

client = boto3.client('rekognition', 
                       aws_access_key_id = access_key_id, 
                       aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image = {'Bytes' : source_bytes
             },   
                              MaxLabels = 2)

# to obtain the image from s3_bucket use
# {'S3Object':{
#     'Bucket':'Bucket_name',
#     'name': 'name_of_iamge'
# }} 
# in place of
# {'Bytes' : source_bytes}

print(response)