# Calculate Length of a String without using predefined function

string = input("Enter the String: ")

count = 0

for i in string:
    count += 1
    print(count)

print("Length of the %s = %d" %(string, count))
