from moto import mock_aws
from decimal import Decimal

# local modules
from functions.put_visitors_function import app
from test.event import apigw_event
from test.unit.prepare import setup, Expected_VISITORS_KEY, Expected_VISITORS_DATA

@mock_aws
def test_get_visitors_function(apigw_event):
    
    table = setup()

    response = app.lambda_handler(apigw_event, "")
    putVisitorsResult = table.get_item(Key = {'ID': 'visitors'})

    assert response["statusCode"] == 200
    assert putVisitorsResult['Item']['itemdata'] == Decimal(Expected_VISITORS_DATA + 1)