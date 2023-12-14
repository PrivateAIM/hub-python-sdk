import unittest
from yarl import URL
import asyncio
from hub_python_client import MasterImageAPI


class TestMasterImageAPI(unittest.TestCase):
    def setUp(self):
        username = '5c239847-591a-4087-a48f-226cc02f5dd0'
        password = 'Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM'
        base_url = URL('https://dev.personalhealthtrain.de')
        self.api = MasterImageAPI(username, password, base_url)


    def test_something(self):


        loop = asyncio.get_event_loop()
        master_images = loop.run_until_complete(self.api.get_many())
        print(master_images)
        first_master_image = loop.run_until_complete(self.api.get_one(master_images['data'][0]['id']))
        print(first_master_image)
        loop.run_until_complete(self.api.close())

        #self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
