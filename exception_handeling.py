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
    
    