import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Array:", arr)

new_arr = np.insert(arr, 1, [20,30,40], axis=0)
print("Modify Array:", new_arr)