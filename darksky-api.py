import requests
import pandas

from pandas.io.json import json_normalize

url = 'https://api.darksky.net/forecast/363a3ec44465121cebe6039f0262266b/-27.4698,153.0251'

response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)
