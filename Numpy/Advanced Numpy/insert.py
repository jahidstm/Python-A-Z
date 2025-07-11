import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

new_arr = np.insert(arr, 2, 25)
print("Modify Array:", new_arr)