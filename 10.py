# Print Factorial of Series of Numbers
# eg Factorial of 0 to 10

num = int(input("Enter the number whose factorial to print = "))

def fact(num):
    fact_num = 1
    while num >= 1:
        fact_num = fact_num * num
        num = num - 1
    return fact_num

for i in range(num):
    print('Ther Factorial of {} is {}'.format(i+1, fact(i+1)))