# Use 'Tuple' to make group of elements which can not be changed
# When create a tuple, use brackets '()'.
dimensions = (10, 30)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
   print(dimension)
   
# Cannot change elements in tuple, but can redefine it.
dimensions = (40, 50)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)