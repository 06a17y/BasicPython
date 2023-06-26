"""
W3schools python tutorials practice
Dict
- Above version3.7 is ordered.
- changeable
- duplicates not allowed
"""
# Create a dict
# Basic
Info = {
  "Name": "Jennie",
  "Birth": "6/10",
  "Age": 18
}
print(Info)
# dict()
Info = dict(Name = "Jennie", Age = 18, Birth = "6/10")
print(Info)

# Accessing Items
Info = {
  "Name": "Jennie",
  "Birth": "6/10",
  "Age": 18
}
x = Info['Name']
print(x)
x = Info.get('Name')
print(x)

# Get Keys
x = Info.keys()
print(x)
Info['gender'] = 'female'
print(x)

# Get Values
x = Info.values()
print(x)

# Change Values
Info = {
  "Name": "Jennie",
  "Birth": "6/10",
  "Age": 18
}
Info['Age'] = 20
print(Info)

# Update Values
Info.update({'Gender': 'female'})
print(Info)

# Remove Items
Info.pop('Gender')
print(Info)

Info.popitem()
print(Info)