import pprint, requests
from github_status import github_status
from slack_status import slack_status
from digital_ocean_status import digitalocean_status
pp = pprint.PrettyPrinter(indent=4)

# curl -X POST -H 'Content-type: application/json'
#     --data '{"text":"This is just the start! Lets have fun!"}' 
# https://hooks.slack.com/services/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

def slack_message(data):
    url = 'secretURL.com'
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % data

    slack_resp = requests.post(url, headers=header, data=data)
    print(slack_resp)
    return slack_resp

slack_message(data=github_status())
slack_message(data=slack_status())
slack_message(data=digitalocean_status())
