import numpy as np

np_height = np.array([1.3, 1.2, 1.7])
np_weight = np.array([65, 63, 45])

bmi = np_weight / np_height ** 2 

# numpy arrays can only contain same type of datatypes

#### 2D NumPy Arrays

np_2d = np.array([[2,4,6,8],
         [1,3,5,7]])

print(np_2d.shape) # analyzing the shape
print(np_2d[0][2]) # accessing a node
print(np_2d[0,2]) # accessing a node but in a fancy way

# if we change one node of matrix into string, whole will be converted to string

print(np_2d[:, 1:3]) # : because we want both the elements, and accessing index 1 and 2 
print(np_2d[1, :]) # acessing all row 1 elements in [a,b] a means row and b means column



#### NumPy Statistics

np_array = np.array([1, 3, 5, 7, 9, 11])

print(np.mean(np_array))   # average
print(np.median(np_array)) # median
print(np.std(np_array))    # standard deviation
print(np.var(np_array))    # variance

print(np.min(np_array))    # smallest value
print(np.max(np_array))    # largest value

print(np.sum(np_array))    # sum of all values
print(np.prod(np_array))   # product of all values

np_2d = np.array([[2,4,6,8],
                  [1,3,5,7]])

print(np.mean(np_2d, axis=0))  # mean of each column
print(np.mean(np_2d, axis=1))  # mean of each row