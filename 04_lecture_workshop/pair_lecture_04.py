# Lecture_04, pair programming m. Anja
# Task: All numbers except one follow the same rule
# return the ODD ONE (7 in this case)


"""
numbers = [2, 4, 6, 8, 7, 10]

for nums in numbers:
    if nums % 2 == 1:
        print(nums)
"""

"""
numbers = [3, 1, 4, 2, 5, 2]

for number in numbers:
    for num in numbers:

        print(number)    
"""

numbers = [3, 1, 4, 2, 5, 2]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
print(duplicates)
