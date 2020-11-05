#################
# Python Basics #
#################

"""
General things about Python
---------------------------

Some properties distinguish Python from other languages:

* Python is case sensitive
* Python uses indentation for blocks in contrast to { } in C, for example, and does not require a special end of line symbol
* Python is interpreted, not compiled
* Python has a complex type system, but it lets you get away with not caring about it
* Python uses many libraries and they are typically easy to use and fast
* Python has a garbage collection, so created objects are cleaned up automatically
* Python is 0-indexed (counting of elements starts with the 0th element)
* Python uses True and False
* Linebreaks are marked with \ or by simply not closing a parenthesis or bracket for multiple lines
* Multiple statements in one line are separated by ;
""" 

#####################################
# Primitive Datatypes and Operators #
#####################################

# this is a single line comment

""" this is a multi-line comment
    note how it starts with
    three "s
"""

t = type(3) # this is an integer
print(t)

t = type(4.2) # this is a floating point number
print(t)

t = type(3.1j) # this is a complex number
print(t)


# Simple math operations are straightforward
print(1+3)
print(7.5-1.5)
print(5*2j)

# More complicated operations
print(7%3) # modulo
print(2**4) # exponentiation
print((1+4)*5) # parenthesis


# Boolean operators (case sensitive!)
print(True and False)
print(False or True)
print(not True)
print(not False)


# Equalities
print(1 == 1)
print(2 == 1)


# Inequalities
print(1 != 1)
print(2 != 1)


# Greater/smaller than or equal
print(1 < 10)
print(1 > 10)
print(2 <= 2)
print(2 >= 2)


# Chains work as well
print(1 < 2 < 3)
print(2 < 3 < 2)


# Ternary operator. Python uses if and else instead of ?: in C/C++
print("Yahoo!") if 3 > 2 else 2


# Strings are created with " or '
print("This is a string.")
print('This is one as well.')


# Triple symbols allow for multi-line strings
print("""This is a long string ...
it goes on and on ...
and then it stops.""")


# Combining strings
print("Nice " + "weather.")
print("Two " "numbers.")


# String multiplication
print("Hello"*3)


# Formatting strings with .format()
print("{} is a {}.".format("This","placeholder"))
print("{0} can be {2} {1}".format("Strings","nicely","formatted"))
print("{name} wants to eat {food}.".format(name="Alice", food="noodles"))


#############################
# Variables and Collections #
#############################

# Variables

""" 
Python has no command for declaring a variable. A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type and can even change type after they have been set.
"""

some_var = 5
some_var = "Bob"
#some_other_var # this gives an error

# Almost any variable name can be used, except: and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

# Specify a field that is not (yet) created
third_var = None

# User input
#input_var = input("Enter something: ")
#print(input_var)


#########
# Lists #
#########

# Declaration
li = [] # empty list
other_li = [4, 5, 6] # prefilled

print(li)
print(other_li)


# Appending lists
li.append(1)
li.append(3)
li.append(9)
print(li)


# Remove last element
li.pop()
print(li)


# Access any element
print(li[0])


# Or modify it
li[0] = 42
print(li)


# Look at last element
print(li[-1])


# Or one before that
print(li[-2])


# Out of bound error
# li[3]


# Can combine lists
new_li = li + other_li
print(new_li)


# Or extend them
li.extend(other_li)
print("extended: ",li)


# Check of existence in a list
print(3 in li)


# Look at ranges with slice syntax
print(li[1:3])

# syntax for slices is [beginning : end : step]

# omit beginning
print(li[2:])


# or the end
print(li[:3])


# every second entry
print(li[::2])


# list in reverse
print(li[::-1])


# delete items
print(li)
del li[3]
print(li)


# or remove occurrences of specific items
li.remove(3)
print(li)


# insertion (where, what)
li.insert(1,3)
print(li)


################
# Control flow #
################

# Make a variable
some_var = 5


# if statements
if some_var > 10:
  print("some_var is totally bigger than 10.")
elif some_var < 10:  # elif clause is optional
  print("some_var is smaller than 10.")
else:  # also optional
  print("some_var is indeed 10.")


# for loops can iterate over lists
for animal in ["dog", "cat", "mouse"]:
  print("{} is a mammal.".format(animal))


# ordered bunch of numbers
for i in range(4):
  print(i)

for i in range(4, 8):
  print(i)

for i in range(4, 8, 2):
  print(i)


# while loops
x = 0
while x < 4:
  print(x)
  x += 1 # Shorthand for x = x + 1


# loops can be skipped or interrupted 
for i in range(1000):
  if i % 2 == 0:
    continue
  
  print(i)

  if i > 10:
    break


# Fancy list comprehensions
square_numbers = [i**2 for i in range(10)]
print(square_numbers)


#############
# Functions #
#############


# Use def to create a new function
def add(x, y):
  print("x is {} and y is {}".format(x, y))
  return x + y # Return values with a return statement

print(add(5, 6))


# Default values for arguments
def subtract(x, y=1):
  print("x is {} and y is {}".format(x, y))
  return x - y

print(subtract(3))


# Return multiple values
def swap(x, y):
  return y, x

x = 1
y = 2
x, y = swap(x, y)

print("x = ", x)
print("y = ", y)


# Functions can be passed as argument to other functions
def double(x):
  return 2*x

def repeated_evaluation(f,x,n):
  for i in range(n):
    x = f(x)

  return x

print(repeated_evaluation(double, 1, 10))


########################
# Modules and Packages #
########################


# Importing modules
import math
print(math.sqrt(16))


# Can also import specific functions from a module
from math import ceil, floor
print(ceil(3.7))
print(floor(3.7))


# Shorten module names
import math as m
print(math.sqrt(16) == m.sqrt(16))


# Get help
#help(math)


# Or more specifically
help(math.exp)


#############################
# Writing and reading files #
#############################


# Writing
with open("test.txt", 'w', encoding = 'utf-8') as file:
  file.write("my first file\n")
  file.write("This file\n")
  file.write("contains three lines\n")


# Reading
file = open("test.txt", 'r', encoding = 'utf-8')
print(file.read(4))  # first 4 data
print(file.read(4))  # next 4 data

print(file.read()) # rest of the file

file.seek(0) # go to desired position
print(file.readline()) # read the first line

print(file.readlines()) # read in line by line