import requests, pprint, random, os, json

pretty = pprint.PrettyPrinter(indent=4)

def cats():
    url = "https://cat-fact.herokuapp.com/facts"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    verified_facts = filter(lambda fact: fact['status']['verified'] == True, response.json())
    facts_list = list(verified_facts)
    randint = random.randint(0, len(facts_list))

    try: 
        return facts_list[randint]['text']
    except IndexError:
        dif_randint = random.randint(0, len(facts_list))
        return facts_list[dif_randint]['text']


def slack(data):
    url = os.getenv("SLACK_URL")
    headers = {"Content-type": "application/json"}
    data = {"text": f"Random Cat Fact: {data}"}

    # print(help(requests.post))
    res = requests.post(url, json.dumps(data), headers=headers)
    print(res)

fact = cats()
slack(data=fact)



