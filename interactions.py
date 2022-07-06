# Import pandas
import pandas as pd

# Read data
df = pd.read_csv('../data_modules/candlestick_data.csv', index_col=0)
df.head()

# Importing the necessary packages
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file

# Indexing
import pandas as pd
w = 12*60*60*1000  # half day in ms
df.index = pd.to_datetime(df.index)

inc = df.Close > df.Open
dec = df.Open > df.Close

# The various 'interactions' we want in our candlestick graph. This is an argument to be passed in figure () from bokeh.plotting
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

# Pan: It helps you pan/move the plot

# Wheel Zoom: You can zoom in using the wheel of your mouse

# Box Zoom: You can zoom in by creating a box on the specific area of the plot. Use the mouse, click and drag to create the box

# The various 'interactions' we want in our candlestick graph. This is an argument to be passed in figure () from bokeh.plotting
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

# Pan: It helps you pan/move the plot

# Wheel Zoom: You can zoom in using the wheel of your mouse

# Box Zoom: You can zoom in by creating a box on the specific area of the plot. Use the mouse, click and drag to create the box

# Reset: If you want to reset the visualisation of the plot

# Save: Saving the plot (entire or the part which you want) as an image file

# Passing the arguments of our bokeh plot
p = figure(x_axis_type="datetime", tools=TOOLS,
           plot_width=1000, title="SPY Candlestick")



# Reset: If you want to reset the visualisation of the plot

# Save: Saving the plot (entire or the part which you want) as an image file

from math import pi

# The orientation of major tick labels can be controlled with the major_label_orientation property.
# This property accepts the values "horizontal" or "vertical" or a floating point number that gives
# the angle (in radians) to rotate from the horizontal.
p.xaxis.major_label_orientation = pi/4


# Alpha signifies the floating point between 0 (transparent) and 1 (opaque).
# The line specifies the alpha for the grid lines in the plot.
p.grid.grid_line_alpha = 0.3

# Configure and add segment glyphs to the figure
p.segment(df.index, df.High, df.index, df.Low, color="red")

# Adds vbar glyphs to the Figure
p.vbar(df.index[inc], w, df.Open[inc], df.Close[inc],
       fill_color="#1ED837", line_color="black")
p.vbar(df.index[dec], w, df.Open[dec], df.Close[dec],
       fill_color="#F2583E", line_color="black")

# Generates simple standalone HTML documents for Bokeh visualization
output_file("candlestick.html", title="candlestick.py example")

# The graph will open in another tab of the browser

show(p)

# The code ends here

# This is more of a 'helping' code that will help us to visualise the candlestick plot on our 'Quantra' portal

# Please run this twice or thrice if it gives an error in the first run
from IPython.display import HTML
HTML("./candlestick.html")

