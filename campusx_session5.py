#******************Tuples***************
# A tuple in Python is similar to a list. The difference between the two is that 
# we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# Ordered
# Unchangeble
# Allows duplicate

# Creating a Tuple
# Accessing items
# Editing items ----> not posssible like string
# Adding items  ----> not posssible like string
# Deleting items
# Operations on Tuples
# Tuple Functions

# empty
'''t1 = ()
print(t1)
# create a tuple with a single item
t2 = ('hello',)
print(t2)
print(type(t2))
# homo
t3 = (1,2,3,4)
print(t3)
# hetro
t4 = (1,2.5,True,[1,2,3])
print(t4)
# tuple
t5 = (1,2,3,(4,5))
print(t5)
# using type conversion
t6 = tuple('hello')
print(t6)

#************Accessing Items****************
#Indexing
t3 = (1,2,3,4)
print(t3)
print(t3[0])
print(t3[-1])

t5 = (1,2,3,(4,5))
print(t5[3][0])
# Slicing
t3 = (1,2,3,4)
print(t3[::-1])

#*************Editing items**********

# t3 = (1,2,3,4)
# t3[0] = 100   ---->not possible
# print(t3)
# immutable just like strings

# adding elements ---> not possible
# t3[4] = 85
# print(t3)

# Deleting whole items
del t3
print(t3) 

# deleting one element is not possible
# print(t5)
# del t5[-1]

#****************Operations on Tuples**************
# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)

print(t1 + t2)

print(t1*3)
# membership
print(1 in t1)
# iteration
for i in t1:
  print(i)

#**********************Tuple Functions****************
# len/sum/min/max/sorted
t = (1,2,3,4)
len(t)

sum(t)

min(t)

max(t)

sorted(t,reverse=True)

# count

t = (1,2,3,4,5)

t.count(5)

# index
t.index(5)

#**************Difference between Lists and Tuples************
# Syntax
# Mutability
# Speed
# Memory
# Built in functionality
# Error prone
# Usability


#Tuples take less time than Lists
import time 

L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
  i*5
print('List time',time.time()-start)

start = time.time()
for i in T:
  i*5
print('Tuple time',time.time()-start)

#Tuples take less memory than Lists
import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size',sys.getsizeof(L))
print('Tuple size',sys.getsizeof(T))

# Error prone in lists
a = [1,2,3]
b = a

a.append(4)
print(a)
print(b)

# Error prone in tuple
a = (1,2,3)
b = a

a = a + (4,)
print(a)
print(b)

#*************Why use tuple?***********
# tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)

# a,b = (1,2,3)
# print(a,b)

#2
a = 1
b = 2
a,b = b,a

print(a,b)
#3
a,b,*others = (1,2,3,4)
print(a,b)
print(others)

# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

tuple(zip(a,b))'''

#*****************Sets***************
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:

# Unordered
# Mutable
# No Duplicates
# Can't contain mutable data types

