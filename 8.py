X=Y=0
X=int(input("enter the first number: "))
y=int(input("enter the second number: "))
if(x>y):
    x,y=y,x
    print("the largest number is : ",y)
    print("the smaller number is :  ",x)
else:
    print("the largest number is : ",Y)
    print("the smaller number is : ",x)