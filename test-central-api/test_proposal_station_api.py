import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import ProposalStationAPI

from hub_python_client import (ProposalAPI, Proposal, ProposalCreate, ProposalManyResponse,
                               ProposalRisk, ProposalSocketServerToClientEventName,
                               ProposalSocketClientToServerEventName)

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

    #TODO do station first
    @pytest.mark.asyncio
    async def test_aprov_proposl(self):

        test_title = "Proposal Title test"
        proposal = ProposalCreate(
            title=test_title,
            requested_data="Requested Data add more length to this",
            risk=ProposalRisk.LOW,
            risk_comment="No risk comment   add more length to this",
            master_image_id=None
        )

        proposal = await self.api.create(proposal)


if __name__ == '__main__':
    unittest.main()