# Loading and viewing the data frame
import pandas as pd
infy = pd.read_csv ('infy_dv.csv', parse_dates = ['Date'])

# Preparing data to visualise
infy_close = infy [['Date','Close Price']]
infy_close.set_index('Date', inplace=True)

# To plot
import matplotlib 
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.figure(figsize = (14,5))
plt.plot(infy_close,'b')
plt.plot(infy_close,'ro')
plt.grid(True)
plt.title ('Infosys Close Price Representation')
plt.xlabel ('Trading Days')
plt.ylabel ('Infosys Close Price')

# Type your code here
plt.plot(infy_close)
plt.show()