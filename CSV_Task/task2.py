'''
1. Download file a.csv from S3 bucket
2. Split them to a1.csv and a2.csv
3. Recombine them to b.csv
3. Upload the resulting filesto S3 bucket
'''


import task1 as t1
import pandas as pd
import boto3
from boto3.session import Session

KEY_ID = 'your_access_key'
SECRET_KEY = 'your_secret_key'


def upload_file(file):
    bucket_name = 'lingesh-k-bucket1'
    s3 = boto3.client('s3', aws_access_key_id=KEY_ID,
                       aws_secret_access_key=SECRET_KEY)
    s3.upload_file(file, bucket_name, file)
    return True


if __name__ == "__main__":
    session = Session(aws_access_key_id=KEY_ID,
    aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('lingesh-k-bucket1')
    for s3_file in your_bucket.objects.all():
        print(f"File in bucket: {s3_file.key}")  # prints the contents of bucket
        file = str(s3_file.key)
    print(f"{file} in Bucket!")
    t1.split_data(file)
    t1.check_csv()
    t1.combine_data('a1.csv', 'a2.csv')
    b = pd.read_csv('b.csv')
    print('b.csv')
    print(b.head())  
    # Uploading files to S3 Bucket
    print('Writing the files')
    for item in ['a1.csv', 'a2.csv', 'b.csv']:
        upload_file(item)
    print('Writing done!')
