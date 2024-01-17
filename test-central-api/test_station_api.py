import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import StationAPI


class TestStationAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')
        self.api = StationAPI(username, password, base_url)

    @pytest.mark.asyncio
    async def test_get_proposal_station(self):
        response = await self.api.get_many()
        print(response)
