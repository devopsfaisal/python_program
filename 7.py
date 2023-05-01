# Print Fibonacci Series for N numbers using recursion
# import sys
# sys.setrecursionlimit(3000)
num = int(input("Enter, how many number of fibonacci seriens you want to print = "))

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(num):
    print(fibo(i+1), end = " ")