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

def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
greet(dog='Tony', cat='mangla', city='hyderabad', password='chimpu@123', subject='physics', sea='arabian')
