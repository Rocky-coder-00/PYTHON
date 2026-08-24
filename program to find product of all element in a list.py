num_list=[]
number =int(input("enter total number of element in a list: "))
for i in range(1, number + 1):
    value = int(input("enter element : "))
    num_list.append(value)
    print(num_list)
product = 1
for item in num_list:
    product=product*item
print("product of all element in a list:",product)