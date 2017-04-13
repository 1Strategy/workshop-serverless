import boto3
import json
import datetime

# Use the Boto3 SDK to create a client to call SNS functions
sns_client = boto3.client('sns', region_name='us-west-2')


def lambda_handler(event, context):

    if 'firing_code' in event:
        publish_to_sns(message_send_firing_code(event), event['sns_arn'])
        return

    if 'planet_destroyed' == event['message']['message_context']:
        publish_to_sns(message_planet_destroyed(event), event['sns_arn'])
        return

    if 'hesitation' == event['message']['message_context']:
        publish_to_sns(message_hesitation(event), event['sns_arn'])
        return


def publish_to_sns(message, sns_arn):
    print('Published SNS message: {}'.format(message))
    sns_client.publish( TopicArn=sns_arn,
                        Message="{message}".format(message=message),
                        Subject='Serverless Architecitures Workshop Notification')


def message_planet_destroyed(event):
    sns_message = ''
    sns_message += '{rank} {name}, {planet}'.format(rank=event['commander']['rank'],
                                                    name=event['commander']['name'],
                                                    planet=event['planet_name'])
    sns_message += ' has been destroyed. Your demonstration of power was successful. ' + \
                   'You are now the ultimate power in the universe. https://www.youtube.com/embed/GhHyD4RNyvM?start=17&end=40'
    return sns_message


def message_send_firing_code(event):
    sns_message = ''
    sns_message += '{rank} {name}, {planet}'.format(rank=event['commander']['rank'],
                                                    name=event['commander']['name'],
                                                    planet=event['planet_name'])
    sns_message += ' has been targeted. The firing code is: {firing_code}'.format(firing_code=event['firing_code'])
    return sns_message


def message_hesitation(event):
    sns_message = ''
    sns_message += '{rank} {name}, {planet}'.format(rank=event['commander']['rank'],
                                                    name=event['commander']['name'],
                                                    planet=event['planet_name'])
    sns_message += ' was not destroyed. Your hesitation will be reported to Lord Vader.'
    return sns_message

#
# event = {
#         "sqs_name": "your-name-queue",
#         "activity_arn": "arn:aws:states:us-west-2:281782457076:activity:serverless_issue_fire_command",
#         "cannon_3_charge_status": "successful",
#         "cannon_1_charge_status": "successful",
#         "travel_distance": 86,
#         "cannon_2_charge_status": "successful",
#         "planet_name": "Corellia",
#         "sns_arn": "arn:aws:sns:us-west-2:281782457076:jiravani-notification",
#         "message": {
#             "message_context": "planet_destroyed",
#             "message_payload": " has been destroyed. Your demonstration of power was successful. You are now the ultimate power in the universe. https://www.youtube.com/embed/GhHyD4RNyvM?start=17&end=40",
#             "firing_code": "somefiringcode"
#         },
#         "commander": {
#         	"name": "<REPLACE ME>",
#         	"rank": "<REPLACE ME>"
#         }
#     }
#
#
#     # if 'message' not in event:
#     #     message = "Error: 'message' key not found in input payload" + str(event)
#     #     publish_to_sns(message, event['sns_arn'])
#     #     raise ValueError('Error: "message" key not found in input payload')
#     #
#     # if 'message_context' not in event['message']:
#     #     message = "Error: 'message_context' key not found in input payload" + str(event)
#     #     publish_to_sns(message, event['sns_arn'])
#     #     raise ValueError("Error: 'message_context' key not found in input payload")
