import numpy as np
array = np.array("A")

#Returns number of dimensions in the array
print(array.ndim)
print(array.shape)

array1 = np.array(["A", "B","C"])
print(array1.ndim)
print(array1.shape)

array2 = np.array(  [["A", "B","C"], 
                    ["D","E","F"]])
print(array2.ndim)

#Returns Dimensions of the Array (3,3)
print(array2.shape)

# Arrays/Matrices require a homogenous shape. Error will occur if array is heterogenous
main_array = np.array( [[["A", "B","C"], ["D","E","F"], ["G","H","I"]],
                        [["J", "K","L"], ["M","N","O"], ["P","Q","R"]],
                        [["S", "T","U"], ["V","W","X"], ["Y","Z", " "]]])
print(main_array.ndim)
print(main_array.shape)

# Exercise 1: Make the word dog from multidimensional indexing
word = main_array[0,1,0] + main_array[1,1,2] + main_array[0,2,0]
print(word)