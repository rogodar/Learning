# In this assignment you will write a Python program somewhat similar to http: // www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json
# Actual data: http://py4e-data.dr-chuck.net/comments_148683.json(Sum ends with 39)

import json
import urllib.parse, urllib.request, urllib.error

url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved: ', len(data))
info = json.loads(data)

num = 0
count = 0
for item in info['comments']:
    num += item['count']
    count += 1
print('Count: ', count)
print('Sum: ', num)
