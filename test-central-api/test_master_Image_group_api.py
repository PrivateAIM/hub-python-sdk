import unittest
import os
from dotenv import load_dotenv
from httpx import URL
import asyncio
from hub_python_client import MasterImageGroupAPI


class TestMasterImageGroupAPI(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = URL(os.getenv('BASE_URL'))
        self.loop = asyncio.get_event_loop()

        self.api = MasterImageGroupAPI(username, password, base_url)

    def test_master_many_image_groups(self):
        self.loop.run_until_complete(self.api.get_many())
        # self.loop.run_until_complete(self.api.close())

    def test_master_one_image_group(self):
        master_image_groups = self.loop.run_until_complete(self.api.get_many())
        print(master_image_groups)
        self.loop.run_until_complete(self.api.get_one(master_image_groups['data'][0]['id']))
        # self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()