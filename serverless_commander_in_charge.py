import os
def lambda_handler(event, context):
    
    event['activity_arn'] = os.environ['activity_arn']
    event['sns_arn']      = os.environ['sns_arn']
    event['sqs_name']     = os.environ['sqs_name']
    event['commander']    = {
                                "rank":"<REPLACE ME>",
                                "name":"<REPLACE ME>"
                            }
    return event