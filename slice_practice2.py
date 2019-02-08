my_pizzas = ['hawaii', 'american', 'cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('beef')
friend_pizzas.append('corn')

print('My pizzas are:')
print(my_pizzas)

# When use a list valuation to print, result indicates by list.
# When use an assigned valuation to print, result indicates by elements. 
print("\nMy friend's pizzas are:")
print(friend_pizzas)
for pizza2 in friend_pizzas:
   print(pizza2.title())
