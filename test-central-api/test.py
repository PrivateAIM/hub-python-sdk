# develop test
import aiohttp
import asyncio


async def fetch(session, url):
    #headers = {'Authorization': f'Bearer {token}'}
    username = '5c239847-591a-4087-a48f-226cc02f5dd0'
    password = 'Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM'
    async with session.get(url, auth=aiohttp.BasicAuth(username,password)) as response:
        return await response.text()

async def get_token(session, url, secrets, id):
    data = {
        'secrets': secrets,
        'id': id
    }
    async with session.post(url, data=data) as response:
        json_response = await response.json()
        return json_response.get('token')

async def main():
    secrets="Erfj1O_pQxG.Ew1ywnmkCrMjzNxYsxqVj5fd7qaqF4Ow.noXesyU0Auci49SStpM"
    _id="5c239847-591a-4087-a48f-226cc02f5dd0"


    token_url = 'https://dev.personalhealthtrain.de/api/token'  # replace with your actual token URL

    async with aiohttp.ClientSession() as session:
        #token = await get_token(session, token_url, secrets, _id)
        html = await fetch(session, 'https://dev.personalhealthtrain.de/api/user-secrets')
        print(html)
if __name__ == '__main__':
    asyncio.run(main())

