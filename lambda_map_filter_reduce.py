# Lambda:-
    # Lambdas are nothing but functions without name.[namesless functions]
    # Very concise
    # callable
    # easy to use
    
# square = lambda x: x**2
# print(square(5))
# print(square(7))
# print(square(9))

# cubes = lambda y:y**3

# print(cubes(10))
# print(cubes(25))


#######################

# create a lambda function which prints all 
# even nubers in between 40 to 50.

# nums = lambda:[print(x, end=" ") for x in range(40, 50)]
# print(nums())

###########################

# ask users to enter two numbers to enter seperated by comma.
# using lambda perform addition

# nums = input("Enter two numbers seperated by comma: ")

# list_of_nums = nums.split(',')

# addition = lambda x: int(x[0]) + int(x[1]) 

# print(addition(list_of_nums)) 


# tuple1 = ('A', '45', 'p', 78, 12)

# write a lambda which provides an addition of all the numbers
# from tuple1 no matter what data type they are.

# addition = lambda x: sum([int(i) for i in x if type(i) == int or (type(i)== str and i.isdigit())])
# print(addition(tuple1))


str1 = "12,345,6789,99, 45 , 101, 20"

# first collect only those numbers which are lesser 
# than 100, and get the product of them from str1
# use lambda

# list1 = str1.split(',')
# print(list1)
# import math
# list1 = lambda x: math.prod([int(i.strip()) for i in x.split(',') if int(i)< 100])
# print(list1(str1))

