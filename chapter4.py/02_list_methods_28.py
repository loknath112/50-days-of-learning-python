friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

print(friends[0])  # Output: Alice

friends.append("Loki")
print(friends)


l1 = [2,33,44,55,66,77,88,99]
l1.reverse()
print(l1)  # Output: [99, 88, 77, 66, 55, 44, 33, 2]


#using the sort() method
l1.sort()
print(l1)  # Output: [2, 33, 44, 55, 66, 77, 88, 99]

l1.insert(2, 22222)
print(l1)  # Output: [2, 22222, 33, 44, 55, 66, 77, 88, 99]