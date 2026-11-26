# Write a program to print user's first name and print its length.
name = input("Enter your first name: ")
print("Your first name is", name, "and its length is", len(name))


# Write a program to find the occurrence of "$" in the string.
string2 = "I have $100 and $200 in my bank account, I want to buy new $50 shoes."
print("Number of $ in the string =", string2.count("$"))


# ----- Conditional Statements -----

# Write a program to check if a number entered by user is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Write a program to find the greatest of 3 numbers entered by user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is greatest, value =", a)
elif b >= a and b >= c:
    print("B is greatest, value =", b)
else:
    print("C is greatest, value =", c)


# Write a program to check if a number is a multiple of 7 or not.
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Multiple of 7.")
else:
    print("Not a multiple of 7.")
