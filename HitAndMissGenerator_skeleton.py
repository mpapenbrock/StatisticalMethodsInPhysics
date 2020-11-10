# Import the modules that you need
# Tip: You will have to generate random numbers and plot the final results


# Set a seed for the random number generator (or randomise it itself)


# Here are some parameters needed for the event generator
# Adjust them as you like
N = 1000 # number of events to be generated
alpha = -0.2 # a parameter for the event generator (see exercise 1.3)
bins = 100 # number of bins for the histogram


# Implement a function for the hit/miss criterion (filtering the cos(theta) distribution)
# The desired angular distribution is W(cos(theta)) = 1 + alpha * cos(theta)**2
# Tip: You should normalise this distribution with 1 + abs(alpha)
# Tip: The cos(theta) distribution should go from -1 to 1
# Tip: Some good input parameters for your function would be N and alpha
# Tip: You will need a second random number to check the criterion, e.g. "random_number2 < something"
# Tip: Python's generator function ("yield") could be used here


# Use your implemented function to generate a new cos(theta) distribution
# with N entries


# Plot the distribution
