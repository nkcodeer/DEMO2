#code for prime nos
'''
if input is less than 1 then return invlid nos
if input is greater than 1 then ret
> then check if the no is only divisible by 1 and itself then return true , else return false
'''
'''
global scope vs local scope
'''
x = "awesome"

def myfunc():
  y = 5
  print("Python is " + x)
  print("localscope" , y)

myfunc()
#print("checking in global scope"  , y)

'''
List [] items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc

list are changangle and allow duplicate values
'''
'''
if age < 10 then print "baby", if age between 10 to 20 then print school boy, if age more than 20 then print men
'''
print("enter age")
age = input()
age= int(age)

if age < 10:
  print('baby')
elif age > 10 and age < 20:
  print('school boy')
else:
  print('men')

#print 1 to 5
#how to itterate over a string
print(" enter name")
name = input()
for x in name:
  print("printing x here",x)
  print(name)
  print("name")

  #list

  thislist = list(("apple", "banana", "cherry"))
print(thislist)
print(len(thislist))
print(thislist[0])
for x in thislist:
 print(x)
#To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#The insert() method inserts an item at the specified inde
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#priniting nos in new line 
for x in range(1, 6):
 print()
 for y in range(1,x+1):
    print(y,end='')
''''output   =
1
12
123
1234
12345'''
#palindrone nos
num = 12321
reverse = int(str(num)[::-1])

if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
