groceryPrices = [200, 120, 10, 25, 110, 15, 75, 150]

total_price = 0
# for index in range(len(groceryPrices)):
#     total_price = total_price + groceryPrices[index]
#     print('Current price:', groceryPrices[index])

# print('Total Price ', total_price)

# or

for itemPrice in groceryPrices:
    total_price = total_price + itemPrice
    print(itemPrice)

print('Total Price ', total_price)
