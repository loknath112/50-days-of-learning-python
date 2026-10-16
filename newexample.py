#Python Program: Fibonacci Series
#The Fibonacci series is a sequence in which each number is the sum of the previous two numbers.

# Fibonacci Series

n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
