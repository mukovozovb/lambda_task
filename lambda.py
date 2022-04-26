import json
import boto3
from datetime import date, datetime
 
REGION = 'us-east-1'

def describe_instances():
    ec2 = boto3.client('ec2', region_name=REGION)
    response = ec2.describe_instances()
    user_info = f'Istance_info: {response}'
    return user_info
        
def delete_instance():
    ec2 = boto3.client('ec2', region_name=REGION) 
    instances = ec2.describe_instances(Filters=[{
    'Name': 'instance-type', 
    'Values': ["t2.micro"]}
    ,{
    'Name': 'instance-state-name',
    'Values': ['running']
    }])['Reservations'][0]['Instances'][0]['InstanceId']
    ec2.terminate_instances(InstanceIds=[instances,])
    user_info = f'instance {instances} was terminated'
    return user_info

    
def create_instance():
    AMI = 'ami-0f9fc25dd2506cf6d'
    INSTANCE_TYPE = 't2.micro'
    KEY_NAME = 'TEST'
    ec2 = boto3.client('ec2', region_name=REGION)
    instance = ec2.run_instances(
            ImageId=AMI,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MaxCount=1,
            MinCount=1
        )
    instance_id = instance['Instances'][0]['InstanceId']
    user_info = f'instance was created with id {instance_id}'
    return user_info
    
    
 
def lambda_handler(event, context):
    test1 = event["action"]
    if test1 == "create" :
        return create_instance()
    elif test1 == "delete":
        return delete_instance()
    elif test1 == "describe":
        return describe_instances()