import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import ProposalStationAPI, ProposalAPI, StationAPI, RegistryAPI

from hub_python_client import (ProposalCreate,ProposalRisk , ProposalStationCreate, StationCreate,
                               ProposalStationApprovalStatus , ProposalStation)

class TestProposalStationAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')
        self.api_proposal = ProposalAPI(username, password, base_url)
        self.api_station = StationAPI(username, password, base_url)
        self.api_proposal_station = ProposalStationAPI(username, password, base_url)
        self.api_registry = RegistryAPI(username, password, base_url)

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
        # Create
        test_title = "Proposal Title test"
        proposal = ProposalCreate(
            title=test_title,
            requested_data="Requested Data add more length to this",
            risk=ProposalRisk.LOW,
            risk_comment="No risk comment   add more length to this",
            master_image_id=None
        )

        proposal = await self.api_proposal.create(proposal)

        station_name = f"station_name_test_{os.urandom(8).hex()}"
        registrys = await self.api_registry.get_many()
        registry_id = registrys['data'][0]['id']

        station = StationCreate(
            external_name=station_name,
            name=station_name,
            hidden=False,
            registry_id=registry_id
        )
        station = await self.api_station.create(station)

        proposal_station = ProposalStationCreate(
            approval_status=ProposalStationApprovalStatus.REJECTED,
            proposal_id=proposal['id'],
            station_id=station['id']
        )
        proposal_station = await self.api_proposal_station.create(proposal_station)
        print(proposal_station)
        # Read
        proposal_stations = await self.api_proposal_station.get_many()
        print(proposal_stations)
        proposal_station_id = None
        for proposal_station in proposal_stations['data']:
            if proposal_station['proposal_id'] == proposal['id']:
                proposal_station_id = proposal_station['id']
                break
        self.assertIsNotNone(proposal_station_id)

        # read one
        proposal_station = await self.api_proposal_station.get_one(proposal_station_id)
        # Update
        update_approval_status = ProposalStationApprovalStatus.APPROVED
        proposal_station['approval_status'] = update_approval_status
        print(proposal_station)
        proposal_station = ProposalStation(**proposal_station)
        proposal_station = await self.api_proposal_station.update(proposal_station_id, proposal_station)
        print(proposal_station)


if __name__ == '__main__':
    unittest.main()