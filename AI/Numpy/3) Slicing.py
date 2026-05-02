import numpy as np

array= np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# Numpy arrays work similarly to python strings for subscripts but doesnt return errors when out of bounds
rows = array[::-3]

# Adding ,x converts the number to columns
columns = array[:,::-1]

# Rturning quadrants is y,x ranges
matrix = array[2:, 2:4]

print(rows, '\n')
print(columns, '\n')
print(matrix)