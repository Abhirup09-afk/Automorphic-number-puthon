#program to find an automorphic number
#defination: A number whose square ends with the same digits as the number itself. 
# For instance, 25 is automorphic because 25² = 625.

num = int(input("Enter a number: "))

sqr = num ** 2
x = str(sqr).endswith(str(num))

if x == True:
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")