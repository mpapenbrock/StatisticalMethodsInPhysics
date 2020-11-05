###############
# 2D Plotting #
###############

import matplotlib.pyplot as plt

from numpy import pi
from numpy.random import randn

# Generate some data
x_data = randn(1000)
y_data = pi*x_data + randn(1000)

# Generate an empty figure
fig = plt.figure()

# Generate a grid to be filled with plots
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2) # hspace, wspace -> distance between plots

# Define axes and add subplots
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticks=[], yticks=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticks=[], yticks=[])
# x and y ticks are unset for bottom and right histogram

# Plot the main 2D histogram
ax_main.hist2d(x_data, y_data, range=((-3,3),(-10,10)))
ax_main.set_title("histogram with matplotlib")
# range manually defined to ensure the same ranges for histograms

# Add bottom histogram
ax_bottom.hist(x_data, range=(-3,3))
ax_bottom.invert_yaxis()

# Add right histogram
ax_right.hist(y_data, range(-10,10), orientation='horizontal')

plt.show()
