import unittest
import os
from dotenv import load_dotenv
from yarl import URL
import asyncio
from hub_python_client import (ProposalAPI, Proposal, ProposalCreate, ProposalManyResponse,
                               ProposalRisk, ProposalSocketServerToClientEventName,
                               ProposalSocketClientToServerEventName)


class TestProposalAPI(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        #base_url = URL(os.getenv('BASE_URL'))
        base_url = os.getenv('BASE_URL')
        self.loop = asyncio.get_event_loop()

        self.api = ProposalAPI(username, password, base_url)

    def test_proposal_many(self):
        self.loop.run_until_complete(self.api.get_many())
        self.loop.run_until_complete(self.api.close())

    def test_proposal_one(self):
        proposals = self.loop.run_until_complete(self.api.get_many())
        print(proposals)
        self.loop.run_until_complete(self.api.get_one(proposals['data'][0]['id']))
        self.loop.run_until_complete(self.api.close())

    def test_proposal_crud(self):
        # Create
        proposal = ProposalCreate(
            title="Proposal Title",
            requested_data="Requested Data add more length to this",
            risk="low",
            risk_comment="No risk comment   add more length to this"
            #master_image_id=None
        )

        proposal= self.loop.run_until_complete(self.api.create(proposal))
        print(proposal)
        # Read
        proposals = self.loop.run_until_complete(self.api.get_many())
        print(proposals)

        for proposal in proposals['data']:
            if proposal['title'] == 'Proposal Title':
                id = proposal['id']
                break
        self.assertIsNotNone(id)

        # read one
        self.loop.run_until_complete(self.api.get_one(id))
        # Update
        # TODO: Update
        # Delete
        self.loop.run_until_complete(self.api.delete(id))
        # check delete
        proposals = self.loop.run_until_complete(self.api.get_many())
        for proposal in proposals['data']:
            if proposal['title'] == 'Proposal Title':
                id = proposal['id']
                break
        self.assertIsNone(id)
        self.loop.run_until_complete(self.api.close())


    def test_proposal_update(self):
        proposal_update = ProposalCreate(...)  # Fill in with appropriate data
        proposal_id = '...'  # Fill in with appropriate id
        self.loop.run_until_complete(self.api.update(proposal_id, proposal_update))
        self.loop.run_until_complete(self.api.close())

    def test_proposal_delete(self):
        proposal_id = '...'  # Fill in with appropriate id
        self.loop.run_until_complete(self.api.delete(proposal_id))
        self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()
