# Q1. Create a tuple containing integer numbers from 1 to 12, 
# then count how many odd numbers and even numbers in that tuple

# Creating a tuple containing integers from 1 to 12
num_tuple = tuple(range(1, 13))

# initializing

odd_count = 0
even_count = 0

# iterating each number in list
for num in num_tuple:
 
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1

# Output
print("Tuple:", num_tuple)
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)

print(" ")


# Q2. Print numbers from 1 to 7 except for number 3. (Use range function)

sequence = range(1,8)
for x in sequence:
  if x == 3:
    continue
  print(x)

print(" ")


# Q3. let the user enter an integer value,
#     then print the multiplication from 1 to the given value 
#     (EX. given number=3, the result should be 6 (3*2*1)).

user_input = input("Enter an integer: ")
x = int(user_input)

def recursive(x):
    if x <= 1:
        return 1
    else:
        return x * recursive(x - 1)

result = recursive(x)
print("The multiplication of the numbers from 1 to", x, "is", result)

print(" ")

# but I almost forgot about the math function
# for factorials which is much easier

import math

print("The factorial of", x, "is", math.factorial(x))

print(" ")


# Q4. create a list of integers & find the sum of the list elements

#list of 1-10
listofint = list(range(1, 11))
print(listofint)

#adding the list
sumoflist = sum(listofint)
print("The sum of all the numbers in the list is equal to", sumoflist)

print(" ")


# Q5.let the user enter number, then check if this number is palindrome or not

y = input("Enter an integer: ")

def isPalindrome(y):
    return y == y[::-1]

isitpal = isPalindrome(y)
 
if isitpal:
    print("The number entered is a palindrome")
else:
    print("The number entered is not a palindrome")

print(" ")


# Q6. Let the user enter a string, then print each character of that string.

z = input("Enter a word:")

for char in z:
    print(char)

print(" ")


# Q7. Let the user enter a number and check if the number is prime or not

num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
