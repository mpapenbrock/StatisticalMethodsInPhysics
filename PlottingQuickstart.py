############
# Plotting #
############

# Documentation: https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html


# Import modules
import matplotlib.pyplot as plt     # for plotting
import numpy as np                  # for preparing some data to plot


# Generate 50 points between 0 and 2pi
x = np.linspace(0, 2*np.pi, 50)
print(x)


# Calculate the sine for these values
sine = np.sin(x)
print(sine)


# Plot the graph

# Create a canvas (fig) and an axes object (ax)
fig, ax = plt.subplots(1, figsize = (8,6))
# Plot the result
ax.plot(x, sine)
# Show the plot
plt.show()


# Let's do this properly
fig, ax = plt.subplots(1, figsize = (8,6))
ax.plot(x, sine, label='$\sin(x)$')

ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
plt.legend() # Will take the label to generate a legend
plt.show()


# Make this a little fancy

plt.style.use('seaborn-poster')  # Makes some changes to line-width, label-size and tics

x = np.linspace(0, 2*np.pi, 50)

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (8,4))
ax1.plot(x, np.sin(x), label="$\sin(x)$")
ax2.plot(x, np.cos(x), c='orange', label="$\cos(x)$")

ax1.set_xlabel("$x$")
ax2.set_xlabel("$x$")

ax1.set_ylabel("$f(x)$")
ax2.set_ylabel("$f^{\prime}(x)$")

ax1.legend()
ax2.legend()

plt.tight_layout() # important function for correct margins and spacing

plt.savefig("sineAndCosine.png", dpi=200)
plt.show()