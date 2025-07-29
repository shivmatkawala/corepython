# Types of Errors in Python Programming:-

    # Syntax Error:-
        # These errors do occur because of programmers mishandeling
        # These errors do occure while code / programme is executed.
        
        # Ex:-
        
# x = input("Enter a value of x: ")
# y = 12
    
    
    # We get understanding of syntax eerror from python or IDE
    

    
    # Logical Error:-
        # These are the most dangerous errors.
        
# a = 5
# b = 10
# if a > b:
#     print(a)
# else:
#     print(a)
    

    # Runtime Error:-
        # 1) ValuueError
        # 2) ZeroDivisionError

# try:
#     x = int(input("Enter a x value:-"))
#     y = int(input("Enter a y value:-"))
#     product = x * y
#     print(product)
    
#     division = x / y
#     print(division)
# except ValueError:
#     print("Only Integers are allowed.")
    
# except ZeroDivisionError:
#     print("Numbers can not be divided by 0")


list1 = [1, 3, 5, 7]


# try:
#     j = int(input("Enter an index: "))
#     print(list1[j])
# except IndexError:
#     print("Index out of range.")
# finally:
#     print("Programme completed..!")



# def xyz(s, m):
#     print(f'sum of {s} and {m} is {s + m}')
    
# try: 
#     xyz(5, 's')
# except TypeError:
#     print("Do provide only 2 arguments.")

# finally:
#     print("Programme ended successfully..!")




# try:
#     from .comprehensions import alpha
#     print(alpha)

# except ImportError:
#     print("attempted relative import with no known parent package")
    
# finally:
#     print("completed..!")
    

###################################

# write a function which does addition, subtration, multiplication,
# division of entered 2 arguments as numbers.

# def arithmetic(x, y):
#     addition = x + y
#     substraction = x - y
#     multiplication = x * y
#     division = x / y
#     return f"Addition of {x} and {y} is {addition}\nSubstraction of {x} and {y} is {substraction}\nmultiplication of {x} and {y} is {multiplication}\nDivision of {x} and {y} is {division}\n"


# print(arithmetic(15, 7))

# try:
#     print(arithmetic(5, 0))
# except TypeError:
#     print("Arithmetic operations can be only performed upon numeric values.")

# except ZeroDivisionError:
#     print("Numbers can not be divided by 0")
# finally:
#     print("Programme has been executed successfully")
    
    

########################################


# write a function which takes set as an argument
# and performs all set operations like
# Union, Intersection, difference, symmetric difference,
# isSubset, isSuperset.
# if any runtime error then handle it.

# def set_operations(set1: set, set2:set):
#     set1_set2_union = set1 | set2
#     set1_set2_diff = set1 - set2
#     set2_set1_diff = set2 -set1
#     set1_set2_intersection = set1 & set2
#     x = set1.issubset(set2)
#     y = set1.issuperset(set2)
    
#     return f"union ={set1_set2_union}\ndiff1 ={set1_set2_diff}\ndiff2 = {set2_set1_diff}\nintersection ={set1_set2_intersection}\nisSubset ={x}\nissuperset ={y}"

# try:
#     print(set_operations({12, 23, 34, 45, 56}, {45, 56, 67, 78, 89}))
# except TypeError as e:
#     print(e)

# finally:
#     print('success..!')
    

# write a programme which takes variable length arguments
# and does find the maximum, minimum and avaerage of it.
# handle exceptions

def compare(*args):
    maximum = max(args)
    minimum = min(args)
    avg = sum(args) / len(args)
    
    print(maximum, minimum, avg)
    
try:
    compare(12, 23, 3, 'M', 43, 32, 21, 90, 34, 11)
except TypeError as e:
    print(e)
    
finally:
    print("success..!")
    
