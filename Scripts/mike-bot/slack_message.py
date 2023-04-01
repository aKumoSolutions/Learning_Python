import pprint, requests, os
from github_status import github_status
from slack_status import slack_status
from digital_ocean_status import digitalocean_status
pp = pprint.PrettyPrinter(indent=4)


SLACK_URL = os.getenv("slack_url")

def slack_message(data):
    url = SLACK_URL
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % data

    slack_resp = requests.post(url, headers=header, data=data)
    print(slack_resp)
    return slack_resp

if 'ok' not in slack_status():
    slack_message(data=slack_status())
    
if "All Systems Operational" not in github_status():
    slack_message(data=github_status())

if "All Systems Operational" not in digitalocean_status():
    slack_message(data=digitalocean_status())
