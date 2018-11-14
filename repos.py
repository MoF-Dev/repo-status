import requests
import json
TOKEN = ""
url = "https://api.github.com/user/repos?access_token={}".format(TOKEN)
r = requests.get(url)
texts = r.text
obj = json.loads(texts)

with open("remote", "w") as f:
    for item in obj:
        f.write(item["name"]+"\n")


