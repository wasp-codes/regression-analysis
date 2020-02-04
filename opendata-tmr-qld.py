import requests
import pandas as pd

# import for graph
import matplotlib.pyplot as plt

url = 'http://opendata.tmr.qld.gov.au/southport.txt'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text[:30])

df = pd.read_csv('http://opendata.tmr.qld.gov.au/southport.txt', sep=" ", header=None, skiprows=18, engine='python')
df = df.loc[:,[0,2]]
df = df.dropna()
df.columns = ['Time/Date','Water Level in m LAT']
print(df)

# graph
df.plot(x = 'Time/Date', y = 'Water Level in m LAT', kind = 'scatter')
plt.show()