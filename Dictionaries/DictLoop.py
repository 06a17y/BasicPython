"""
W3schools python tutorials practice
Dict
- Above version3.7 is ordered.
- changeable
- duplicates not allowed
"""
# Loop
Info = {
  "Name": "Ford",
  "Birth": "10/25",
  "Age": 19
}

# get keys and values
for i in Info:
    print(i) # keys
    print(Info[i]) # values

for i in Info.keys():
    print(i)
for j in Info.values():
    print(j)

for i, j in Info.items():
    print(i, j)