# Q1.create a function called CircleArea , which calculates the circle area based on this formula( π*r^2 ).
import math

def circleArea(r):
    print((math.pi)*(r**2))

circleArea(2)


# Q2.write a python function called calculate that takes two numbers and symbol and do the calculations based on this symbol E.X(calculate(7,2,+))

def calculate():
    num1 = float(input("Enter the first number: "))
    symb = input("Enter the operation symbol (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if symb == '+':
        return num1 + num2
    elif symb == '-':
        return num1 - num2
    elif symb == '*':
        return num1 * num2
    elif symb == '/':
        return num1 / num2
    else:
        return "Error"

result = calculate()
print("Answer: ", result)


# Q3.Write a function that checks how many vowels in a string.

def num_vowels():
   
    input_string = input("Enter a word or sentence: ").lower()
    vowels = 'aeiou'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

vowel_count = num_vowels()
print("Number of vowels:", vowel_count)


# Q4.write a python function that takes a list and prints all the elements in that list using loops.

def print_list_items(mylist):
 
    for element in mylist:
        print(element)

list_of_numbers = [1, 2, 3]
print_list_items(list_of_numbers)

# Q5.write a python function that returns the factorial of a number.(Use recursive function)

user_input = input("Enter an integer: ")
x = int(user_input)

def recursive(x):
    if x <= 1:
        return 1
    else:
        return x * recursive(x - 1)

result = recursive(x)
print("The multiplication of the numbers from 1 to", x, "is", result)