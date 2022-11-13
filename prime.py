number=int(input("Enter number ! "))

isprimenumber=True

for i in range(2,number) :
    if number %i==0 :
        isprimenumber=False

if isprimenumber == True :
    print(number,"is prime")
else:
    print(number,"is not prime")