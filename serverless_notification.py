import boto3
import json
import datetime

# Use the Boto3 SDK to create a client to call SNS functions
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    message = ""
    commander = ""
    
    # If the event payload contains a 'message' key, use that else display default message
    if 'message' in event:
        message = event['message']
    else:
        message = str(event)
    
    
    # If the event payload contains a 'commander' key, include name and rank in the message
    if 'commander' in event:
        commander = "%s %s" % (event['commander']['rank'], event['commander']['name'])
        
    sns_client.publish( TopicArn=event['sns_arn'],
                        Message="%s, %s" % (commander, message),
                        Subject='Serverless Architecitures Workshop Notification')
    if 'message' in event:
        del event['message']    
    