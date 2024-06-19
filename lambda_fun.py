import json
import boto3

lambda_Client = boto3.client('lambda', region_name='us-east-2')

response =lambda_Client.create_function(
    Code={
        'S3Bucket': 'udwgdkqoishdbcjhdue',
        'S3Key': 'lambda.zip', #how can i create or fetch this S3Key
    },
    Description='Process image objects from Amazon S3.',
    FunctionName='test-my-function',
    Handler='main.lambda_handler',
    Publish=True,
    Role='arn:aws:iam::471112685796:role/lambda-s3-admin',
    Runtime='python3.12'
)