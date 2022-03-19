import aiohttp

from source import storage

class Delete_Message():
    def __init__(self) -> None:
        self.user_info = storage.storage

    async def delete(self, message_id, message_content) -> None:
        session = aiohttp.ClientSession()

        async with session.delete(\
            f'https://xblmessaging.xboxlive.com/network/xbox/users/me/conversations/{self.user_info.conversation_id}/messages/{message_id}',\
        headers={
            'Authorization': self.user_info.user_token,
            'x-xbl-contract-version': '1'
        })\
        as delete_message_request:
            if delete_message_request.status == 200:
                print(f' [\x1b[1;35m+\x1b[39m] Deleted Message  |  ID: ({message_id})  |  Content: {message_content}')
            else:
                print(f' [\x1b[1;31m!\x1b[39m] \x1b[1;31mFailed\x1b[39m to Delete Message  |  ID: ({message_id})  |  Content: {message_content}')
    
        await session.close()