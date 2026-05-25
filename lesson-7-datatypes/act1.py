fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(len(fruits))

print(fruits[0])

print(fruits[-1])

fruits.append("fig")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.sort
print("Sorted fruits:", fruits)

fruits.pop(1)
print("Fruits after popping : \n ", fruits)

fruits.reverse()
print(fruits)

print(fruits*2)

mini_fruits = fruits[:4]
print(mini_fruits)

fruits.clear()
print(fruits)