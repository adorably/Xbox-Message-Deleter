import aiohttp, os

from source import storage

class Index_Messages():
    def __init__(self) -> None:
        self.user_info = storage.storage

    async def retrieve_messages(self) -> None:
        session = aiohttp.ClientSession()

        async with session.get(f'https://xblmessaging.xboxlive.com/network/xbox/users/me/conversations/users/xuid({self.user_info.peer_xuid})?maxItems=1000', 
        headers={
            'Authorization': self.user_info.user_token,
            'x-xbl-contract-version': '1'
        })\
        as message_request:
            if message_request.status == 200:

                retrieved_data = await message_request.json()
                messages = retrieved_data['messages']
                if len(messages) > 0:
                    self.user_info.conversation_id = retrieved_data['conversationId']
                    print(f' [\x1b[1;35m*\x1b[39m] Retrieved \x1b[1;35m{len(messages)}\x1b[39m Messages With \x1b[1;32m{self.user_info.peer_xuid}\x1b[39m')
                else:
                    print(f' [\x1b[1;33m!\x1b[39m] No Messages Exist With \x1b[1;33m{self.user_info.peer_xuid}')
                    os._exit(0)

            else:
                print(f' [\x1b[1;31m!\x1b[39m] \x1b[1;31mFailed\x1b[39m to Retrieve Messages With \x1b[1;33m{self.user_info.peer_xuid}\x1b[39m')
                os._exit(0)

        await session.close()
        return messages