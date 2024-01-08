import pytest
from unittest.mock import AsyncMock, patch
from hub_python_client.domains.station.api import StationAPI

@pytest.fixture
def station_api():
    return StationAPI()

@patch('hub_python_client.domains.station.api.build_query', new_callable=AsyncMock)
@patch('hub_python_client.domains.station.api.nullify_empty_object_properties', new_callable=AsyncMock)
def test_get_many(build_query_mock, nullify_empty_object_properties_mock, station_api):
    # Arrange
    options = {"key": "value"}
    build_query_mock.return_value = "?key=value"
    station_api.client.get = AsyncMock(return_value={"data": "response"})

    # Act
    response = station_api.get_many(options)

    # Assert
    assert response == {"data": "response"}
    build_query_mock.assert_called_once_with(options)
    station_api.client.get.assert_called_once_with("/stations?key=value")

# Similar tests for get_one, create, update, delete, run_command