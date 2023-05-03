# We can pass function as argument to another function, for this lambda function is best option.
# function1(function2, sequence)
# filter() can be used to filter values from the given sequence based on some conditions
# filter() function Example

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
list1 = [0,5,10,15,20,25,30]
list2 = list(filter(isEven, l))
print(type(list2))
print(list2)