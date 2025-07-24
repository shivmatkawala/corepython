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

def get_right_angle_triangle_area(height, base):
    area = 0.5 * height * base
    print(area)
    
get_right_angle_triangle_area(10, 5)
get_right_angle_triangle_area(20, 10)
