#importing necessary modules
from math import sqrt

# Assigning values
a = 9
b = 8
c = 12
d = 33
e = 5

# calculating the sum of all assigned values
total = a + b + c + d + e
print("Sum =", total)

# Average or mean of the total values
mean = total / 5
print("Average =", mean)

# Population standard deviation calculation
var = ((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2 + (d - mean) ** 2 + (e - mean) ** 2) / 5


# Standard deviation calculation
std_dev = sqrt(var)
print(f"Population Standard Deviation is {std_dev}")
