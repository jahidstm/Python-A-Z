import numpy as np

arr_2d = np.array([[2,3,4],[5,6,7]])

new_arr1 = np.delete(arr_2d, 1, axis=0)
print("Modify Array1: ",new_arr1)

new_arr1 = np.delete(arr_2d, 0, axis=1)
print("Modify Array2: \n",new_arr1)