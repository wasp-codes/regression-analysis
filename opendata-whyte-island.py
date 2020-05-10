import requests
import pandas as pd

from datetime import datetime

# Import for plots
import matplotlib.pyplot as plt

descriptionUrl = 'http://tmr.qld.gov.au/~/media/aboutus/corpinfo/Open%20data/brisbanebartidegaugenearrealtime/Whyte_Island_description.ashx'

# Status check for description
description = requests.get(descriptionUrl)
if description.status_code != 200:
    print('Failed to get description:', description.status_code)
else:
    print(description.text)

readingsUrl = 'http://opendata.tmr.qld.gov.au/Whyte_Island.txt'

# Status check for readings
readings = requests.get(readingsUrl)
if readings.status_code != 200:
    print('Failed to get readings:', readings.status_code)
else:
    columnNames = ['Time/Date', 'Water Level in m LAT', 'N/A 1', 'N/A 2', 'N/A 3']
    df = pd.read_csv(readingsUrl, sep="  ", names=columnNames, header=None, dtype= {'Time/Date': 'str'}, skiprows=5, engine='python')
    df['Time/Date'] = df['Time/Date'].apply(lambda x: datetime.strptime(x, '%d%m%Y%H%M'))

    # plots
    df.loc[11500:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Minutecast', kind='line')
    df.loc[10500:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Hourly', kind='line')
    df.loc[:11520].plot(x='Time/Date', y='Water Level in m LAT', title='Daily', kind='line')

    print(df)
    plt.show()
