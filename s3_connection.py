import boto3
import uuid

header = "https://image-database-system.s3.ap-south-1.amazonaws.com"

def image_unique_name():
    return "img-" + str(uuid.uuid1())


print(image_unique_name())

# s3 = boto3.resource("s3")
# bucket = s3.Bucket("image-database-system")
# Data ingestion pipeline would be to s3 bucket
# bucket.upload_file(r'data\kurama.jpg', f'images/label2/{image_unique_name()}.jpeg', ExtraArgs={'ACL': 'public-read'})

# For bulk upload we need to ask path


# Read File Path
# s3 = boto3.resource("s3")
# bucket = s3.Bucket("image-database-system")
#
# print([obj.key for obj in bucket.objects.all()])
# print([obj.key for obj in bucket.objects.filter(Prefix="images/")])