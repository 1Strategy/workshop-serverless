from __future__ import print_function
import random
import boto3
import json
import decimal
import pprint
import math
from boto3.dynamodb.conditions import Key, Attr


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


# establish a connection with DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

# Randomly select a planet to target
systemList = (11, 93, 99, 57, 92, 9, 86, 50, 29, 31, 71, 13, 56, 17, 45, 72,
              19, 23, 49, 64)


def lambda_handler(event, context):

    galaxy = dynamodb.Table(event['dynamodb_table'])
    """Handler function that Lambda will execute"""
    choice = random.randint(0, len(systemList)-1)
    planet = str(systemList[choice])

    try:
        response = galaxy.query(    ExpressionAttributeNames={'#nm': 'planetName','#rgn': 'region'},
                                    ProjectionExpression='#nm, #rgn',
                                    KeyConditionExpression=Key('id').eq(planet))
    except Exception as e:
        print("{}".format(e))
        event['planet_name'] = 'Jedha'
        event['travel_distance'] = random.randint(99, 101)
        return event

    target = response['Items'][0]
    event['planet_name'] = target['planetName']
    if target['region'] in ['Unknown', 'Outer Rim', 'Mid Rim']:
        event['travel_distance'] = random.randint(100, 10000)
    else:
        event['travel_distance'] = random.randint(1, 99)
    print(event)
    return(event)


lambda_handler({'dynamodb_table':'potato'},{})
