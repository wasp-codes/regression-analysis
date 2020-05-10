import requests
import json

url = 'http://newsapi.org/v2/top-headlines?&sources=bbc-news&&apiKey=486ad551576442e788d9d3e7672919b0'

response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    dataframe = json.loads(response.text)

#print(dataframe['daily']['data'])
#for moonPhase in dataframe['daily']['data']:
    #if '<'time.time()'' in moonPhase['time']:
    #if moonPhase['time'] < time.time():
        #print (moonPhase['moonPhase'])

#print(dataframe['results'])

for extractValue in dataframe['results']:
    print(extractValue['title'])
    print(extractValue['abstract'])
    print('\n')

