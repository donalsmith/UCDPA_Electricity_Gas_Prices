import matplotlib.pyplot as plt
import pandas as pd

#import previously saved electricity data
elec_data = pd.read_csv('elecdata')
print(elec_data.head().info())

# plot data using matplotlib setting titles and color
elec_data.plot('Date','Price', title ='Monthly Electricity Prices (£/MW)', color = 'b')
plt.xlabel('Time (Months)')
plt.ylabel('Price (£)')
plt.show()


