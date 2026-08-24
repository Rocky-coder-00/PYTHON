list = []
print("Enter elements in the list:")

for i in range(1, 6):
    a = int(input("Enter element: "))
    list.append(a)

print(list)
sum=0
avg=0
for i in list:
    sum=sum+i
    avg=sum/5
    print("the avg is ",avg)