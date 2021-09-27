import boto3

#connection
client = boto3.client('s3')

#PUT
with open('apple.jpg','rb') as f:
    apple=f.read()

response = client.put_object(
    ACL='private',
    Body=apple,
    Bucket='BucketName',
    Key='apple.jpg'
)
print(response)

#GET
response = client.list_objects(
    Bucket='BucketName',
        )
for x in response.get("Contents"):
    print(x.get("key")) #Data is inside item

#DELETE
response = client.delete_object(
    Bucket='BucketName',
    Key='apple.jpg'
        )
print(response)