# Check Even or Odd wuthout using Modulus
# Check Even or Odd using Bitwise AND '&'

num = int(input("Enter the number = "))

if num&1:
    print("%d is Odd" %num)
else:
    print("%d is Even" %num)