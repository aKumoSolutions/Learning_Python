import requests
import pprint
import os

TOKEN = os.getenv("GITHUB_TOKEN")

url = 'https://api.github.com/repos/copypasteninja/python'
headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"}
data = '{"private":true}'


# print(help(requests.patch))
res = requests.patch(url, data, headers=headers)
print(res)