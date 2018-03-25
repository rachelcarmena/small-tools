# coding=utf-8
import sys
import getpass
from slack_api.get import *
from download.image import *
from latex.format import *

def get_image_url(user_profile):
    keys = ('image_1024', 'image_512', 'image_192', 'image_original')
    for key in keys:
        if user_profile.has_key(key) and not user_profile[key] == '':
            return user_profile[key]
    return 'no_image'

def get_users_info(token, user_ids):
    users_info = {} 
    for user_id in user_ids:
        user_profile = get_profile(token, user_id)
        users_info[user_id] = {'name': user_profile['real_name'], 'image_url': get_image_url(user_profile)}
    return users_info

def download_user_images(user_ids, users_info):
    for user_id in user_ids:
        download_image(user_id, users_info[user_id]['image_url'])

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('UTF8')

    token = getpass.getpass('Token: ')
    channel_name = raw_input('Channel id: ')

    messages = get_messages_from_channel(token, channel_name)
    messages.reverse()

    user_ids = set()
    for message in messages:
        user_ids.add(message['user'])
        if message.has_key('thread_ts'):
            thread_id = message['thread_ts']
            message['thread_messages'] = get_messages_from_thread(token, channel_name, thread_id)
                
    users_info = get_users_info(token, user_ids)
    download_user_images(user_ids, users_info)

    print_tex(messages, users_info)
