# W3schools python tutorials practice
# Variables

# Create variables
a = 100
print(type(a)) # int

b = 100.25
print(type(b)) # float

c = 'Hi'
print(type(c)) # string

# Single or Double Quotes is both fine
x = "Hi"
x = 'Hi'

# Case Sensitive
# A will not overwrite a
a = 4
A = "Hi"

# One values to Multiple Variables
a = b = c = "Monday"
print(a) # Monday
print(b) # Monday
print(c) # Monday

# Many values to Multiple Variables
a, b, c = "Monday", "Tuesday", "Wednesday"
print(a) # Monday
print(b) # Tuesday
print(c) # Wednesday

# Unpack a Collection
day = ["Monday", "Tuesday", "Wednesday"]
a, b, c = day
print(a) # Monday
print(b) # Tuesday
print(c) # Wednesday

# create a variable with the same name inside a function, this variable will be local
x = "Monday"

def day():
    x = "Tuesday"
    print("Today is " + x) # Today is Tuesday
day()
print("Today is " + x) # Today is Monday