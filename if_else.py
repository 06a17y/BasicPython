"""
W3schools python tutorials practice
If Else
While
"""
# Short Hand If
a = 10
b = 5
if a > b: print('a is greater than b')

a = 100
b = 100
print('A') if a > b else print("=") if a == b else print('B')

# While
# break statement will stop the loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)