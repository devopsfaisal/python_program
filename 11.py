# Check Multiple return allowed in Python to create a basic calculator

def calc(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div

result = calc(100,20)
print(type(result))
print('Results are: ')

for outcome in result:
    print(outcome)