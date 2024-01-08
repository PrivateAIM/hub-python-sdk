import unittest
import os
from dotenv import load_dotenv
from yarl import URL
import asyncio
from hub_python_client import MasterImageAPI


class TestMasterImageAPI(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        base_url = URL(os.getenv('BASE_URL'))
        #username = '5c239847-591a-4087-a48f-226cc02f5dd0'
        #password = 'Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM'
        #base_url = URL('https://dev.personalhealthtrain.de')
        self.loop = asyncio.get_event_loop()

        self.api = MasterImageAPI(username, password, base_url)

    def test_master_many_images(self):
        self.loop.run_until_complete(self.api.get_many())
        self.loop.run_until_complete(self.api.close())

    def test_master_one_images(self):
        master_images = self.loop.run_until_complete(self.api.get_many())
        print(master_images)
        self.loop.run_until_complete(self.api.get_one(master_images['data'][0]['id']))
        self.loop.run_until_complete(self.api.close())

    def test_master_delete_images(self):
        master_images = self.loop.run_until_complete(self.api.get_many())
        print(master_images)
        self.loop.run_until_complete(self.api.delete(master_images['data'][0]['id']))
        self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()
