# print("Welcomme to 'MARRIAGE ELIGIBILITY APP'.")

# age = int(input("Enter your age: "))

# if age == 0 or age < 0:
#     print("Please enter a valid age..!")
    
# if age > 0 and age < 18:
#     print("You are still kid . not eligible to get married")
    
# if age == 18:
#     print("Congrats..! you turned 18 and got eleigible to get married")
    
# if age > 18 and age <35:
#     print("Please get married you are allowed")

# if age >= 35 and age < 50:
#     print("You got late to get marrieed but its okay. get married soon.")
    
# if age > 50:
#     print("Man..! Try in next life")

#############################################

# Only there are two conditions:
    # if 
    # else
    
# number = int(input("enter a number: "))

# if number  % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# isMarried = input("Are you married[Y/n]: ")

# if isMarried.upper() == "Y":
#     print("Yes ..! You are married")
# else:
#     print("No ..! You are not married")
    

# If more than two conditions:
    # if
    # elif  --> else+if
    # elif
    # else
    
# Ask user to enter a salary:

# condition1 : if salary is less than 10000 --> Economically backward
# condition2 : if salary is greater than 10000 and lesser than 20000 --> Economically lower middle class
# condition3 : if salary is greater than 20000 and lesser than 50000 --> Economically middle class
# condition4 : if salary is greater than 50000 and lesser than 100000 ---> Economically upper middle class
# condition5 : if salary is greater than 100000 ---> Economically upper class

####################################################

# Nested Conditions

# Ask user to enter a number in between 0 to 100
    # condition1 :- if number is in between 0-25 --> quarter no.1
        # condition1A:- if number is even print "Even"
        # condition1B:- if number is odd print "Odd"
        
     # condition2 :- if number is in between 26-50 --> quarter no.2
        # condition2A:- if number is even print "Even"
        # condition2B:- if number is odd print "Odd"
        
    # condition3 :- if number is in between 51-75 --> quarter no.3
        # condition3A:- if number is even print "Even"
        # condition3B:- if number is odd print "Odd"
        
    # condition4 :- if number is in between 76-100 --> quarter no.4
        # condition4A:- if number is even print "Even"
        # condition4B:- if number is odd print "Odd"
        

# num = int(input("Enter a number in between 0 to 100: "))

# if num >= 0 and num < 26:
#     print("quarter no. 1")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# elif num >= 26 and num < 51:
#     print("quarter no. 2")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# elif num >= 51 and num < 76:
#     print("quarter no. 3")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# elif num >= 76 and num < 101:
#     print("quarter no. 4")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# else:
#     print("Entered incorrect number.\nPLease eneter number from 0 to 100 range.")
    
    
# ask user to enter a number, first check wether number is
# even or odd, if  even print "Even" if odd print "odd".
# and then check number is divisible by 3 & 5 both
# if divisible print "Divisible" if not print "Not Divisible"

# number = int(input("Eenter a number: "))

# if number % 2 == 0:
#     print("Even")
#     if number % 3 == 0 and number % 5 == 0:
#         print("Divisible")
    
#     else:
#         print("Not Divisible")
# else:
#     print("Odd")
    
#     if number % 3 == 0 and number % 5 == 0:
#         print("Divisible")
    
#     else:
#         print("Not Divisible")
    

# str1 = 'Hello How are you ?'

# check wether string in title case, upper case, lower case, 
# capitalize case or mixed case.
# is there any special charecter in string or not.
# if it is there print "yes there is a special charecter"
# else print "No there is no special charecter"


# if str1.islower():
#     print("Lower")
#     if " " in str1 or "@" in str1 or "!" in str1 or "." in str1 or "?" in str1:
#         print("Yes there is a special charecter")
#     else:
#         print("No Special Charecter")
        
# elif str1.isupper():
#     print("Upper")
    
#     if " " in str1 or "@" in str1 or "!" in str1 or "." in str1 or "?" in str1:
#         print("Yes there is a special charecter")
#     else:
#         print("No Special Charecter")
    
# elif str1.istitle():
#     print("title")
    
#     if " " in str1 or "@" in str1 or "!" in str1 or "." in str1 or "?" in str1:
#         print("Yes there is a special charecter")
#     else:
#         print("No Special Charecter")
    
# elif str1[0].isupper() and str1[1::].islower():
#     print("Capitalize")
    
#     if " " in str1 or "@" in str1 or "!" in str1 or "." in str1 or "?" in str1:
#         print("Yes there is a special charecter")
#     else:
#         print("No Special Charecter")
    
# else:
#     print("Mixed")
#     if " " in str1 or "@" in str1 or "!" in str1 or "." in str1 or "?" in str1:
#         print("Yes there is a special charecter")
#     else:
#         print("No Special Charecter")