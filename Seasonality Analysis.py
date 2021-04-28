import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose

# import historical electricity price data set using pandas
elec_data= pd.read_csv('elecdata')
gas_data = pd.read_csv('gasdata.csv')

# converting the Date column data to datetime type
elec_data['Date'] = pd.to_datetime(elec_data['Date'])
gas_data['Date'] = pd.to_datetime(gas_data['Date'])

# analysing the dataframe using .info() and observing the first 5 rows
print(elec_data.head(), elec_data.info())
print(gas_data.head(), gas_data.info())

def decompose_time_series(series):

    result = seasonal_decompose(series, period = 12)
    print(result.trend)
    print(result.seasonal)
    print(result.resid)
    print(result.observed)
    result.plot()
    pyplot.show()

#Set Date as a Pandas DatetimeIndex
elec_data.index=pd.DatetimeIndex(elec_data['Date'])
gas_data.index=pd.DatetimeIndex(gas_data['Date'])

#Decompose the time series into parts
decompose_time_series(elec_data['Price'])
#decompose_time_series(gas_data['Price'])

