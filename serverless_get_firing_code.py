import boto3

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):

    try:
        response = sfn_client.get_activity_task(activityArn=event['activity_arn'])
        event['firing_code'] = response['taskToken']
    except Exception as error:
        print(error)
    return event
