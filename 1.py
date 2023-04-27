# Swapping of two numbers using third variable.

a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

temp = a
a = b
b = temp

print("Value of a after swapping = %d \nValue of b after swapping = %d" %(a,b))