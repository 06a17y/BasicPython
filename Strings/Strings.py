# W3schools python tutorials practice
# Strings

# single/double quotation marks both fine
print("Hi")
print('Hi')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """

print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. '''

print(a)

# Looping Through a String
for i in "Monday":
    print(i)
# M
# o
# n
# d
# a
# y

# String Length
a = 'Monday'
print(len(a))

# Check String
txt = 'The best things in life are free!'
print('free' in txt)