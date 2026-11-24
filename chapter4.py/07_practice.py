#Python List Methods Example
fruits = ["Apple", "Banana", "Mango", "Orange"]

# 1. append()
fruits.append("Grapes")
print("Append:", fruits)

# 2. extend()
fruits.extend(["Kiwi", "Papaya"])
print("Extend:", fruits)

# 3. pop()
fruits.pop()
print("Pop:", fruits)

# 4. sort()
fruits.sort()
print("Sort:", fruits)

# 5. reverse()
fruits.reverse()
print("Reverse:", fruits)

# 6. index()
print("Index:", fruits.index("Mango"))

# 7. count()
print("Count:", fruits.count("Apple"))

# 8. copy()
new_fruits = fruits.copy()
print("Copy:", new_fruits)

# 9. clear()
new_fruits.clear()
print("Clear:", new_fruits)