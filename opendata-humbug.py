import requests
import pandas as pd

# import for graph
import matplotlib.pyplot as plt

url = 'http://opendata.tmr.qld.gov.au/Humbug_Wharf.txt'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text[:28])

df = pd.read_csv('http://opendata.tmr.qld.gov.au/Humbug_Wharf.txt', sep=" ", header=None, skiprows=5, engine='python')
df = df.loc[10500:11520,[0,2]]
df = df.dropna()
df.columns = ['Time/Date','Water Level in m LAT']
df['Time/Date'] =  pd.to_datetime(df['Time/Date'], format='%d%m%Y%H%M')
print(df)

# graph
df.plot(x = 'Time/Date', y = 'Water Level in m LAT', kind = 'line')
plt.show()