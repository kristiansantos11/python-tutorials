# doubles the value of each element in the given list
numbers = [2, 3, 4, 5]

result = list(map(lambda n: n*2, numbers))
print(result)

for i in result:
    print(i)
