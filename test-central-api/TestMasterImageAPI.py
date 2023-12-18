import unittest
from yarl import URL
import asyncio
from hub_python_client import MasterImageAPI


class TestMasterImageAPI(unittest.TestCase):
    def setUp(self):
        username = '5c239847-591a-4087-a48f-226cc02f5dd0'
        password = 'Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM'
        base_url = URL('https://dev.personalhealthtrain.de')
        self.loop = asyncio.get_event_loop()
        # self.api =  self.loop.run_until_complete(MasterImageAPI(username, password, base_url))
        self.api = MasterImageAPI(username, password, base_url)

    def test_master_many_images(self):
        self.loop.run_until_complete(self.api.get_many())
        self.loop.run_until_complete(self.api.close())

    def test_master_one_images(self):
        master_images = self.loop.run_until_complete(self.api.get_many())
        self.loop.run_until_complete(self.api.get_one(master_images['data'][0]['id']))
        self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()
