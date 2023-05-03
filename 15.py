# We can pass function as argument to another function, for this lambda function is best option.
# function1(function2, sequence)
# filter() can be used to filter values from the given sequence based on some conditions
# filter() function Example

list1 = [0,5,10,15,20,25,30,35,40]

# As type of list2 variable is filter so we have to typecast list2 in list using list()
list2 = list(filter(lambda num : num%2==0, list1))
print(list2)

list3 = list(filter(lambda num : num%2!=0, list1))
print(list3)