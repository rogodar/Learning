import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 

url = input('Enter adress: ')
print('Processing :', url)

x = 0
code = urllib.request.urlopen(url).read()
print('Retrieved: ', len(code))
tree = ET.fromstring(code)
count = tree.findall('.//name')
print('Number of numbers: ', len(count))

for counts in count:
    element = counts.text
    print(element)
    # x += int(element)
# print(x)