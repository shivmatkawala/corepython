# In Programming world there are multiple paradigms

# write a programme which displays all numbers in between
# 20 to 30

# for i in range(20, 30):
#     print(i)

# write a programme which takes string as an input from
# user and displays all vowels in it.

# str1 = input("Enter your string: ")

# for i in str1:
#     if i.lower() in "aeiou":
#         print(i)
#     else:
#         pass

# write a programme which creates a fibonacci series upto
# user specified position.

# x = 0
# y = 1

# pos = int(input("Enter how many fibonaccie numbers you want: "))
# for i in range(0, pos):
#     num = x + y
#     print(x)
#     x, y = y, num
    
###################################
# def get_numbers():
#     for i in range(20, 30):
#         print(i)



# def updated_get_numbers(start, end):
#     pi = 3.14
#     for i in range(start, end):
#         print(i)
        

# updated_get_numbers(10,20)

# print("---------------")

# updated_get_numbers(50, 55)

# print("---------------")

# updated_get_numbers(100, 110)

#####################################
# def get_vowels():
#     str1 = input("Enter your string: ")

#     for i in str1:
#         if i.lower() in "aeiou":
#             print(i)
#         else:
#             pass

###############################
# def get_fibonacci():
#     x = 0
#     y = 1

#     pos = int(input("Enter how many fibonaccie numbers you want: "))
#     for i in range(0, pos):
#         num = x + y
#         print(x)
#         x, y = y, num
        
#################################################
# get_numbers()
# get_vowels()
# get_fibonacci()


########################################

# write a function which prints area of a right angle triangle

# def get_right_angle_triangle_area(height, base):
#     area = 0.5 * height * base
#     print(area)
    
# get_right_angle_triangle_area(10, 5)
# get_right_angle_triangle_area(20, 10)


################################################

# create a function which flattens a nested list.
l1 = [[1,2], [3,4],[5,6],[7,8]] #--> nested list
#l2 = [1,2,3,4,5,6,7,8]


# def flatten_list(l): # function head
#     fl  = []         # function body
#     for i in l:
#         for j in i:
#             fl.append(j)
#     print(fl)
    
# flatten_list(l1)     # function call


###############################

# def greet():
#     print("Hello Students")

# greet()

####################################################
# def greet(name):            # Positional arguments
#     print(f"Hello {name}")
    
# greet('Manasa')
# greet("Praveen")
# greet("students")

# def greet(girl, boy):
#     print(f"Hello {girl}, you are a girl")
#     print(f"Hello {boy}, you are a boy")
    
# greet("Manasa", "Praveen")
# greet("Praveen", "Manasa")

######################################################

# def greet(name="Students"):  # default argument
#     print(f"Hello {name}")
    
# greet()
# greet("Manasa")
# greet("Praveen")

#########################################

# def greet(person1, person2, person3, person4, person5):
#     print(f"Hello {person1}")
#     print(f"Hello {person2}")
#     print(f"Hello {person3}")
#     print(f"Hello {person4}")
#     print(f"Hello {person5}")
    
# greet('vanishri', 'sushma', 'venkat', 'manasa', 'vennky')



# def greet(*args):     # Variable Length Arguments
#     for i in args:
#         print(f"Hello {i}")

# greet("Shwetha", 'Ashika', "Ganesh", "Mallesh", "Avinash", "Poojitha", "Surender", "Devi", "Satya", "Baji", "Anna", "Tai", "Doddanna")


###################################
# Keyword arguments
# def greet(friend, student, wife, brother):
#     print(f"Hello brother {brother}")
#     print(f"Hello friend {friend}")
#     print(f"Hello wife {wife}")
#     print(f"Hello student {student}")
    
# greet(student="Chandra", brother="Lokesh", wife="Sujatha", friend="Sagar")

##############################################

# variable length keyword arguments

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
        
# greet(dog='Tony', cat='mangla', city='hyderabad', password='chimpu@123', subject='physics', sea='arabian')


###############################

# convert binary to decimal --> int()
# convert decimmal to binary --> bin()

# x = int('00000000', 2)
# y = int('11111111', 2)
# print(x)
# print(y)

# print(bin(120))

# print(ord('a'))

# print(bin(97))

# write a function which takes two numbers as argument 
# and performs addition, subtration, division and 
# multiplication and returns the output.

# def arithmetics(x, y):
#     addition = x + y
#     substraction = x - y
#     multiplication = x * y
#     division = x / y
#     return f"addition of {x} and {y}= {addition}\nsubtraction of {x} and {y}= {substraction}\ndivision of {x} and {y}= {division}\nmultiplication of {x} and {y}={multiplication}"

# print(arithmetics(10, 5))



# write a function which takes multiple arguments as numbers
# and returns the maximum,minimum number from it.

# def max_min(*args):
#     return f"maximum of enterd numbers is {max(args)}\nminimum of enetered numbers is {min(args)}"

# print(max_min(2, 3, 4, 6,1, 9, 5, 8))



# write a function which takes list as an argument and 
# returns all integers from it.

# l1 = [1, 3, 'A', True, (1, 2, 3), 5, 6.2]

# def get_ints(mixed_list):
#     for i in mixed_list:
#         if type(i) == int:
#             print(i)
#         else:
#             pass
# get_ints(l1)


# write a function which returns indices of those numbers 
# from provided list as an argument whose addition is 7.

# l2 = [10, 2, 13, 4, 5, 6, 7, 8, 3, 1]

# def get_addition_7_indicees(list):
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if list[i] + list[j] == 7:
#                 print(i, j)
#             else:
#                 pass
# get_addition_7_indicees(l2)


# write a function which flattens a nested list.
l3 = [[1,2], [3, 4], [5, 6], [7, 8]]
# [1, 2, 3, 4, 5, 6, 7, 8]

# def flatten_list(list):
#     l4 = []
#     for i in list:
#         for j in i:
#             l4.append(j)
#     return(l4)

# print(flatten_list(l3))


# write a function which takes dictionary of squares where 
# number is key and its square is value as an argument.
# print values in descending order.

dict1 = {2:4, 6:36, 9:81, 4:16, 5:25, 8:64, 1:1, 3:9} 
# 81, 64, 36, 25, 16, 9, 4, 1

# def get_values_descending(dictinary: dict):
#     l1 = list(dictinary.values())
#     l1.sort(reverse=True)
#     print(l1)
    
# get_values_descending(dict1)

       
# write a function which takes argument as shape:-

# circle --> enter a radius --> return area, perimeter
# rectangle --> enter a length, enter a width --> area and perimeter
# square --> enetr a side --> return area and perimeter
# right_angle_triangle --> enter a base, enter a height --> area and perimeter 


import math

def get_area_peri(shape: str):
    if shape.lower() == "circle":
        r = float(input("enter a radius of circle: "))
        area = math.pi * (r ** 2)
        return f"area of a circle with {r} raadius is {area}"
    
    elif shape.lower() == "square":
        side = float(input("enter a side of square: "))
        area = side * side
        return f"area of a square with side {side} is {area}"
    
    elif shape.lower() == "rectangle":
        length = float(input("Enter a length of a rectangle: "))
        width = float(input("Ennter a width of rectangle: "))
        
        area = length * width
        return f"area of a rectangle with length {length} and width {width} is {area}"
    
    elif shape.lower() == "rta":
        height = float(input("enter a height of right angle triangle: "))
        width = float(input("Enter a width of right angle triangle: "))
        
        area = height * width * 0.5
        return f"area of a right angle triagle with height {height} and width {width} is {area}"
    else:
        return "I dont know about this shape. sorry..!"
    
print(get_area_peri('rectangle'))
        


