"""
W3schools python tutorials practice
Lists
List items are ordered, changeable, and allow duplicate values.
"""
# Loop lists
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numList:
    print(i)
"""
1
2
3
4
5
6
7
8
9
10
"""
# Loop Through the Index Numbers
for i in range(len(numList)):
    print(numList[i])
"""
1
2
3
4
5
6
7
8
9
10
"""

# While Loop
i = 0
while i < len(numList):
    print(numList[i])
    i = i + 1
"""
1
2
3
4
5
6
7
8
9
10
"""

# Looping Using List Comprehension
dayList = ['Monday', 'Tuesday', 'Wednesday']
[print(x) for x in dayList]

dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
newList = []
for x in dayList:
    if 'e' in x:
        newList.append(x)
print(newList) # ['Tuesday', 'Wednesday']

newList.clear()
# [expression for item in iterable if condition == True]
newList = [x for x in dayList if 'e' in x]
print(newList) # ['Tuesday', 'Wednesday']

# Iterable
newList = [x for x in range(10)]
print(newList) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Set all values in the new list
newList = ['Hi' for x in dayList]
print(newList) # ['Hi', 'Hi', 'Hi', 'Hi', 'Hi']