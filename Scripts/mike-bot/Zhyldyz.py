import requests, pprint

pp = pprint.PrettyPrinter(indent=4)

cat_facts_address = 'https://catfact.ninja/fact'
github_status = requests.get(cat_facts_address)
status_r = github_status.json()
cats_fact_msg = status_r['fact']


def slack_message(data):
    url = 'https://hooks.slack.com/services/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'
    header = {"Content-type": "application/json"}
    data = '{"text": "%s" }' % data

    slack_resp = requests.post(url, headers=header, data=data)
    pp.pprint(slack_resp)
    print(slack_resp)
    return slack_resp

slack_message(f"Zhyldyz's fact about cats: {cats_fact_msg}")