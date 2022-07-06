# Loading and viewing the dataframe
import pandas as pd
infy = pd.read_csv ('infy_dv.csv', parse_dates = ['Date'])

# Preparing Data to visualise
infy_close = infy [['Date','Close Price']]
infy_close.set_index('Date', inplace=True)

# To plot
import matplotlib 
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.figure(figsize = (14,5))
plt.plot(infy_close,'b')
plt.plot(infy_close,'ro')

# Type your code here 
plt.grid(True)
plt.xlabel ('Trading Days')
plt.ylabel ('Infosys Close Price')
plt.plot(infy_close)
plt.show ()