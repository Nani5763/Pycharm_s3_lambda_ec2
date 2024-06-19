import boto3


def lambda_handler(event, context):
    print("************Started lambda_handler ************")

    ec2 = boto3.client('ec2', region_name='us-east-2')

    response = ec2.run_instances(
        ImageId= 'ami-033fabdd332044f06',
        InstanceType= 't2.micro',
        KeyName= 'key',
        MaxCount=1,
        MinCount=1
    )

    print("************Started lambda_handler ************")