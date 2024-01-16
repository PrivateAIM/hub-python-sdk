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
        test_title = "Proposal Title test"
        proposal = ProposalCreate(
            title=test_title,
            requested_data="Requested Data add more length to this",
            risk=ProposalRisk.LOW,
            risk_comment="No risk comment   add more length to this",
            master_image_id=None
        )

        proposal = await self.api.create(proposal)
        print(proposal)
        # Read
        proposals = await self.api.get_many()
        print(proposals)
        proposal_id = None
        for proposal in proposals['data']:
            if proposal['title'] == test_title:
                proposal_id = proposal['id']
                break
        self.assertIsNotNone(proposal_id)

        # read one
        proposal = await self.api.get_one(proposal_id)
        # Update
        update_risk_comment=  "this is a change to the risk comment"
        proposal['risk_comment'] = update_risk_comment
        proposal = await self.api.update(proposal_id, proposal)

        self.assertEqual(proposal['risk_comment'], update_risk_comment)


        # Delete
        await self.api.delete(proposal_id)
        # check delete
        proposal_id = None
        proposals = await self.api.get_many()
        for proposal in proposals['data']:
            if proposal['title'] == test_title:
                proposal_id = proposal['id']
                break
        self.assertIsNone(proposal_id)



if __name__ == '__main__':
    unittest.main()
