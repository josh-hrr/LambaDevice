testingLamba = lambda number: number**2
print(testingLamba(5))

#even or odd when using lambdas

testingSecond = lambda number: 'YES' if number % 2 == 0 else 'NO'

print(testingSecond(5))

#lambda of a sum function

sum = lambda n1, n2: n1 + n2

print(sum(5, 5))

#filter
# for filtering specific values

myList = [1, 2, 3, 4, 5]
result = list(filter(lambda n: n % 2 == 0, myList))

print(result)

#map
#c to f
# for mapping each object

temps = [("Berlin", 29), ("Cairo", 36), ("LA", 19)]

c_to_f = lambda data:(data[0], (9/5)*data[1] + 32)

mapResult = list(map(c_to_f, temps))

print(mapResult)

#reduce

from functools import reduce

data = [2, 3, 5, 11]

multiply = lambda x, y: x*y

reduceResult = reduce(multiply, data)

print(reduceResult)

#reduce with a for loop

product = 1
for i in data:
    product = product * i

print(product)