list = []
print("Enter elements in the list:")

for i in range(1, 6):
    a = int(input("Enter element: "))
    list.append(a)

print(list)
max=list[0]
for i in list:
    if i>max:
        max=i

print("the max is max ",max)