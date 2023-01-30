import boto3

s3 = boto3.client("s3")

bucket_name = sys.argv[1]
filename = sys.argv[2]
local_file_name = sys.argv[3]
s3.upload_file(local_file_name, bucket_name, filename)
