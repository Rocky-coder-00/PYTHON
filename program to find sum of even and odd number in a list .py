num_list = []
even_sum = 0
odd_sum = 0

number = int(input("Enter total number of elements in list: "))

for i in range(number):
    value = int(input("Enter element: "))
    num_list.append(value)

for i in range(number):
    if num_list[i] % 2 == 0:
        even_sum += num_list[i]
    else:
        odd_sum += num_list[i]

print("\nThe sum of even numbers in the list =", even_sum)
print("The sum of odd numbers in the list =", odd_sum)
