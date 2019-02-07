# Use 'list()' to make a list for range.
# Use 'min()' -> smallest, 'max()' -> largest, 
# and 'sum()' -> summation to require different demonds.
num = list(range(1, 1000001))
print(min(num))
print(max(num))
print(sum(num))
# Make a list of odd numbers, and give a range.
num2 = []
for x in range(1, 21, 2):
    num2.append(x)
print(num2)
# Make a list of numbers which are divisible to 3.
num3 = []
for y in range(3, 31, 3):
    num3.append(y)
print(num3)
# Make a list of cube numbers from 1 to 10.
num4 = []
for z in range(1, 11):
    num4.append(z**3)
print(num4)
# Same purpose as above but with brief code.
num5 = [a**3 for a in range(1, 11)]
print(num5)