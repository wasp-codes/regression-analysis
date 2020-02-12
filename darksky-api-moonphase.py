import requests
import json
import time

url = 'https://api.darksky.net/forecast/363a3ec44465121cebe6039f0262266b/-27.4698,153.0251'

response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    dataframe = json.loads(response.text)
    
for extractValue in dataframe['daily']['data']:
    if extractValue['time'] < time.time():
        print(extractValue['moonPhase'])
