import boto3
from moto import mock_aws

# test data variables
Expected_VISITORS_KEY = 'visitors'
Expected_VISITORS_DATA = 17
TEST_TABLE_NAME = 'hiten-cloud-resume'

@mock_aws
def setup():
    # create mock DynamoDB table
    dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.create_table(
        TableName=TEST_TABLE_NAME,
        KeySchema=[{'AttributeName': 'ID', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'ID', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    )

    table = dynamodb.Table(TEST_TABLE_NAME)

    table.put_item(Item = {
        'ID': Expected_VISITORS_KEY, 
        'itemdata': Expected_VISITORS_DATA
    })

    return table