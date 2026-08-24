import math

def main():
    print("This program finds the real solutions")
    print()

    a = int(input("Please enter the coefficient a: "))
    b = int(input("Please enter the coefficient b: "))
    c = int(input("Please enter the coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)

    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2)

main()