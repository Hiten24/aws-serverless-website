import json
import pytest
from moto import mock_aws
from decimal import Decimal

# local modules
from functions.get_visitors_function import app
from test.event import apigw_event
from test.unit.prepare import setup, Expected_VISITORS_KEY, Expected_VISITORS_DATA


@mock_aws
def test_get_visitors_function(apigw_event):
    
    setup()

    response = app.lambda_handler(apigw_event, "")
    data = json.loads(response["body"])
    visitorCount = data[Expected_VISITORS_KEY]

    assert response["statusCode"] == 200
    assert Expected_VISITORS_KEY in response["body"]
    assert Decimal(visitorCount) == Expected_VISITORS_DATA