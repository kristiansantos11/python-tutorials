from functools import reduce

numbers = [2, 5, 6, 8]

result = reduce(lambda x,y: x+y , numbers)

print(result)
