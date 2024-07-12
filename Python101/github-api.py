import requests
import pprint

pretty = pprint.PrettyPrinter(indent=4)

url = f'https://api.github.com/users/copypasteninja/repos'
header = {"Accept": "application/vnd.github+json"}
response = requests.get(url, header)
all_repos = response.json()

print(len(all_repos))

# for repo in all_repos:
#     print("clone url:", repo['clone_url'])
#     print("private: ", repo['private'])
#     print("Username: ", repo['owner']['login'])
