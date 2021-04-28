import matplotlib.pyplot as plt
import pandas as pd

#import previously saved gas data
gas_data = pd.read_csv('gasdata.csv')
print(gas_data.head().info())

# plot data using matplotlib setting titles and color
gas_data.plot('Date','Price', title ='Monthly Gas Prices (£/MW)', color = 'orange')
plt.xlabel('Time (Months)')
plt.ylabel('Price (£)')
plt.show()



