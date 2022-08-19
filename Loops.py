## If statements
# Basic if statement
x = 33
y = 200
if y > x:
  print("y is greater than x ")

# if Else

a = 33
b = 33
if b > a:
  print("b is greater than a")
else:
  print("a and b are equal")

# Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short hand if 
if a > b: print("a is greater than b")  

# Short hand if... else
a = 2
b = 330
print("A") if a > b else print("B")

# Ternary Operators

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#with three statements 

# Nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

## While Loops    

# basic of while loop
i = 1
while i < 6:
  print(i)
  i += 1

# while loop with break statements

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# While loop with Continue statements  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# While with else statement

  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


## For Loops

# Basic of for loop

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# For loop for strings
for x in "banana":
  print(x)

# For loop using break statements
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  
# For pass Statement 
for x in [0, 1, 2]:
  pass