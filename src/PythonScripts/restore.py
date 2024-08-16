from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
from params import *
import tarfile
import sys

if len(sys.argv[1:]) < 1:
    print(f'1 or more argument required, {len(sys.argv[1:])} recieved.')


def progress_callback(bytes_sent, bytes_total):
    print(
        f'\x1b[2K\r{name}: saving... ({round(bytes_sent / bytes_total * 100, 2)}%)', end='')


print('Connecting to Telegram...')

with TelegramClient(app_name, app_id, app_hash) as client:
    client: TelegramClient
    messages = []
    bytes_total = 0

    for message in client.iter_messages(chat, None, filter=InputMessagesFilterDocument):
        messages.append(message)
        bytes_total += message.media.document.size
        if message.media.document.attributes[0].file_name.endswith('part0'):
            break
    messages.reverse()

    bytes_received = 0
    for message in messages:
        name = message.media.document.attributes[0].file_name

        print(f'\x1b[2K\r{name}: downloading...', end='')
        part = client.download_media(message, bytes)
        bytes_received += message.media.document.size
        print(f'\x1b[2K\r{name}: saving...', end='')
        tar_file.write(part)
        print(
            f'\x1b[2K\r{name}: saved! Total progress: {round(bytes_received / bytes_total * 100, 2)}%')

tar = tarfile.open(tar_file.name, mode='r')
tar.extractall(sys.argv[1])
tar.close()
