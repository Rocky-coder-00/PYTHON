lst=[]
num=int(input('how many numbers: '))
for n in range (num):
    numbers =int(input('enter number '))
    lst.append(numbers)
print("maximum element in the list is:", max(lst))
print("minimum element in the list is:", min(lst))