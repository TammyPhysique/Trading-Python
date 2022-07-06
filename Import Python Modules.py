import math

import warnings
warnings.filterwarnings('ignore')

# The value of Pi
math.pi 

# The cosine value of 1
math.cos(1) 

# The sine value of 1
math.sin(1)

dir(math)

# We will import only the 'mean' object from the 'scipy' package
from scipy import mean

# This will give arithmetic mean of the numbers
mean([1, 2, 3, 4, 5])  

from scipy import stats

stats.hmean([1, 2, 3, 4, 5])

from numpy import *

sin(1)

diag([1, 5, 9, 6])

import numpy as np

dir(np)

# Will return the median of the number set
np.median([4, 5, 6, 3, 4, 5, 9, 8, 7, 12])

# Will return the minimum number of the number set
np.min([4, 5, 6, 3, 4, 5, 9, 8, 7, 12])

# Will return the maximum number of the number set
np.max([4, 5, 6, 3, 4, 5, 9, 8, 7, 12])

