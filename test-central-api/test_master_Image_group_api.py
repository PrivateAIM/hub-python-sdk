import unittest
import os
from dotenv import load_dotenv
import pytest
from hub_python_client import MasterImageGroupAPI


class TestMasterImageGroupAPI(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        username = os.getenv('USERNAME_ROBOT')
        password = os.getenv('PASSWORD_ROBOT')
        base_url = os.getenv('BASE_URL')

        self.api = MasterImageGroupAPI(username, password, base_url)

    @pytest.mark.asyncio
    async def test_master_many_image_groups(self):
        await self.api.get_many()

    @pytest.mark.asyncio
    async def test_master_one_image_group(self):
        master_image_groups = await self.api.get_many()
        master_image_group = master_image_groups['data'][0]
        test_master_image_group = await self.api.get_one(master_image_group['id'])

        assert master_image_group['id'] == test_master_image_group['id']


if __name__ == '__main__':
    unittest.main()
