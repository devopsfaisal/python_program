# Print Factorial of any Number

num = int(input("Enter the number whose factorial to print = "))

def fact(num):
    result = 1
    while num>=1:
        result=result*num
        num=num-1
    return result

# print(fact(4))

print('Ther Factorial of {} is {}'.format(num, fact(num)))
