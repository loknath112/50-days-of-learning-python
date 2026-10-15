
# Student Grade Calculator

marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks!")
elif marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
    #this code make a grade calculator that takes input from the user and outputs the corresponding grade based on the marks entered. It also checks for invalid input and handles it appropriately.
