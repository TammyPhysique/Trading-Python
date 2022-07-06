# Loading and viewing the dataframe

import pandas as pd

infy = pd.read_csv('../data_modules/infy_dv.csv')

infy.head()

# Preparing Data to visualise

infy_close = infy[['Date', 'Close Price']]  # The columns which we require

infy_close.set_index('Date', inplace=True)  # Setting index as date

# More on this in the upcoming section on 'Pandas'

infy_close

import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(infy_close)
plt.show()

import matplotlib.pyplot as plt
%matplotlib inline

# This customizes the size of the plot as per the inputs. Here 14,5 represents the breadth and length of the plot.
plt.figure(figsize=(14, 5))

# This helps in plotting the blue color of the ‘infy_close’ series line graph.
plt.plot(infy_close, 'b')
# plt.plot (infy_close, 'g') # to plot green color

# This helps in plotting the discrete red data points of the closing prices of ‘infy_close’ series.
plt.plot(infy_close, 'ro')
# Here ‘r’ stands for ‘red’ and ‘o’ stands for circles while plotting our discrete data points.
# That is why the points are colored red and the default line color is blue.

# This gives a grid layout to the plot.
plt.grid(True)

# This gives the title to the plot.
plt.title('Infosys Close Price Representation')

# This labels the x-axis
plt.xlabel('Trading Days')

# This labels the y-axis
plt.ylabel('Infosys Close Price')


# To plot and visualise the data
plt.show()

# Preparing data

import pandas as pd

infy2 = pd.read_csv('../data_modules/infy_dv.csv')

#infy2 = pd.read_csv ('C:/Users/academy/Desktop/infy_dv.csv')

infy2 = infy2[['Date', 'Close Price', 'Open Price']]  # Choosing more columns

infy2.set_index('Date', inplace=True)  # Setting 'Date' column as an index

infy2

# PLotting data

plt.figure(figsize=(14, 5))

plt.plot(infy2["Close Price"], lw=1.5, label='Close Price')
plt.plot(infy2["Open Price"], lw=1.5, label='Open Price')

plt.plot(infy2, 'ro')

plt.grid(True)

plt.legend(loc=0)

# This helps us tighten the figure margins
plt.axis('tight')

plt.xlabel('Time')
plt.ylabel('Index')
plt.title('Representative plot with two datasets')

plt.show()

import numpy as np

y = np.random.standard_normal((100, 2))  # Random data created

plt.figure(figsize=(7, 5))

# The function 'scatter' is called to our 'plt' object
plt.scatter(y[:, 0], y[:, 1], marker='o')

plt.grid(True)
plt.xlabel('1st dataset')
plt.ylabel('2nd dataset')
plt.title('Scatter Plot')
plt.show()

# Random data created

np.random.seed(100)
y = np.random.standard_normal(size=1000)

plt.figure(figsize=(10, 5))

# The function 'hist' is called to our 'plt' object
plt.hist(y, label=['Returns Distribution'])

plt.grid(True)
plt.legend(loc=0)
plt.ylabel('Frequency')
plt.xlabel('Returns in Percentage')
plt.title('Histogram')
plt.show()

