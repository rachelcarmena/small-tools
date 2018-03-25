import requests
import sys

def request(url, token, params):
    SLACK_API = 'https://slack.com/api'

    headers = {'Authorization': 'Bearer {}'.format(token)}

    response = requests.get(SLACK_API + url, headers = headers, params = params)

    if response.status_code != requests.codes.ok:
        print 'Please, take a look at this: ' + response.text
        sys.exit(0)

    data = response.json()
    if data['ok'] != True:
        print 'ERROR: ' + data['error']
        sys.exit(0)

    return data
