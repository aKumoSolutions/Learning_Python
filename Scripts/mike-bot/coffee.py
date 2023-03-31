import requests, os, pprint
p = pprint.PrettyPrinter(indent=4)

everyone = [
    {"name": "Abdul"}
    # {"name": "Abdulmalik"},
    # {"name": "Ahmad Ali"},
    # {"name": "Arman"},
    # {"name": "Aruzhan"},
    # {"name": "Emre Güzeldere"},
    # {"name": "Esenbek Burkanov"},
    # {"name": "Gulnaz Zholshy"},
    # {"name": "Mairamkul Ramazanova"},
    # {"name": "MERDAN KAPLAN"},
    # {"name": "mustafa t"},
    # {"name": "Tugba"},
    # {"name": "Uuviee"},
    # {"name": "Zhyldyz Abdykadyrova"}
]

def slack_message(data):
    url = "secret.com/api"
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % data

    slack_resp = requests.post(url, headers=header, data=data)
    return slack_resp

def random_user(name):
    try:
        random_user = requests.get('https://randomuser.me/api/')
        partner = random_user.json()['results'][0]
        text_data = f"""
*{name}*, you have been randomly chosen a partner from randomuser.me public API page!

Your partner is a {partner['gender']} individual at the age of {partner['dob']['age']}. This individual is from {partner['location']['country']}. 
You may contact this person at {partner['email']} or {partner['cell']}. 

Good luck on your mission :thumbsup:
"""
        return text_data
    
    except:
        print(partner)
        slack_message(data="Something went wrong")


for i in everyone:
    print(slack_message(data=random_user(name=i['name'])))
