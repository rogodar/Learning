import xml.etree.ElementTree as ET 
import urllib.request, urllib.parse, urllib.error
#  http://py4e-data.dr-chuck.net/comments_148682.xml

url = input('Enter location: ')
print('Retrieving ', url)
xms = urllib.request.urlopen(url).read()
print('Retrieved: ', len(xms))
x = 0

tree = ET.fromstring(xms)
lst = tree.findall('.//count')
print('Count: ', len(lst))
for item in lst:
    element = item.text
    x += int(element)
print('Sum: ', x)
