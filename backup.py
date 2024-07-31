import tarfile
import io
from telethon.sync import TelegramClient
import os
import sys
import time
from params import *
import wget

def backup(password):
    if len(sys.argv[1:]) < 1:
        print(f'1 argument required, {len(sys.argv[1:])} recieved.')


    def progress_callback(bytes_sent, bytes_total):
        print(
            f'\x1b[2K\r{name}: sending... ({round(bytes_sent / bytes_total * 100, 2)}%)', end='')


    filename = f"{time.strftime('%d.%m.%Y-%H:%M:%S.tar', time.localtime())}"

    print('Creating tar archive...')

    tar = tarfile.open(tar_file.name, mode='w')
    for arg in sys.argv[1:]:
        tar.add(arg)
    
    tar.close()

    print('Connecting to Telegram...')

    with TelegramClient(app_name, app_id, app_hash) as client:
        client: TelegramClient
        print('Sending data...')

        i = 0
        bytes_sent = 0

        tar_file.seek(0, io.SEEK_END)
        bytes_total = tar_file.tell()
        tar_file.seek(0)

        while True:
            if tar_file.tell() == bytes_total:
                break
            name = f"{filename}.part{i}"
            print(f'\x1b[2K\r{name}: reading...', end='')
            part_bytes = tar_file.read(1024 * 1024 * 1024 * 2)
            bytes_sent += len(part_bytes)

            part = io.BytesIO(part_bytes)
            part.name = name
            print(f'\x1b[2K\r{name}: sending...', end='')
            client.send_file(chat, part, progress_callback=progress_callback)
            print(
                f'\x1b[2K\r{name}: sent! Total progress: {round(bytes_sent / bytes_total * 100, 2)}%')
            i += 1
