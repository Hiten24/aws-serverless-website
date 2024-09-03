import json
import boto3

def lambda_handler(event, context):

    dynamoDb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamoDb.Table('hiten-cloud-resume')

    response = table.update_item(
        Key={
            'ID': 'visitors'
        },
        UpdateExpression='SET itemdata = itemdata + :inc',
        ExpressionAttributeValues={
            ':inc': 1
        }
    )

    HTTPStatusCode = response['ResponseMetadata']['HTTPStatusCode']

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "statusCode": HTTPStatusCode,
    }
