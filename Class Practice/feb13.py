# define function

def my_function():
    print("Hello")

# call function

my_function()

# arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# multiple args

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If you do not know how many keyword arguments that will be 
# passed into your function, add two asterisk: ** before the 
# parameter name in the function definition.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement for empty functions

def myfunction():
  pass

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
# cannot use variable name

def my_function(x, /):
  print(x)

my_function(3)

# Keyword-Only Arguments
# have to use variable name

def my_function(*, x):
  print(x)

my_function(x = 3)

# Recursion where function can call itself

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

print("newline ")

# adding
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(1,2))

# multiplying
def mult_two_numbers(num1, num2):
    return num1 * num2

print(mult_two_numbers(1,2))

#odd or even
def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_or_even(4))



