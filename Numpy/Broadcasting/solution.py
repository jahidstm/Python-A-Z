import numpy as np

prices = np.array([10, 20, 30, 40, 60,65])

discount = 20 #20% discount
dis_price = prices * (1 - (discount/100))

print(dis_price)