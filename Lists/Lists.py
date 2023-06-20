"""
W3schools python tutorials practice
Lists
List items are ordered, changeable, and allow duplicate values.
"""
# Negative Indexing
dayList = ["Monday", "Tuesday", "Wednesday"]
print(dayList[-1]) # Wednesday

fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit[2:5]) # ["cherry", "orange", "kiwi"]

#Change Item Value
dayList = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
dayList[3] = 'Thursday'
print(dayList) # "Monday", "Tuesday", "Wednesday", "Thursday"]

dayList = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
dayList[3:4] = ['Thursday']
print(dayList)

# Insert Items
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
dayList.insert(4, "Friday")
print(dayList) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Append Items
# add item to the end of the list
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
dayList.append('Friday')
print(dayList) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Append two lists
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
weekList = ['Saturday', 'Sunday']
dayList.extend(weekList)
print(dayList) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']

# Remove Specified Item
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
dayList.remove("Wednesday")
print(dayList) # ['Monday', 'Tuesday','Thursday']

# Remove Specified Index
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
dayList.pop(1)
print(dayList) # ['Monday', 'Wednesday', 'Thursday']
# do not specify the index, the pop() method removes the last item.
dayList.pop() 
print(dayList) # ['Monday', 'Wednesday']
# del can also remove
del dayList[0]
print(dayList) # Monday

# Clear the list
dayList.clear()
print(dayList) # []