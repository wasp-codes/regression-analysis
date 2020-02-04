import requests
url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/AUS.csv'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)
# http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/2019/2020/AUS.csv
# http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv
