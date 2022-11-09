#Electricity bill generation
#input: number of units consumed
#0-100 = 0.50 per unit
#100-150 = 1.25 per unit
#150-200 = 2.50 per unit

a = int(input("Enter number of units consumed: "))
if a>=0 and a<=100:
    print("Electric bill is;", 0.50*a)

if a>=100 and a<=150:
    print("Electric bill is;", 1.25*a)

if a>=150 and a<=200:
        print("Electric bill is;", 2.50*a)

#Travel between 1 to  50 KMs -> you pay 2/KMs
#Travel betwwen 50 to 100 KMs -> you pay 4/KMs
#Travel > 100KMs -> you pay 5/KMs
a = int(input("Enter how much distance travelled? "))
b=0
if a>=1 and a<=50:
    b=a*2

if a>=50 and a<=100:
    b=a*4

if a>=100:
    b=a*5

#55 -> 49*2 => 98
#6 -> 6*4 => 24
print("you should pay", b,"Rs.")

