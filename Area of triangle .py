side1=float(input("enter first side of a triangle:"))
side2=float(input("enter second side of a triangle:"))
side3=float(input("enter third side of a triangle:"))
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("area od a tiangle is:",area)