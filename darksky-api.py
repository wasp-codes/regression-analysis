import requests
import pandas as pd
import json

url = 'https://api.darksky.net/forecast/363a3ec44465121cebe6039f0262266b/-27.4698,153.0251'

response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)

dataframe = pd.read_json(response.text)

dataframe = dataframe.astype(str)

print(dataframe)

readValue = json.loads(response.text)
#print(readValue['currently'])
for read in readValue:
    print(read['timezone'])
