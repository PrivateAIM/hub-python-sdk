import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import StationAPI , StationCreate
from hub_python_client import RegistryAPI

class TestStationAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()

        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')

        self.api_station = StationAPI(username, password, base_url)
        self.api_registry = RegistryAPI(username, password, base_url)


    @pytest.mark.asyncio
    async def test_get_stations(self):
        response = await self.api_station.get_many()
        print(response)

    @pytest.mark.asyncio
    async def test_get_stations(self):
        stations = await self.api_station.get_many()
        station = stations['data'][0]
        station = await self.api_station.get_one(station['id'])

    @pytest.mark.asyncio
    async def test_station_crud(self):
        # Create
        station_name = "station_name_test"
        # TODO get registry id
        registrys =  await self.api_registry.get_many()
        registry_id = registrys['data'][0]['id']


        station = StationCreate(
            external_name=station_name,
            name=station_name,
            ecosystem="tue",
            hidden=False,
            registry_id = registry_id
        )
        station = await self.api_station.create(station)
        print(station)
        # Read


        # read one
        station = await self.api.get_one(station_id)

        # Update


        # Delete


if __name__ == '__main__':
    unittest.main()