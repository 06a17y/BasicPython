# W3schools python tutorials practice
# Slice Strings

a = "Today is Monday!"
print(a[2:5]) # day
print(a[:5]) # Today
print(a[-4:-2]) #da

# Modify Strings
# Upper & Lower
a = "Today is Monday!"
print(a.upper()) # TODAY IS MONDAY!
print(a.lower()) # today is monday!
print(a.strip())

# Replace String
a = "Today is Monday!"
print(a.replace('T','A')) # Aoday is Monday!

# Split String
a = "Today is Monday!"
print(a.split(' ')) # ['Today','is','Monday']

# Format String
age = 18
txt = "My name is Jenny, and I am {}."
print(txt.format(age)) # My name is Jenny, and I am 18.

qty = 3
itemNo = 157
price = 49.85
order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(order.format(qty, itemNo, price)) # I want to pay 48 dollars for 3 pieces of item 157.

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."

# Single quote \'
txt = 'It\'s alright.'
print(txt) #It's alright.

# Backslash \\
txt = "This will insert one \\ (backslash)."
print(txt) # This will insert one \ (backslash).

# Tab
txt = "Hello\tWorld!"
print(txt) # Hello  World!

# Erases one character (backspace)
txt = "Hello \bWorld!"
print(txt) # HelloWorld!