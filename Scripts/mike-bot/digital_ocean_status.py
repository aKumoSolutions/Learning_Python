import requests, pprint

pp = pprint.PrettyPrinter(indent=4)


def digitalocean_status():
    ##requests.get(url, header, data)
    do_url = 'https://status.digitalocean.com/api/v2/status.json'
    do_resp = requests.get(do_url)
    status_data = do_resp.json()

    if status_data['status']['indicator'] == 'none':
        result = f"*Digital Ocean Status*: {status_data['status']['description']} & *Indicator*: {status_data['status']['indicator']} *Last Updated*: {status_data['page']['updated_at']} :doge:" 
    else:
        result = f"*Digital Ocean Status*: {status_data['status']['description']} & *Indicator*: {status_data['status']['indicator']} *Last Updated*: {status_data['page']['updated_at']} :facepalm:"
    
    return result
