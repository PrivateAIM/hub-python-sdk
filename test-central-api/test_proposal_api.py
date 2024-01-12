import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import (ProposalAPI, Proposal, ProposalCreate, ProposalManyResponse,
                               ProposalRisk, ProposalSocketServerToClientEventName,
                               ProposalSocketClientToServerEventName)


class TestProposalAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')

        self.api = ProposalAPI(username, password, base_url)

    @pytest.mark.asyncio
    async def test_proposal_many(self):
        await self.api.get_many()

    @pytest.mark.asyncio
    async def test_proposal_one(self):
        proposals = await self.api.get_many()
        proposal = proposals['data'][0]
        test_proposal = await self.api.get_one(proposal['id'])

        assert proposal['id'] == test_proposal['id']

    @pytest.mark.asyncio
    async def test_proposal_crud(self):
        # Create
        proposal = ProposalCreate(
            title="Proposal Title",
            requested_data="Requested Data add more length to this",
            risk="low",
            risk_comment="No risk comment   add more length to this"
        )

        proposal = await self.api.create(proposal)
        print(proposal)
        # Read
        proposals = await self.api.get_many()
        print(proposals)

        for proposal in proposals['data']:
            if proposal['title'] == 'Proposal Title':
                id = proposal['id']
                break
        self.assertIsNotNone(id)

        # read one
        await self.api.get_one(id)
        # Update
        # TODO: Update
        # Delete
        await self.api.delete(id)
        # check delete
        proposals = await self.api.get_many()
        for proposal in proposals['data']:
            if proposal['title'] == 'Proposal Title':
                id = proposal['id']
                break
        # self.assertIsNone(id)

    @pytest.mark.asyncio
    async def test_proposal_update(self):
        proposal_update = ProposalCreate(...)  # Fill in with appropriate data
        proposal_id = '...'  # Fill in with appropriate id
        await self.api.update(proposal_id, proposal_update)
        # self.loop.run_until_complete(self.api.close())

    @pytest.mark.asyncio
    async def test_proposal_delete(self):
        proposal_id = '...'  # Fill in with appropriate id
        await self.api.delete(proposal_id)
        # self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()
