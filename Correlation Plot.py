import matplotlib.pyplot as plt
import pandas as pd


merged_data = pd.read_csv('mergeddata')
print(merged_data.head())
print(merged_data.tail())
fig, ax = plt.subplots()
ax.plot(merged_data['Date'], merged_data['Price_elec_data'],label ='Electricity Price')
ax.plot(merged_data['Date'], merged_data['Price_gas_data'], label='Gas Price')
labels = ['2010','2011','2012','2013','2014','2015','2016','2017', '2018','2019','2020']
plt.xticks(['2010-01-05','2011-01-01','2012-01-01','2013-01-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01', '2018-01-01','2019-01-01','2020-01-01'], labels)
plt.xlabel('Time (Months)')
plt.ylabel('Price (£)')
plt.title('Correlation Analysis')
ax.legend()
plt.legend(loc='upper right')
plt.show()



