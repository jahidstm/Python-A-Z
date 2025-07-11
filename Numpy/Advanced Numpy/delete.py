import numpy as np

arr = np.array([2,3,4,5,6,7])

new_arr1 = np.delete(arr, 4)
new_arr2 = np.delete(arr, 1)
print("Modify Array1: ",new_arr1)
print("Modify Array2: ",new_arr2)