nterms = int(input("enter the length of the series : \n"))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("please,enter a valid number")
else:
    print("the fibonacci series is : \n")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
