import pytest
import requests_mock
from src.services.getPostcode import get_postcodes1

def test_get_postcodes_success():
    with requests_mock.Mocker() as m:
        endpoint = "https://api.postcodes.io/postcodes?"
        expected_postcode = "SW1A 1AA"
        response_json = {
            "status": 200,
            "result": [{"postcode": expected_postcode, "distance": 10}]
        }
        m.get(f"{endpoint}lat=51.501009&lon=-0.141588", json=response_json)
        result = get_postcodes1(51.501009, -0.141588)
        assert result == expected_postcode

def test_get_postcodes_no_results():
    with requests_mock.Mocker() as m:
        endpoint = "https://api.postcodes.io/postcodes?"
        m.get(f"{endpoint}lat=51.501009&lon=-0.141588", json={"status": 200, "result": []})
        result = get_postcodes1(51.501009, -0.141588)
        assert result is None

def test_get_postcodes_api_failure():
    with requests_mock.Mocker() as m:
        endpoint = "https://api.postcodes.io/postcodes?"
        m.get(f"{endpoint}lat=51.501009&lon=-0.141588", json={"status": 500, "result": None})
        result = get_postcodes1(51.501009, -0.141588)
        assert result is None

def test_get_postcodes_invalid_json():
    with requests_mock.Mocker() as m:
        endpoint = "https://api.postcodes.io/postcodes?"
        m.get(f"{endpoint}lat=51.501009&lon=-0.141588", text="Not JSON")
        result = get_postcodes1(51.501009, -0.141588)
        assert result is None

def test_get_postcodes_missing_lat_lon():
    result = get_postcodes1(None, -0.141588)
    assert result is None
    result = get_postcodes1(51.501009, None)
    assert result is None
