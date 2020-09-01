
# This is a comment

# lets print a string
#print("Hello, CS35!", "Some other text", "and theres more...")
# variables
# label = value
# let const var (js)
# int bool short (c)
# first_name = "Tom"
# print("Hello CS35 and" , first_name)
# print("Hello CS35 and " + first_name)
# print("Hello CS35 and" + first_name)
# num = 23.87

# # f strings
# my_string = "    this is a string tom    "
# print(my_string)

# print(my_string.strip())
# print(len(my_string))
# print(len(my_string.strip()))

# st = "sdfsd sdfsdf"

# print(f"Hello CS35 and {len('this is a test')}                {first_name}.......".strip())
# print("something on a new line")

# first_name

# collections

# create an empty list? Array
# my_list = []
# my_list2 = list()

# print(my_list)

# create a list with numbers 1, 2, 3, 4, 5
lst1 = [1, 2, 3, 4, 5]
# add an element 24 to end of lst1
lst1.append(24)
# add an element 12 to the start of lst1
lst1.insert(0, 12)
# print(lst1)

# # print all values in lst2
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
# print(lst1[3])
# print(lst1[4])
# print(lst1[5])
# print(lst1[6])
# print(lst1[7])

# loop over the list using a for loop
# for i in range(len(lst1)):
#     print(lst1[i])

# while loop


# List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4]
squares = [num * num for num in numbers]
# for num in numbers:
#     squares.append(num * num)
# print(numbers)
# print(squares)
# Filtering with a list comprehension
evens = [num for num in numbers if num % 2 == 0]
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)


# create a new list of even numbers using the values of the numbers list as inputs

# print(evens)

# create a new list containing only the names that start with 's' make sure they are capitalized (regardless of their original case)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# print(s_names)

# Dictionaries

# Create a new dictionary

# empty
d1 = {}
d2 = dict()

# key value pairs
d3 = {
    "name": "Tom",
    5676: "wooooooo",
    "age": 34
}

# access an element via its key
d3["name"]

print(d3["name"])
print(d3[5676])

d3["height"] = 345

print(d3)