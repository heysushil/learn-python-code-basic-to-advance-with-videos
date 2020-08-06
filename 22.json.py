# json: JavaScript Object Notation
'''
facebook => Api (It's url) JSON fromat data => YouTube
'''

import json as j

# creat json format data
jsonData = '{"name":"Neha","course":"Python","platform":"HeySushil"}'

# convert json data into python
getJsonDataIntoPython = j.loads(jsonData)

# get data into python dict
print('Get data: ',getJsonDataIntoPython['name'])

# conver python data into json: dumps
getJsonData = j.dumps(getJsonDataIntoPython)
print('Json data: ',getJsonData)
print('type: ',type(getJsonData))