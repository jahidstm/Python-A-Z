import numpy as np

prices = np.array([10, 20, 30, 40, 60,65])

discount = 20 #20% discount
final_price = []

for price in prices:
    dis_price = price * (1 - (discount/100))
    final_price.append(int(dis_price))

print(final_price)