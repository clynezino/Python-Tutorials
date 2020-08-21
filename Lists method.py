numbers = [5, 2, 1, 7, 4]
numbers. append(20)
print(numbers)

numbers = [6, 3, 2, 7, 4]
numbers. insert(0, 10)
print(numbers)

numbers = [6, 8, 3, 1, 2]
numbers. clear()
print(numbers)

numbers = [5, 2, 1, 8, 9]
numbers. pop()
print(numbers)

numbers = [6, 8, 4, 2, 10]
print(numbers.index(6))

# checking the existence of a number
numbers = [6, 7, 5, 3, 1]
print(50 in numbers)

numbers = [6, 8, 7, 6, 5, 2]
print(numbers. count(6))

numbers = [7, 8, 6, 5, 4]
numbers. sort()
print(numbers)

numbers = [7, 8, 6, 5, 4]
numbers. sort()
numbers. reverse()
print(numbers)

numbers = [7, 8, 9, 2, 3, 4]
numbers2 = numbers. copy()
numbers. append(10)
print(numbers2)

# excersize
numbers = [2, 2, 5, 7, 3, 5, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques. append(number)
print(uniques)        