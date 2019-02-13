import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

params = {"address": address}
url = serviceurl + urllib.parse.urlencode(params)
print('Retrieving ', url)

fh = urllib.request.urlopen(url)
data = fh.read().decode()
print('Retrieved ', len(data), 'characters')
js = json.loads(data)
print('Place id', js['results'][0]['place_id'])