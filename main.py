testingLamba = lambda number: number**2
print(testingLamba(5))

#even or odd when using lambdas

testingSecond = lambda number: 'YES' if number % 2 == 0 else 'NO'

print(testingSecond(5))

#lambda of a sum function

sum = lambda n1, n2: n1 + n2

print(sum(5, 5))

#filter

myList = [1, 2, 3, 4, 5]
result = list(filter(lambda n: n % 2 == 0, myList))

print(result)
