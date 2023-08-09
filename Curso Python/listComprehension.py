"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
"""

print([x for x in ["apple", "banana", "cherry", "kiwi", "mango"] if "a" in x])


print([str(numero) for numero in [1,2,3,4,5]])
print([int(numero) for numero in ['1', '2', '3', '4', '5']])
