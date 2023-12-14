from hub_python_client import MasterImageAPI
import asyncio
from yarl import URL
#test

def test_master_image_api(username, password, base_url):
    master_image_api = MasterImageAPI(username, password, base_url)

    loop = asyncio.get_event_loop()
    master_images = loop.run_until_complete(master_image_api.get_many())
    print(master_images)
    first_master_image = loop.run_until_complete(master_image_api.get_one(master_images['data'][0]['id']))
    print(first_master_image)
    loop.run_until_complete(master_image_api.close())



if __name__ == '__main__':
    username = '5c239847-591a-4087-a48f-226cc02f5dd0'
    password = 'Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM'
    base_url = URL('https://dev.personalhealthtrain.de')
    test_master_image_api(username, password, base_url)