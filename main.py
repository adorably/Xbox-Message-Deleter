import asyncio
import colorama
import os, sys
import getpass

from source import user_info, storage, index_messages, delete

class Xbox_Message_Deleter():
    def __init__(self) -> None:
        self.store_info = storage.storage
        self.user_information = user_info.Get_User_Information()
        self.get_messages = index_messages.Index_Messages()
        self.delete = delete.Delete_Message()


    async def setup(self) -> None:
        colorama.init(autoreset=True)
        os.system('cls' if sys.platform == 'win32' else 'clear')
        self.store_info.user_token = getpass.getpass(' [\x1b[1;35m?\x1b[39m] Authorization Token: ')
        self.store_info.peer_xuid = input(' [\x1b[1;35m?\x1b[39m] Peer XUID From Chat: ')
        await self.user_information.retrieve_account_info()
        await self.begin_deletion()
        print('\n [\x1b[1;35m+\x1b[39m] Finished Deleting Messages!')


    async def begin_deletion(self) -> None:
        message_data = await self.get_messages.retrieve_messages()

        for message_range in range(len(message_data)):
            sender = message_data[message_range]['sender']
            deleted = message_data[message_range]['isDeleted']

            if sender == self.store_info.user_xuid and not deleted:
                message_id = message_data[message_range]['messageId']
                message_type = message_data[message_range]['contentPayload']['content']['parts'][0]['contentType']

                if message_type == 'text':
                    message_content = message_data[message_range]['contentPayload']['content']['parts'][0]['text']
                else:
                    message_content = message_type

                await self.delete.delete(message_id, message_content)
                await asyncio.sleep(1.25)
            else:
                pass


if __name__ == '__main__':
    asyncio.get_event_loop().\
    run_until_complete(Xbox_Message_Deleter().\
    setup())