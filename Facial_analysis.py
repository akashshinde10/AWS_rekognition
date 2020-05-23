import csv
import boto3


with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'facial.jpg'

client = boto3.client('rekognition', 
                       aws_access_key_id = access_key_id, 
                       aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_faces(Image = {'S3Object':{
             'Bucket':'Bucket_name',
             'Name': 'image_name'
                }}  ,
                 Attributes = ['ALL']
)

# to obtain the image from local computer use
# {'Bytes' : source_bytes}
# in place of
# {'S3Object':{
#     'Bucket':'Bucket_name',
#     'name': 'name_of_iamge'
# }} 

print(response)

#FOR MULTIPLE FACES
# for key, value in response.items():
#     if key == 'Facedetails':
#         for people_att in value:
#             print(people_att)
#             print('======')
