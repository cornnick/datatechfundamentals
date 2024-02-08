a = 4
b = 5
print("A") if a > b else print("=") if a == b else print("B")

#nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")