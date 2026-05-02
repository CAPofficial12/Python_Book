import numpy as np 

## Scalar Arithmetic
array = np.array([1,2,3])
print(array)

# Any operation applied upon an array affects the whole array as individual elements
print(array + 1)

## Excerise: convert an array of radii into areas
radii = np.array([1,2,3])
radii = np.pi * (radii ** 2)
print(radii.round(2)) 

## Element-Wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

# Arithmetic between arrays applies to all ements of that array and they must be homogenous
result = array1 ** array2
print(result)

## Comparisom operator
score = np.array([5,9,4,2,3,6,8,7,5,6,7])

# Logical operators also works on all elements
result = score[score >= 9]
print(result)