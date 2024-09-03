import json
import boto3
from decimal import Decimal

# dynamoDb = boto3.resource('dynamodb')
# table = dynamoDb.Table('hiten-cloud-resume')

def lambda_handler(event, context):

    dynamoDb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamoDb.Table('hiten-cloud-resume')

    response = table.get_item(
        Key = {
            'ID': 'visitors'
        }
    )

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "statusCode": 200,
        "body": json.dumps({
            "visitors": str(response['Item']['itemdata'])
        }),
    }