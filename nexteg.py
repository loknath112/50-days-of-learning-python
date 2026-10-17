'''Python Program: Check Palindrome Number
A palindrome number is a number that remains the same when its digits are reversed.
Examples: 121,  madam isn't a number, 1331, 12321.
 Palindrome Number Checker'''

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
