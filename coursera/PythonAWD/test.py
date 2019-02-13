import json
json = json.loads(open('C:\Learning\Learning\coursera\PythonAWD\\test.json').read())
for item in json:
    print('Name: ', item['name'])
    print('Id: ', item['position'])
    print('*'*20)