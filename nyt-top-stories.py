import requests
import json

url = 'https://api.nytimes.com/svc/topstories/v2/world.json?api-key=tPvfWWnLYnfZsYXS1AL9sQq0zzqz25wg'

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
    print("Abstract:", extractValue['abstract'])
    print('\n')