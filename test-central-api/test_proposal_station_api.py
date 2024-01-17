import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import ProposalStationAPI

class TestProposalStationAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')
        self.api = ProposalStationAPI(username, password, base_url)

    @pytest.mark.asyncio
    async def test_get_proposal_station(self):
        response = await self.api.get_many()
        print(response)

    @pytest.mark.asyncio
    async def test_get_proposal_station(self):
        proposal_station = await self.api.get_many()
        proposal_station = proposal_station['data'][0]
        proposal_station = await self.api.get_one(proposal_station['id'])
        assert proposal_station['id'] == test_proposal_station['id']


if __name__ == '__main__':
    unittest.main()