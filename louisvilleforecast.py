import pandas as pd 
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt 

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
new_column.dropna(inpace=True)
new_column.columns = ['ds', 'y']
new_column.tail()

n= NeuralProphet()
model = n.fit(new_column, freq='D', epochs=5000)

future = n.make_future_dataframe(new_column, periods=1500)
forecast = n.predict(future)
forecast.tail()

plot = n.plot(forecast) 