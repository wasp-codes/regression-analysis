import requests
import json

query = input("Your query:")

appid = '76R8AJ-A36T6HJWVT'

url = 'http://api.wolframalpha.com/v1/result?appid=' + appid + '&i=' + query

response = requests.get(url)

if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)
    