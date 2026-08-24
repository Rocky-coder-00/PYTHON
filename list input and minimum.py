list = []
print("Enter elements in the list:")

for i in range(1, 6):
    a = int(input("Enter element: "))
    list.append(a)

print(list)
min=list[0]
for i in list:
    if i<min:
        min=i

print("the min is ",min)