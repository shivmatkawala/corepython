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

#############################################


# map:-

# map is an inbuilt function which takes two
# arguments
# first argument is a lmbda function and second argument is 
# iterable/ collection

# list1 = [2, 3, 4, 5, 6]
# list1_squares = list(map(lambda x: x**2, list1))
# print(list1_squares)


# with the help of map & lambda get the all even 
# numbers from range of 12 to 45

# even_nums = list(map(lambda x: x if x % 2 == 0 else None, range(12, 45)))
# print(even_nums)


# filter 

# filter is an inbuilt function of python
# It is used to filter out the values.

# list1 = [2, 3, 4, 5, 6, 7, 8, 9]

# only_odds = list(filter(lambda x: x if x%2 !=0 else None, list1))

# print(only_odds)


r1 = 'Apple@123'

# filter the r1 and get only numbers 

# only_nums = list(filter(lambda x: x if x.isdigit() else None, r1))
# print(only_nums)


# reduce

# reduce is a method of functools library
# it is used to get the single output of  an iterable

list1 = [1, 2, 3, 4, 5, 6]

from functools import reduce


# total = reduce(lambda x, y : x+y, list1)
# print(total)


# find the maximum from list2
# list2 = [2, 5, 8, 4, 3, 1]
# maximum = reduce(lambda x, y: x if x > y else y, list2)
# print(maximum)



# sorted

# list3 = [(1, 3), (2, 1), (4, 2)]  # [(2, 1), (4, 2), (1, 3)]

# sorted_list3 = sorted(list3, key=lambda x: x[1])
# print(sorted_list3)

list1= [2,4,3,5,8,7,1,6,0]
add = 7
def get_indices(lst, s):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == s:
                print(i, j)
            else:
                pass


get_indices(list1, add)
