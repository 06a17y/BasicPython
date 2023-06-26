"""
W3schools python tutorials practice
Set
Unordered, Unchangeable
"""
# Create a set
thisSet = {"Monday", "Tuesday", "Wednesday"}
print(thisSet)

# Duplicates Not Allowed
thisSet = {"Monday", "Tuesday", "Wednesday", "Monday"}
print(thisSet)

# Add set Item
thisSet = {"Monday", "Tuesday", "Wednesday"}
thisSet.add("Thursday")
print(thisSet)

# one set add into two set
thisSet = {"Monday", "Tuesday", "Wednesday"}
other = {"Saturday","Sunday"}
thisSet.update(other)
print(thisSet)

# Remove Item
thisSet = {"Monday", "Tuesday", "Wednesday"}
thisSet.remove('Tuesday')
print(thisSet)

thisSet.pop()
print(thisSet)

# clear will empty the set
thisSet.clear()
print(thisSet)

# del will delete the set completely
thisSet = {"Monday", "Tuesday", "Wednesday"}
del thisSet
# print(thisSet)

# Join two sets
# update(), union()
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# Keep only the duplicates
x = {'a','b','c'}
y = {'a','e','f'}
x.intersection_update(y)
print(x)

# Keep All, But NOT the Duplicates
x = {'a','b','c'}
y = {'a','e','f'}
x.symmetric_difference_update(y)
print(x)

# return a new set
x = {'a','b','c'}
y = {'a','e','f'}
z = x.symmetric_difference(y)
print(z)