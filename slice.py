# Use 'slice' to require the first three elements. 
names = ['charls', 'austin', 'louise', 'thomas', 'may']
print(names[0:3])

# If don't place a number, Python will default to start/end for [:].
print(names[2:])

# If the list is long and want to take the last three elements,
# can use [-3:]. 
print(names[-3:]) 

# Also can use 'for...in...' to request list.
print('\nThree of my colleagues are:')
for name in names[:3]:
   print(name.title())