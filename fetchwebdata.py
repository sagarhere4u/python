#fetchwebdata.py

import requests
response = requests.get('https://open.er-api.com/v6/latest/USD')
print(response)

print(response.status_code)

if response:
  print('Request is successful.')
else:
  print('Request returned an error.')

print (response.json())
print (response.json()['rates']['CLP'])
