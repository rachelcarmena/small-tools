from http.request import *

def get_messages_from_channel(token, channel_name):
    params = {'channel': channel_name}

    response = request('/conversations.history', token, params)
    return response['messages']

def get_messages_from_thread(token, channel_name, thread_id):
    params = {'channel': channel_name, 'thread_ts': thread_id}

    response = request('/channels.replies', token, params)
    return response['messages']

def get_profile(token, user_id):
    params = {'user': user_id}

    response = request('/users.profile.get', token, params)
    return response['profile']
