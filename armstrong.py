
# Armstrong Number Checker

num = int(input("Enter a number: "))

original = num
total = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
