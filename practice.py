'''practice list
lst = [1, 2, 3, ,4, 3, 4, 5, 6, 7, ,3, 5, 1]
  print(lst)
  output = syntax error'''
lst = [1, 2, 3, 4, 3, 4, 5, 6, 7, 3, 5, 1]
print(lst)
#Remove Duplicates From a List and Keep Order
#syntax : print(list(dict.fromkeys(names)))
print(list(dict.fromkeys(lst)))
'''also we can do it using a loop
lst = [1, 2, 3, 4, 3, 4, 5, 6, 7, 3, 5, 1]
unique_lst = []
for int in lst:
    if int not in unique_lst:
        unique_lst.append(int)
print(unique_lst)
'''
#How can you access the last three elements of the list
print(lst[9:])
#How do you add an element 8 to the end of the list?
lst.append(8)
print(lst)
# How can you count the occurrences of 3 in the list?
count_3 = lst.count(3)
print(count_3)
#How do you remove the first occurrence of 4 from the list?
lst.remove(4)
print(lst)
#How can you reverse the list
lst.reverse()
print(lst)
#sqared list from each element
new_lst = [x**2 for x in lst]
print(new_lst)
#Write a function that returns only unique elements from the list
def unique_list(lst):
    unique_lst = []
    for value in lst:
     if value not in unique_lst:
      unique_lst.append(value)
    return unique_lst 
print(unique_list(lst))

#filter out all even numbers from the list
def even_lst(lst):
    even_lst = []
    for num in lst:
     if num % 2 == 0:
      even_lst.append(num)
    return even_lst 
print(even_lst(lst))

#assending order list
lst.sort()
print(lst)
# desending order without modying the original list
lst.sort(reverse = True)
print(lst)
#double each element in the list using map() - built in ()
double_lst = list(map(lambda x: x * 2,lst))
print(double_lst)
#use filter(){built in ()} to extyract only items grater than 3 
filter_lst = list(filter(lambda x: x>3,lst))
print(filter_lst)
#convert list into set
sett = set(lst)
print(sett)
#difference between two list using sets
lst1 = [1,4,6,5]
lst2 = [4,3,7,8]
diff = set(lst1)-set(lst2)
print(diff)
#create a dictinoary
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])
print(d.get('a',0)+1)
print(d['a'])
#frequency in alist
arr = [1, 1, 2, 3, 2, 1]
dict = {}
for x in arr:
   dict[x]=dict.get(x,0)+1
print(dict)