#code for prime nos
'''
if input is less than 1 then return invlid nos
if input is greater than 1 then ret
> then check if the no is only divisible by 1 and itself then return true , else rwtuen false
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
print("checking in global scope"  , y)
