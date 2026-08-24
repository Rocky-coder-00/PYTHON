list = []
print("Enter elements in the list:")

for i in range(1, 6):
    a = int(input("Enter element: "))
    list.append(a)

print(list)
mul=1
for i in list:
    mul=mul*i
print("the product is ",mul)
