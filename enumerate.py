data=input("data:")
list1=data.split(",")
size=len(list1)
for i in range(size):
    list1[i]=int(list1[i])
print("lenght:", size)
print("list enumerate:", list(enumerate(list1)))
print("max:", max(list1))
print("min:", min(list1))
print("list:", sorted(list1))