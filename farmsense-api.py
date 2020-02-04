import time
import requests
import json

unixTimeStampStr = str(int(time.time()))

url = 'http://api.farmsense.net/v1/moonphases/?d=' + unixTimeStampStr
response = requests.get(url)

"""
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)
"""

readValue = json.loads(response.text)
for read in readValue:
    print(read['Phase'])
