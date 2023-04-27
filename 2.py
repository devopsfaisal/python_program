# Swapping of two numbers without using third variable.

a = int(input("Enter first number = "))
b = int(input("Enter first number = "))

b = a + b
a = b - a
b = b - a

print("Value of a after swapping = %d \nValue of b after swapping = %d" %(a,b))