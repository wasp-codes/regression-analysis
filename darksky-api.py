import requests
import json
import time

url = 'https://api.darksky.net/forecast/363a3ec44465121cebe6039f0262266b/-27.4698,153.0251'

response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)

dataframe = json.loads(response.text)

#print(dataframe['daily']['data'])
for moonPhase in dataframe['daily']['data']:
    #if '<'time.time()'' in moonPhase['time']:
    if moonPhase['time'] < time.time():
        print (moonPhase['moonPhase'])

#print(dataframe['currently']['summary'])
