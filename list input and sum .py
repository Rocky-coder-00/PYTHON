list = []
print("Enter elements in the list:")

for i in range(1, 6):
    a = int(input("Enter element: "))
    list.append(a)

print(list)

total = 0
for i in list:
    total = total + i

print("The sum is", total)