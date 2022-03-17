num = int(input("enter the number :\n"))
if num < 0:
    print("enter a valid number.")
else:
    fact = 1
    while num > 0:
        fact = fact*num
        num -= 1
    print("the factorial of the given number is :", fact)
# try:
# 	x = int(input("Please input the number to calculate factorial of the number\n"))
# 	print("You entered=", x)
# 	if (x < 0):
# 		print("The factorial of numbers below 0 is not defined")
# 		exit
# 	else:
# 			factorial = 1
# 			while x > 0
# 			    factorial = factorial*x
# 			    x -= 1
# 		    print ("The factorial of ", x ," is :", )
# except TypeError:
# 	print ("Data type error occured, Please provide any positive number to calculate factorial of it.")
