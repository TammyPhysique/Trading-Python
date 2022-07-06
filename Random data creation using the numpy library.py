# Random data creation using the numpy library

import numpy as np

strike_price = np.linspace(50, 150, 25)  # Strike values between 100 to 150
time = np.linspace(0.5, 2, 25)  # Time to maturity between 0.5 to 2.5 years

# The numpy's meshgrid() function helps us to create a rectangular grid out of an array of x values and y values

strike_price, time = np.meshgrid(strike_price, time)

strike_price, time[:]  # Printing the mesh grid array

# generate fake implied volatilities

implied_volatility = (strike_price - 100) ** 2 / (100 * strike_price) / time

# Plotting a 3D figure

import matplotlib.pyplot as plt

# Importing the required packages for 3D plotting
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))

# If 'fig' is a variable holding a figure, fig.gca() returns the axes associated with the figure.
# With this 3 dimensional axes is enabled
axis = fig.gca(projection='3d')

# To plot the surface and passing the required arguments
surface = axis.plot_surface(strike_price, time, implied_volatility, rstride=1,
                            cstride=1, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=False)

axis.set_xlabel('strike')
axis.set_ylabel('time-to-maturity')
axis.set_zlabel('implied volatility')

# Adding a colorbar which maps values to colors
fig.colorbar(surface, shrink=0.5, aspect=5)

plt.show()