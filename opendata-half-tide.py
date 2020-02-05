import requests
import pandas as pd

# Import for plots
import matplotlib.pyplot as plt

descriptionUrl = 'http://www.tmr.qld.gov.au/~/media/aboutus/corpinfo/Open%20data/nearrealtimedata/Half_Tide_description'

response = requests.get(descriptionUrl)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print(response.text)

readingsUrl = 'http://opendata.tmr.qld.gov.au/Half_Tide.txt'
columnNames = ['Time/Date', 'Water Level in m LAT', 'N/A 1', 'N/A 2', 'N/A 3']
dateparse = lambda x: pd.datetime.strptime(x, '%d%m%Y%H%M')

df = pd.read_csv(readingsUrl, sep="  ", names=columnNames, header=None, skiprows=5, parse_dates=['Time/Date'], date_parser=dateparse, engine='python')
#df['Time/Date'] =  pd.to_datetime(df['Time/Date'], format='%d%m%Y%H%M')

print(df)

# plots
#df.loc[11500:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Minute-level Readings', kind='line')
#df.loc[10500:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Hour-level Readings', kind='line')
#df.loc[:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Day-level Readings', kind='line')
#plt.show()