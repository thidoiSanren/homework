# for value in range(1, 21):
#     print(value)

# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# numbers = list(range(1, 20, 2))
# for number in numbers:
#     print(number)

# numbers = list(range(3, 31, 3))
# for number in numbers:
#     print(number)

# cube = []
# for value in range(1, 11):
#     cube.append(value**3)
# print(cube)

cube = [value**3 for value in range(1, 11)]
print(cube)
