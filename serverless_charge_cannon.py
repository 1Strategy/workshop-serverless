import boto3
import json

sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    
    queue_url = sqs_client.get_queue_url(QueueName=event['sqs_name'])['QueueUrl']
    cannon_identifier = str(event['cannon_identifier'])
    
    sqs_response = sqs_client.receive_message(  QueueUrl=queue_url, 
                                                WaitTimeSeconds=20,
                                                AttributeNames=['All'],
                                                MessageAttributeNames=['cannon_identifier'],
                                                MaxNumberOfMessages=3)
    
    # Raise an error if no messages exist in the queue
    if 'Messages' not in sqs_response:
        raise Exception('No Available Orders Found')

    for message in sqs_response['Messages']:
        
        # Determine what cannon the message is intended for. True if this cannon, false otherwise
        order_intended_for_me = False if message['MessageAttributes']['cannon_identifier']['StringValue'] is not cannon_identifier else True
        
        # If this cannon is the has a message on the queue
        if order_intended_for_me:
            
            # Delete the message on the queue and signal that this cannon has "powered on"
            sqs_client.delete_message(  QueueUrl=queue_url, 
                                        ReceiptHandle=message['ReceiptHandle'])
            return {"cannon_%s_charge_status" %  cannon_identifier: 'successful'}
    
    # if no queue message are found for this entity, throw an error
    raise Exception('No Orders Found For Cannon: %s' % cannon_identifier)