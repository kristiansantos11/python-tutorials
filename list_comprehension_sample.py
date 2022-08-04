'''
numbers = []
for x in range(1, 11):
    numbers.append(x**3)
print(numbers)
'''


# List comprehension sample:
# Syntax: variable = [condition iterable]
# iterable can be if statements as well
numbers = []
numbers = [x**3 for x in range(1, 11)]
print(numbers)