# empty
'''s = set()
print(s)
print(type(s))
#single element
s11={4,}
print(s11)
# 1D and 2D
s1 = {1,2,3}
print(s1)
#s2 = {1,2,3,{4,5}}
#print(s2)
# homo and hetro
s3 = {1,'hello',4.5,(1,2,3)}
print(s3)
# using type conversion

s4 = set([1,2,3])
print(s4)
# duplicates not allowed
s5 = {1,1,2,2,3,3}
print(s5)
# set can't have mutable items
# s6 = {1,2,[3,4]}
# print(s6)

#unorded
s1 = {1,2,3}
s2 = {3,2,1}

print(s1 == s2)

#***************Accessing Items***********
# you cannot access element through index or set[] but you can access through loop

# s1 = {1,2,3,4}
# s1[0:3]

# s1 = {1,2,3,4}
# s1[0] = 100

#*******************Adding items************
S = {1,2,3,4}
# add
S.add(5)
print(S)
# update
S.update({5,6,7})
print(S)

#*************Deleting items************
# del
s = {1,2,3,4,6,5,7,5}
# print(s)
# del s[0] ---> never delete through this pattern you can delete whole set through del
# print(s)

# discard
# s.discard(50)  #--->this function take number if the number not present in set then it isnot through error
# print(s)

# remove
# s.remove(50)  #--->this function take number if the number not present in set then it is through error
# print(s)

# pop --> this function delete any random number
s.pop()
print(s)

# clear --->this function delete whole function
s.clear()
print(s)

#************Set Operations*************
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# Union(|)
print(s1 | s2)
# Intersection(&)
print(s1 & s2)
# Difference(-)
print(s1 - s2)
print(s2 - s1)
# Symmetric Difference(^)
print(s1 ^ s2)
# Membership Test
print(1 not in s1)
# Iteration
for i in s1:
  print(i)

#******************Set Function***********
# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
len(s)
sum(s)
min(s)
max(s)
sorted(s,reverse=True)

# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# s1 | s2
s3= s1.union(s2)
print(s3)
s1.update(s2)
print(s1)

# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection_update(s2)
print(s1)
print(s2)

# difference/difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.difference_update(s2)
print(s1)
print(s2)

# symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

print(s1.isdisjoint(s2))

s1 = {1,2,3,4,5}
s2 = {3,4,5}

print(s1.issuperset(s2))

# copy
s1 = {1,2,3}
s2 = s1.copy()

print(s1)
print(s2)

#*************Frozenset************
# Frozen set is just an immutable version of a Python set object

# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

print(fs1 | fs2)

# When to use
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
print(fs)

# what works and what does not
# works -> all read functions
# does't work -> write operations

#******************Set Comprehension**********
# examples

print({i**2 for i in range(1,11) if i>5})'''

#**************Dictionary************
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

#*************Create Dictionary**********
'''# empty dictionary
d = {}
print(d)
# 1D dictionary
d1 = { 'name' : 'nitish' ,'gender' : 'male' }
print(d1)
# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
print(d2)
# 2D dictionary -> JSON
s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
print(s)
# using sequence and dict function
d4 = dict([('name','nitish'),('age',32),(3,3)])
print(d4)
# duplicate keys
d5 = {'name':'nitish','name':'rahul'}
print(d5)
# mutable items as keys
d6 = {'name':'nitish',(1,2,3):2}
print(d6)

#*****************Accessing items***********

my_dict = {'name': 'Jack', 'age': 26}
# []
print(my_dict['age'])
# get
print(my_dict.get('age'))

s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
print(s['subjects']['maths'])

#**************Adding key-value pair*************

d4 = dict([('name','nitish'),('age',32),(3,3)])
d4['gender'] = 'male'
print(d4)
d4['weight'] = 72
print(d4)

s['subjects']['ds'] = 75
print(s)

#****************Remove key-value pair************

d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}

# pop
d.pop(3)
print(d)

#d.popitem() -->removes the item that was last inserted into the dictionary
d.popitem()
print(d)

# del -->used to in-place delete the key that is present in the dictionary in Python
del d['name']
print(d)

del s['subjects']['maths']
print(s)

# clear -->delete whole element
d.clear()
print(d)

#**************Editing key-value pair*************

s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
s['subjects']['dsa'] = 80
print(s)

#**************Dictionary Operations***********
# Membership
print(s)

print('name' in s)

#iteration
d = {'name':'nitish','gender':'male','age':33}

for i in d:
  print(i,d[i])

#**************Dictionary Functions****************
# len
d = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
print(len(d))

# sorted
print(sorted(d,reverse=True))

#max
print(max(d))

# items/keys/values
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}

print(d.items())
print(d.keys())
print(d.values())

# update
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}

d1.update(d2)
print(d1)

#***********Dictionary Comprehension**********
# {key:values for vars in iterables} 

# print 1st 10 numbers and their squares
print({i:i**2 for i in range(1,11)})

# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

print({i:j for (i,j) in zip(days,temp_C)})

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

print({key:value for (key,value) in products.items() if value>0})

# Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})'''