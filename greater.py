a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b:
    if a>c:
        print(a, "is the greater number")
    else:
        print(c, "is the greater number")
else:
    if b>c:
        print(b, "is the greater number")
    else:
        print(c, "is the greater number")
