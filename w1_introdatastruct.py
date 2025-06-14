# -*- coding: utf-8 -*-
"""IntroDataStruct.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S2gz_4CS_baJNKL7lselENSl7qEDBFRt
"""

print("Hello World")
#Connect colab to GGDrive

a = 10

print(a)

a = 20

print(a)

class Student:
  def __init__(self, name):
    self.name = name


  def __repr__(self):
    return self.name

s = Student("Java")

print(s)

s

#we can combine string easily by this
a = "aaaa" + "bbb"
print(a)

#when using this taking inoput it's always string I have to assign the value
n = input("Please inout number : ")
n = int(n) #change n into integer

if n%2 == 0:
  print("even")
else:
  print("odd")

if n < 0:
  print("%d is negative"%(n))
elif n == 0:
  print(str(n) + " is zero")
else:
  print(str(n) + " is positive")

#while loop
i = 0
while i < 10:
  print(i)
  i += 1

#do while loop
i = 0
while True:
  i+=1
  print(i)
  if i > 10:
    break

1 and 1, 0 or 0, not 0 #what is not 0

#AND
#IF the left one is true we output the second input
#IF the left one is false we output the first input
1 and 2

#OR
#IF the first is true will output the first input
#IF the first is false will output the second input
'a' or 2

n = 10
#use and
n%2 and 'odd' or 'even' #if n%2==0 print odd else print even

for i in ['a','b',123,3.1415]:
  print(i)

#loop through data structure
for i in range(-10, 10):
  print(i)

range(100) #output the range from 0 to 99
#list(range(100)) #convert range to list

for i in range(-10, 10, 2):#skip by 2
  print(i)

#Mutable we only learn List, Dictionary(all the number and value)
#allow to change point to other object instead

#List: allow you to edit the list [mutable]
List = [1, 'abc', 3.1415, s]
print(List)

#Tupple: once you defined it's not allow to change any value [immutable]
Tupple = (1, 'abc', 3.1415, s)
print(Tupple)

List1 = [1,2,3,4,5]
List2 = List1
print(List1, List2)
#we only change value of first List(mutable object) but the second value also change why?
#because List1 point to set of array, and List2 point to List1
#assign value to array then asign array to array could occur errors
List1[0] = 99
print(List1, List2)

# Key(left) value(right) data structure (Dictionary [mutable])
# Key is immutable
# cannot use list as a key as list is mutable object
d = {"ant" : "Ant is the animal with 6 legs", "cat" : "Cat is the animal with 4 legs"}

print(d["ant"])
print(d["cat"])
d["cat"] = "My cat is cute"
print(d["cat"])

#EVERYTHING you type in python is an object
#dir(2)     #show all function in object
#help(2).   #show everthing in integer
#self is this in Java

#__repr__ #overload
class Student:
  def __init__(self,name,age,grade): #init is a constructor, self represents this
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade

  def __repr__(self): #IF not overload it's show this output <__main__.Student object at 0x7cd152aa8750>
    return self.name

s1 = Student('Teatree', 20, 4.00)
s1.get_grade()

print(s1)

def adder(a,b = 0): #asign the defult value
  return a+b
print(adder(12, 2))

def fibo(n):
  if n < 0:
    return "please input positive number"
  else:
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fibo(n-1) + fibo(n-2)

n = int(input("Please input number : "))
fibo(n)

"""$\frac{1}{2}$"""

def f(n):
  A = [0,1]
  for i in range(2, n+1):
    A.append(A[i-1] + A[i-2])
  return A[n]

n = int(input("Please input number : "))
f(n)