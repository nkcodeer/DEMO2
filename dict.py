#dict 
student = {"name": "Rahul","age": 22,"course": "Computer Science","grade": "A"}
print(student["name"])
#creating dict of 5 student and marks
# Creating a dictionary of students with their marks
students_marks = {"Ankul": 85,"Rahul": 90,"Piyush": 78,"Shivam": 92,"Ankit": 88}
print("the marks of rahul is ", students_marks["Rahul"])
#delete 
students_marks.pop("Ankul")
print(students_marks)
#check if key exists
for x in students_marks:
    print(x)
#Write a function that checks whether a given key exists in a dictionary.
def key_exists(dictionary, key):
    return key in dictionary
my_dict = {"Ankul": 85,"Rahul": 90,"Piyush": 78,"Shivam": 92,"Ankit": 88}
key_check = "Shivam"
if key_exists(my_dict, key_check):
    print(f"The key '{key_check}' exists in the dictionary.")
else:
    print(f"The key '{key_check}' does not exist.")
# Write a Python program to iterate through all keys and values of a dictionary and print them.
for x, y in my_dict.items(): #items() method is used to iterate through the dictionary, which returns key-value pairs.
 print(f"{x}:{y}") 
 '''f" = The f in print(f"{key}: {value}") indicates that the string is an f-string, 
 which stands for "formatted string literal. '''
#Write a Python program to merge two dictionaries into one.
merged_dict = {**student,**my_dict}
print(merged_dict)
#max and min value in dict
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print(max_value)
print(min_value)
#Invert a Dictionary (Swap Keys and Values)