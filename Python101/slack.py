import requests, pprint, os

url = os.getenv("SLACK_URL")
headers = {"Content-type": "application/json"}
data = '{"text": "@here \nStarting our session shortly: \nhttps://us02web.zoom.us/j/87909221981?pwd=oAwMENU9aCTvgAAHUScSAQvsYqwGEJ.1 :doge:"}'


# print(help(requests.post))
res = requests.post(url, data, headers=headers)
print(res)

