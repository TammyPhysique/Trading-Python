def my_function(x, n):
    output = x ** n
    return output

my_function(10, 2)  # 10 raise to 2 = 100

my_function(5, 3)  # 5 raise to 3 = 125

def Bollinger_Bands(data, n):

    # Calculating the moving average
    MA = data['Close'].rolling(window=n).mean()

    # Calculating the standard deviation
    SD = data['Close'].rolling(window=n).std()

    data['Lower_BB'] = MA - (2 * SD)  # Lower Bollinger Band
    data['Upper_BB'] = MA + (2 * SD)  # Upper Bollinger Band

    return data

# Load and view Nifty data
import pandas as pd
nifty = pd.read_csv('../data_modules/nifty_data.csv')
nifty.head()

# Calling Bollinger Bands for 'Nifty' index price data

n = 21  # We have kept the window of the moving average as 21 days

# Calling the Bollinger Bands function cerated by us
nifty_bb = Bollinger_Bands(nifty, n)

nifty_bb.tail()

# Plotting the Bollinger Bands for "Nifty' index
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=(10, 5))

plt.plot(nifty_bb.Close)
plt.plot(nifty_bb.Lower_BB)
plt.plot(nifty_bb.Upper_BB)
plt.grid(True)

plt.show()

# Calling Bollinger Bands for 'Infosys' price data

import pandas as pd

# Loading 'Nifty Index' data
infy = pd.read_csv('../data_modules/infy_data_bb.csv')

n = 21  # We have kept the window of the moving average as 21 days

# Calling the Bollinger Bands function cerated by us
infy_bb = Bollinger_Bands(infy, n)

infy_bb.tail()

# Plotting the Bollinger Bands for "Infosys" stock
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=(10, 5))

plt.plot(infy_bb.Close)
plt.plot(infy_bb.Lower_BB)
plt.plot(infy_bb.Upper_BB)
plt.grid(True)

plt.show()

