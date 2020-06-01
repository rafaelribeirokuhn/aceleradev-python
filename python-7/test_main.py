from main import get_temperature
from unittest import mock


def test_get_temperature_by_lat_lng():
    lat = -14.235004
    lng = -51.92528

    with mock.patch('main.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {
            "currently": {
                "temperature": 62
            }
        }

        celsius_degree = get_temperature(lat, lng)

    assert celsius_degree == 16
