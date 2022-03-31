import pandas as pd 
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt 
import datetime 

today =  datetime.date.today()
future = datetime.date(2025,4,1)
diff = future - today
print(diff.days, 'number of future forecast dates')

df = pd.read_csv('louisville_weather.csv')
df.tail()
df.Date.unique()
df.columns
df.dtypes
df['Date'] = pd.to_datetime(df ['Date'])
df.tail()
df.dtypes 
plt.plot(df ['Date'], df ['TempAvgF'])
plt.show()

new_column = df[['Date','TempAvgF']]
new_column.dropna(inplace=True)
new_column.columns = ['ds', 'y']
new_column.tail()

model= NeuralProphet()
metrics = model.fit(new_column, freq='D')


future = model.make_future_dataframe(new_column, periods=1500)
forecast = model.predict(future)
forecast.tail()

plot = model.plot(forecast) 

plt.plot(forecast)