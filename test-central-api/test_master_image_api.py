import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import MasterImageAPI


class TestMasterImageAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')

        self.api = MasterImageAPI(username, password, base_url)

    @pytest.mark.asyncio
    async def test_master_many_images(self):
        await self.api.get_many()

    @pytest.mark.asyncio
    async def test_master_one_images(self):
        master_images = await self.api.get_many()
        master_image = master_images['data'][0]
        test_master_image = await self.api.get_one(master_image['id'])

        assert master_image['id'] == test_master_image['id']

    @pytest.mark.asyncio
    async def test_master_delete_images(self):
        master_images = await self.api.get_many()
        master_image = master_images['data'][0]
        await self.api.delete(master_image['id'])

        # master_images = await self.api.get_many()
        # print(master_image['id'] in [img['id'] for img in master_images['data']])
        # assert master_image['id'] not in [img['id'] for img in master_images['data']]
        # self.loop.run_until_complete(self.api.close())


if __name__ == '__main__':
    unittest.main()
