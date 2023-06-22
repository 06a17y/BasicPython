"""
W3schools python tutorials practice
Tuple
"""
# Change Tuple Values
x = ("Monday", "Tuesday", "Wednesday")
y = list(x)
y[1] = "Friday"
x = tuple(y)
print(x)

# Add Items
x = ("Monday", "Tuesday", "Wednesday")
y = list(x)
y.append('Thursday')
x = tuple(y)
print(x)

# Remove Items
y = list(x)
y.remove('Thursday')
x = tuple(y)
print(x)

# del
a = ("Monday", "Tuesday", "Wednesday")
del a
# print(a) will raise an error because the tuple no longer exists

# Using Asterisk
x = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
(a, b, *c) = x
print(a) # Monday
print(b) # Tuesday
print(c) # ['Wednesday', 'Thursday', 'Friday', 'Saturday']

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)