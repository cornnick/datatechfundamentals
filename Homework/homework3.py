# Q1.write a python function that returns the factorial of a number.(Use recursive function)

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

# Q2.write a python function that takes a list and returns the minimum value in that list.(1 point)

list_of_numbers = [2, 3, 49, 31]

def minfunction(list): 
    min_value = min(list)
    return min_value

min_value = minfunction(list_of_numbers)
print("The minimum value is:", min_value)

print(" ")

# Q3.write a python function that takes a list and returns the maximum value in that list.(1 point)

list_of_numbers = [2, 3, 49, 31]

def maxfunction(list): 
    max_value = max(list)
    return max_value

max_value = maxfunction(list_of_numbers)
print("The maximum value is:", max_value)

print(" ")

# Q4.write a function that takes a word and returns this word in reverse order. (hello>> olleh). (3 points)

def reverse_string(x):
    return x[::-1]

user_input = input("Enter a word: ")
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)

print(" ")

# Q5.write a python function that takes a number and returns the multiplication table for this number.(the multiplication table should start from 1 and end with 12). (2 points)

def multiplication_table(n):
    for i in range(1, 13):
        print(f"{i} x {n} = {n*i}")

number = int(input("Enter a number: "))
multiplication_table(number)

print(" ")

# Q6. write a python function that takes a list and two indexes and changes the list items in these indexes with each other. (3 points) 
# E.x(list[4,7,8,90],1st index 1, 2nd index 3 >> output [4,90,8,7]) .

def switch_indexes(list, index1, index2):
    if index1 >= len(list) or index2 >= len(list):
        return "Index not found"

    list[index1], list[index2] = list[index2], list[index1]
    return list

my_list = [4, 7, 8, 90]
print("Original list:", my_list)
switch_indexes(my_list, 1, 3)
print("List after switching indexes:", my_list)

print(" ")

# Q7.write a python function that takes a string and returns how many capital letters and small letters and numbers in that string. E.x(Hi9 >> output : capital:1, small:1,numbers:1) (3 points)

def count_characters(s):
    capital_letters = sum(1 for char in s if char.isupper())
    lowercase_letters = sum(1 for char in s if char.islower())
    numbers = sum(1 for char in s if char.isdigit())

    return capital_letters, lowercase_letters, numbers

user_input = input("Enter a string: ")
capitals, lowercases, digits = count_characters(user_input)
print(f"Capital letters: {capitals}, Lowercase letters: {lowercases}, Digits: {digits}")

print(" ")

# Q8.write a python function that takes two numbers and returns the result of the power between two numbers.( use recursive function) E.x(7,2 >>output 7^2=49).(3 points)
def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * recursive_power(base, exponent - 1)

print("Find the power of a number.")
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

answer = recursive_power(base, exponent)
print(f"{base}^{exponent} = {answer}")

print(" ")

# Q9.print your name.(1 point) 

print("Nicholas Corn")