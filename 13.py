# Anonymous Funtion or Lambda Funtion Example

# Lambda function to square a number
num = int(input('Enter the number = '))
sqr = lambda num : num * num
print('Square of {} is {}'.format(num, sqr(num)))

# Lambda function to sum of two numbers
num1 = int(input('Enter the First Number = '))
num2 = int(input('Enter the Second Number = '))
sum = lambda num1,num2 : num1+ num2
print('Sum of {} and {} is {}'.format(num1,num2,sum(num1,num2)))

# Lambda function to find highest valum between two numbers
num1 = int(input('Enter the First Number = '))
num2 = int(input('Enter the Second Number = '))
result = lambda num1, num2 : num1 if num1>num2 else num2
print('Highest value between {} and {} is {}'.format(num1,num2,result(num1,num2)))