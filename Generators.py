##############
# Generators #
##############

# Write a function that doubles a number
def double_numbers(iterable):
  for i in iterable:
    yield i + i

for i in double_numbers(range(1, 900000000)):
  print(i)
  if i >= 30:
    break



# Use generator to create a truncated gaussian
import numpy as np
import matplotlib.pyplot as plt


# Let's randomise the random seed
np.random.seed()


def truncated_gaussian(mean, sigma, N=10000, width=1):
  i = 0
  while i < N:
    rand = np.random.normal(mean, sigma)
    i += 1
    if abs(rand - mean) < width:
      yield rand


# Fill the actual distribution
distribution = []
for number in truncated_gaussian(1, 0.5, width=0.5):
  distribution.append(number)


# Plot the result
bins = 30
plt.hist(distribution, bins)
plt.xlim(-1, 3)
plt.show()