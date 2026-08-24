num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
def find_smallest():
    if(num1<num2):
        if(num1<num3):
            smallest=num1
        else:
            smallest=num3
    else:
        if num2<num3:
            smallest=num2

        else:
            smallest<num2

            print("smalest number is: ",smallest)

find_smallest();