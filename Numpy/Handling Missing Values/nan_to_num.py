import numpy as np

arr = np.array([10, 20, np.nan, 40, np.nan, 60])

cleaned_arr = np.nan_to_num(arr)

print(cleaned_arr)

cleaned_arr = np.nan_to_num(arr, nan=100) #Give a value 100

print(cleaned_arr)