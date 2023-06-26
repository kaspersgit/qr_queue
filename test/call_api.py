import requests

url = 'http://127.0.0.1:5000/api/call'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)