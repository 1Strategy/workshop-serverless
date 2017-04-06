import boto3
import json


def lambda_handler(event, context):
    
    sfn_client = boto3.client('stepfunctions')
    
    task_token = event['body']
    return_payload = {
        "statusCode": 200,
        "headers": {}
    }
    
    try:
        sfn_client.send_task_success(taskToken=task_token, output="{}")
    except Exception as e:
        
        print(e)
        return_payload['body'] = "Firing Code Invalid!\n"
        return return_payload 
    
    return_payload['body'] = "Firing Code Accepted!\n"
    return return_payload 
    