import aiohttp, os

from source import storage

class Get_User_Information():
    def __init__(self) -> None:
        self.user_storage = storage.storage

    async def retrieve_account_info(self) -> None:
        user_session = aiohttp.ClientSession()

        async with user_session.get('https://profile.xboxlive.com/users/me/profile/settings', 
        headers={
            'Authorization': self.user_storage.user_token,
            'x-xbl-contract-version': '2'
        })\
        as user_info_request:
            if user_info_request.status == 200:
                response_data = await user_info_request.json()
                self.user_storage.user_xuid = response_data['profileUsers'][0]['id']
                print(f'\n \x1b[1;39m[\x1b[1;35m*\x1b[1;39m] Retrieved Profile Information! \n [\x1b[1;35m*\x1b[39m] My XUID: \x1b[1;35m{self.user_storage.user_xuid}\n')
            else:
                print(' \x1b[1;39m[\x1b[1;31m!\x1b[1;39m] Failed to retrieve profile xuid!')
                os._exit(0)

        await user_session.close()