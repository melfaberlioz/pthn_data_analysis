import matplotlib.pyplot as plt

# data for x and y axes
x_axis = [1, 2, 3, 4, 5, 6]
y_axis = [5, 16, 34, 56, 32, 76]

# with the title function, we set a title for the chart
plt.title('Price over 6 years')
# the 'scatter' function draws the scatter chart. It accepts the
# data for the x and y axes, the color of the marker, the shape of the
# marker, and the label.
plt.scatter(x_axis, y_axis, color='darkblue', marker='x', label='item 1')

# set the labels for the axes
plt.xlabel('Time (years)')
plt.ylabel("Price (dollars)")

# show the grid with the 'grid' function.
# The grid consists of a number of vertical and horizontal
# lines.
plt.grid(True)
# the "legend" function places a legend on the axes.
plt.legend()

# displays the chart
plt.show()
