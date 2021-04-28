# Start by importing the csv datasets. The first dataset is time series of historical UK Wholesale Electricity Prices. The
# second is a time series of hstorcal UK Natural Gas futures cnotracts prices.

# import necessary packages
from typing import Any, Union
import pandas as pd
import statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from matplotlib import pyplot
from numpy import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray


#**************************************************************

# import electricity price data set using pandas
elec_data= pd.read_csv('Monthly_elec_Prices.csv')

# converting the Date column data to datetime type
elec_data['Date'] = pd.to_datetime(elec_data['Date'])

# analysing the dataframe using .info() and observing the first 5 rows
print(elec_data.head(), elec_data.info())


# See Elec Data Plot script for plot - saving the dataframe to csv format
elec_data.to_csv("elecdata")

#**************************************************************

#def decompose_time_series(series):

    #result = seasonal_decompose(series, model='additive', period=12)
    #result.plot()
    #pyplot.show()

#Set Date as a Pandas DatetimeIndex
#elec_data.index=pd.DatetimeIndex(elec_data['Date'])
#Decompose the time series into parts
#decompose_time_series(elec_data['Price'])


#Execute in the main block

#Convert the Date column into a date object

#**********************************************************

# import historical gas price data set using pandas
gas_data= pd.read_csv('Monthly_gas_Prices.csv')

# converting the Date column data to datetime type
gas_data['Date'] = pd.to_datetime(gas_data['Date'])

# analysing the dataframe using .info(),.head() and.columns
#print('Gas Data Info', gas_data.head(), gas_data.info())
#print(gas_data.columns)

# sorting the gas data for columns
gas_sorted= gas_data[['Date','Price']]
print('Gas Sorted',gas_sorted.head())

# Saving the sorted gas data in csv format
gas_data.to_csv("gasdata.csv")

#*********************************************************

# checking for missing values and finding the sum
print('Elec Null', elec_data.isnull().sum())
print('Gas Null', gas_data.isnull().sum())

# dropping missing values
gas_data = gas_data.dropna()
print('Gas drop',gas_data.isnull().sum())

print(gas_sorted.duplicated().sum())
print(gas_sorted.isnull().sum())

# merge elec data with gas data using .merge_ordered and suffixes
merged_data = pd.merge_ordered(elec_data, gas_sorted, on ='Date', suffixes= ('_elec_data', '_gas_data'))
print(merged_data.head())

# checking for missing values due to the different time spans of the datasets
print(merged_data.isnull().sum())

# dropping rows of merged dataset which contain missing values
merged_data= merged_data.dropna()
print(merged_data.head())



# grouping by sorting the merged dataset for the Ptice columns for both variables using a list within the call function
price_columns = merged_data[['Price_elec_data','Price_gas_data']]
# testing correlation of the variables to help determine relationship
print('Corr Matrix', price_columns.corr())

merged_data = merged_data[['Date', 'Price_elec_data', 'Price_gas_data']]
#Saving dataframe to a csv
merged_data.to_csv("mergeddata")

# checking for duplicate value to see if there is a need to drop (no duplicates upon inspection)
print('Number of Duplicate Data Points:', merged_data.duplicated().sum())

#*****************************************************************************
#convert price column in dataframe to a list containing all of the prices to find the max price and min price for both electricity and gas in during the time period

# Converting Electricity price dataframe into a numpy array using .to_numpy()
elec_numpy_array = elec_data.to_numpy()

# Creating a List of all of the electricity pricesby extracting from the numpy array
# using numbers argument to call all rows of the second column
elec_price_list = elec_numpy_array[:,1]
print('List of Electricity Prices',elec_price_list)

# In order to find the max and min price that electricity traded for during the time period - created
# a for/if loop, this iterates through all of the values in the list and provides the max and min price
max_value = None
for num in elec_price_list:
    if (max_value is None or num > max_value):
        max_value = num

print('Maximum Price of Electricity:', max_value)

min_value = None
for num in elec_price_list:
    if (min_value is None or num < min_value):
        min_value = num

print('Minimum Price of Electricity:', min_value)
#******

# Converting Gas price dataframe into a numpy array using .to_numpy()
gas_numpy_array = gas_sorted.to_numpy()


# Creating a List of all of the recorded gas prices during the period by extracting from the numpy array
# using numbers argument to call all rows of the second column from row 159 to the last row. This was done to
# to sort the array/list so that  the time period matches that of the electricity data. (2010-01-05 onwards)
gas_price_list = gas_numpy_array[160:,1]
print('List of Gas Prices',gas_price_list)

# In order to find the max and min price that gas traded for during the time period - created
# a for/if loop, this iterates through all of the values in the list and provides the max and min price
max_value = None
for num in gas_price_list:
    if (max_value is None or num > max_value):
        max_value = num

print('Maximum Price of Gas:', max_value)

min_value = None
for num in gas_price_list:
    if (min_value is None or num < min_value):
        min_value = num

print('Minimum Price of Gas:', min_value)

#elec_numpy_array = elec_data.to_numpy()
#print(elec_numpy_array)
#elec_price_listA = elec_numpy[:,1]
#print('List of Electricity Prices',elec_price_listA)


#ax_price = None
#for x in column_list:
   # if x > max_price: max_price = x



#column_test = elec_data['Price']

#or max in
    #column_test = elec_data['Price']
   # max_price_elec = column_test.max()

#print(max_price_elec)


#min_price_elec = column_test.min()
#print(min_price_elec)




#merged_data.plot()
#plt.show()


## **************************************
#gas_new = gas_sorted['2010-01-01':'2015-01-01']
#print(gas_new.head().info())

# sorting the gas data from 2010 onwards to 2020
#sliced_gas_data = gas_sorted['2010':]
#print(sliced_gas_data.info())
