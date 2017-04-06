import boto3

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    
    response = sfn_client.get_activity_task(activityArn=event['activity_arn'])
    
    event['firing_code'] = response['taskToken']
    return event