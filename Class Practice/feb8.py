# how to stop at a number using break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1

# how to continue after breaking at a number
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Print a message once the condition is false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# FOR statements

# print items in a list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print(" ")

# Loop through the letters in the word "banana"

for x in "banana":
  print(x)

print(" ")

# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print(" ")

# exit the loop when x is "banana", but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print(" ")

# where the print statement or its scope matters.
# if in the for scope, or if in the if scope

# With the continue statement we can stop the current iteration of the 
# loop, and continue with the next

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print(" ")

# range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), 
# and ends at a specified number

for x in range(6):
  print(x)

print(" ")

for x in range(2, 6):
  print(x)

print(" ")

# specify the increment value by adding
# a third parameter: range(2, 30, 3)

for x in range(2, 30, 3):
  print(x)

print(" ")

# adding else in for statements

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print(" ")

# else won't print if for breaks

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print(" ")

# a nested loop is a loop inside a loop.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print(" ")

# for loops cannot be empty or you will get
# an error. Use pass statement to avoid error.

for x in [0, 1, 2]:
  pass

print(" ")

# use for loop , print a series of numbers 
# starting with 3 and ending at 60, 
# increment the series with 4.
for x in range(3, 60, 4):
  print(x)

#same thing but with while loop

i = 3
while i < 60:
    print(i)
    i +=4


