import pprint, requests
pp = pprint.PrettyPrinter(indent=4)
from nasa_api import nasa_api

import requests, pprint
pp = pprint.PrettyPrinter(indent=4)

def nasa_api():
    nasa_api = 'https://api.nasa.gov/planetary/apod?api_key=akCp6ZdvEyxc5XlvZc9dQkpj7LonITXKR2IteJvE'
    nasa_resp = requests.get(nasa_api).json()
    info = f"""*Todays Nasa Picture Brought to you by Uuviee:* :milky_way: {nasa_resp['date']},
    *Explanation*: {nasa_resp['explanation']}, 
    *Click here to view image*: {nasa_resp['url']}"""
    return info

pp.pprint(nasa_api())


def mike_bot(info):  
    url = 'https://hooks.slack.com/services/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'
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % info

    nasa_api = requests.post(url, headers=header, data=data)
    print(nasa_api)
    return nasa_api

mike_bot(info=nasa_api())