# Print Fibonacci Series for N numbers

num = int(input("Enter, how many number of fibonacci seriens you want to print = "))

a = -1
b = 1

for i in range(num+1):
    c = a + b
    if c == 0:
        pass
    else:
        print("%d" %c, end = " ")
    
    a = b
    b = c
