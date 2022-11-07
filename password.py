i=1

passwordMatched=False
password=""

while i<=3:
    password=input("Enter password!")
    if password=="abc":
        passwordMatched=True
        break
        i=i+1

if passwordMatched==True:
    print("Login successfull!")
else:
    print("Access Denied!")
