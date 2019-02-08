buffet = ('pelau', 'chicken stew', 'provision', 'corn pie', 'turkey')
for food in buffet:
   print(food)

# Cannot change values in tuple.   
#buffet[0] = 'fish'
#for food in buffet:
#   print(food)

# If want to change, have to redefine it.
buffet = ('soup', 'salad', 'provision', 'corn pie', 'turkey')
for food in buffet:
    print(food.title())