#Question 1

value1 = input("Enter an Integer:")
value2 = input("Enter another Integer:")

value1 = int(value1)
value2 = int(value2)

adding = value1 + value2
subtracting = value1 - value2
multiplying = value1 * value2
dividing = value1 / value2

print(value1, "+", value2, "= ", adding)
print(value1, "-", value2, "= ", subtracting)
print(value1, "*", value2, "= ", multiplying)
print(value1, "/", value2, "= ", dividing)



#Question 2

import math

sqrt1 = math.sqrt(value1)
sqrt2 = math.sqrt(value2)

print("The square root of your first number =", sqrt1)
print("The square root of your second number =", sqrt2)

mod = value1 % value2

print("The remainder of", value1, "/", value2, "=", mod)

expo = value1 ** value2

print(value1, "to the", value2, "power =", expo)



#Question 3

isequal = value1 == value2
isgreater = value1 > value2
isless = value1 < value2

print("Your first number is equal to your second number:", isequal)
print("Your first number is greater than your second number:", isgreater)
print("Your first number is less than your second number:", isless)



#Question 4A

myname = "Nicholas"

print(myname, "has", len(myname), "characters.")

#Question 4B

mynameupper = myname.upper()

print(mynameupper)

#Question 4C

if mynameupper.startswith('F'):
    print("The first letter of the string starts with 'F'.")
else:
    print("The first letter of the string doesn't start with 'F'.")



#Question 5A

myhobbies = ["photography", "web development", "woodworking", "graphic design"]

#Question 5B

print("There are", len(myhobbies), "hobbies in the list.")

#Question 5C

myhobbies.sort()

print("The list in ascending alphabetical order is:", myhobbies)

#Question 5D

myhobbies.sort(reverse = True)

print("The list in descending alphabetical order is:", myhobbies)

#Question 5E

myhobbies.pop()

print("Here's the list with the last item removed:", myhobbies)



#Question 6

fact = math.factorial(7)

print("The factorial of 7 is:", fact)
















