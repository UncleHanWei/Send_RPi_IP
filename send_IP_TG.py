from telethon import TelegramClient
import subprocess

# Use your own values from https://my.telegram.org
api_id = 123456
api_hash = '0123456789abcdef0123456789abcdef'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('myUserName', api_id, api_hash) as client :
    # Linux Specific shell command
    arg = 'ip route list'
    p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
    data = p.communicate()[0].decode().split()
    ip = data[data.index('src')+1]
    msg = 'The ip of your RaspberryPi is ' + ip
    client.loop.run_until_complete(client.send_message('me', msg))
    print('ip sent')