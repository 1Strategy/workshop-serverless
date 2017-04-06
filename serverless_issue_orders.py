import boto3
from random import randint

sqs_client = boto3.client('sqs')


def lambda_handler(event, context):
    numbers = [1,2,3]

    try:
        queue_url = sqs_client.get_queue_url(QueueName=event['sqs_name'])['QueueUrl']
        
        response = sqs_client.purge_queue(QueueUrl=queue_url)
        
    
        for num in numbers:
             response = sqs_client.send_message( QueueUrl=queue_url,
                                                MessageBody='Charge Cannons!',
                                                DelaySeconds=0,
                                                MessageAttributes={
                                                    'cannon_identifier': {
                                                        'StringValue': '%d' % num,
                                                        'DataType': 'Number'}})
    except Exception as e:
        print('Unable to write orders to queue: %s '%e)
        
    return event