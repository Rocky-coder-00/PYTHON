print("1. Calculate area of a square")
print("2. Calculate area of a rectangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    side = float(input("Enter side of the square: "))
    area_square = side * side
    print("Area of the square is:", area_square)
else:
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area_rectangle = length * breadth
    print("Area of the rectangle is:", area_rectangle)

