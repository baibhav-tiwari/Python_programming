x = int(input("enter the first number\n"))
y = int(input("enter the second number\n"))
z = int(input("enter the third number:\n"))
if (x > y) and (x > z):
    print("the largest number is:", x)
elif (y > x) and (y > z):
    print("the largest number is:", y)
elif (z > x) and (z > y):
    print("the largest number is:", z)
else:
    print("enter a valid number")
