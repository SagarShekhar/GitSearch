import requests
from github import Github
ACCESS_TOKEN = 'GITHUB_API_KEY'
g= Github(ACCESS_TOKEN)

search=input("Enter search keywords: ")
url = requests.get("https://api.github.com/search/code?q=repo:SagarShekhar/internship+"+search)
var= url.json()
print(len(var))
print(list(var.items())[0])

for i in range(list(var.values())[0]):
    print(var["items"][i]['name'])
    print(var["items"][i]['path'])
    print(var["items"][i]['html_url']+'\n')