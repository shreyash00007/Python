## Calsses in Python

class MyClass:
    x = 5

print(MyClass)

## Objects in Python
# Object
p1 = MyClass()
print(p1.x)

# using classes, objects and function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Shreyash", 21)

print(p1.name)
print(p1.age)

#Objects Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()