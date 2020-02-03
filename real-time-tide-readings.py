import requests
url = 'http://opendata.tmr.qld.gov.au/southport.txt'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text[:1000])
