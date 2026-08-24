num_list=[]
number =int(input("enter total number of element in a list: "))
for i in range(1, number + 1):
    value = int(input("enter element :"))
    num_list.append(value)
    num_list.sort()
print("sorted list is ",num_list)
print("mid value is ",num_list[int(len(num_list)/2)])

