# import necessary packages
import pandas as pd 
from matplotlib import pyplot as plt 
import datetime 
import requests

# coded for city, could create input for choosing city, message displayed will fetching details
city = 'Louisville'
print("Loading the current forecast for " + city)


# Display the message with report
print('Displaying Weater report for: ' + city)

# pull the weather details from 3rd party (not an API, not sure if it counts but thought it was cool)
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the wttr forecast 
print(res.text)








# Counts the number of days after March 31st 2022, when the csv file becomes outdated. Category 1 
today =  datetime.date.today()
past = datetime.date(2022,3,31)
diff = today - past
print(diff.days, ' days since this graph became outdated')

# reads from external file CSV used in application, and 
# plots visual graph for average temps for March (pandas and matplotlab) 
# *Categories 2 and 3*
df = pd.read_csv('march2022weatherlou.csv')
df.tail()
df.Date.unique()
df.columns
df.dtypes
df['Date'] = pd.to_datetime(df ['Date'])
df.tail()
df.dtypes 
plt.plot(df ['Date'], df ['TempAvgF'])
plt.show()