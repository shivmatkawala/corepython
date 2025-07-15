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


######################################################

                    # SUNDAY CLASS #
                    
# while loop:-

# 1) get the alphabetic charecters from bellow set and 
# form a string and print {use while loop}

# set1 = {"A", 2, 6, "k", "H", "$", 9, 0, 5.5, "I", "A", "L"}
# list1 = list(set1)

# count = 0
# str1 = ""
# while count < len(list1):
#     if str(list1[count]).isalpha():
#         str1 += list1[count]
#         count +=1
#     else:
#         count +=1
#         pass
# print(str1)
    
# NOTE:-
# x = 2
# y = "2"

# print(x.isalpha())  #AttributeError: 'int' object has no attribute 'isalpha'

# print(y.isalpha())



# 2) use str1 and iterate through it and get the integers which are
# odd and form those numbers cubes list. print the list of cubes.

# str1 = "dswk219u034&^$&^ddas95jkqwd3"

# count = 0
# cubes = []
# while count < len(str1):
#     if str1[count].isdigit():
#         if int(str1[count]) % 2 != 0:
#             cubes.append(int(str1[count]) ** 3)
#             count +=1
#         else:
#             count +=1
#             pass
#     else:
#         count +=1
#         pass
# print(cubes)



str2 = "ASDFG!@#$%23456DFGHfgh"
# use while loop and print special charecters

# i = 0

# while i < len(str2):
#     if str2[i].isalnum():
#         i +=1
#         pass
#     else:
#         print(str2[i])
#         i +=1
       
# ask user how many fibonacci numbers want.print fibonacci numbers.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

# num_of_nums = int(input("How many numbers of fibonacci you want: "))

# count = 0
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)

# while count < num_of_nums-2:
#     num3 = num1 + num2
#     print(num3)
#     num1 = num2
#     num2 = num3
#     count +=1
    
#########################################

# with the help of while loop print a tuple of all numbers 
# which are divisible by 7 and 9 in 1 to 100 range


# count = 1
# list1 = []
# while count < 1000:
#     if count % 7 == 0 and count % 9 == 0:
#         list1.append(count)
#         count +=1
#     else:
#         count +=1
#         pass
# print(tuple(list1)) 

######################################################

# for loop :-

# print 1 to 10 all numbers with for loop

# for i in range(1, 10):
#     print(i)


# print A to Z  with for loop

# start = 65

# while start < 91:
#     print(chr(start))
#     start +=1
    

# for i in range(65, 91):
#     print(chr(i))


# print all floats from list with the help of for loop 

# list1 = [1, 2, "3", 'g', 6.5, "9.0", 5, 3.3]


# for i in list1:
#     if type(i) == float:
#         print(i)
#     else:
#         pass


#######################################

# use for loop and print all the prime numbers from 10 to 100

#######################################

# print a table of entered number by user using while 
# loop as well as for loop

# num = int(input("Enter a number: " ))
# count = 1
# while count < 11:
#     print(f"{num} * {count} = {num * count}")
#     count +=1
    
# num = int(input("Ennter a number: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
    
##############################################

list1 = [23, 45, 8, 1, 90, 250, 7, 45, 34, 670, 19, 27]

# with the help of while loop and foor foop find the 
# largest number

# count = 0
# largest = list1[0]

# while count < len(list1):
#     if largest < list1[count]:
#         largest = list1[count]
#     else:
#         pass
#     count +=1
# print(largest)


# largest = list1[0]
# for i in list1:
#     if largest < i:
#         largest = i
#     else:
#         pass
# print(largest)

##########################################

# set1 = {23, "A", 45, 5.5, 1,"%", 2, 90, 67, -6.5, "Mango", 450, 4, -7, 0, -11.5, 29, 5}
# from this set1 find the smallest integer with the help of for loop and while loop

# tup1 = tuple(set1)
# count = 0
# smallest = tup1[0]

# while count < len(tup1):
#     if type(tup1[count]) == int:
#         if smallest > tup1[count]:
#             smallest = tup1[count]
#         else:
#             pass
#     else:
#         pass
#     count +=1
# print(smallest)


# l1 = ["A", 5, 9.5, True, {1, 2}, "mango", 11.5, 0, -4]
# l2 = [1, 'Mango', 5.0, 'A', {2, 1}, False, -4, "M"]

# with the help of for loop create a list of common 
# elements from l1 and l2 
# l3 = []
# for i in l1:
#     if i in l2:
#         l3.append(i)
#     else:
#         pass
# print(l3)


#############################

# str1 = "asnnsk quyaxx9037ede xlii"
# print this string in reverse format using for loop 

# APPLE
# start : end : step
# -1   : 

# for i in range(-1, -len(str1)-1, -1):
#     print(str1[i], end="")
    
############################################################


# str1 = "ASDFGHJK"

# index = 0

# while index < len(str1):
#     print(str1[index])
#     index +=1
    
  
# print 9 to 1 numbers.

# count = 9
# while count > 0:
#     print(count)
#     count -=1
    
#################################################

# find all odd numbers from given list. [while / for]
list1 = [23, True, "Hi", [4, 5, 6, 7], 90, 9, "Password@123"]

# iterate through list
# check whether the element from list1 is a number or not
# check the number is even or odd
# if odd print it
# if even pass it

# while loop

# index = 0

# while index < len(list1):
#     if type(list1[index]) == int:
#         if list1[index] % 2 != 0:
#             print(list1[index])
#         else:
#             pass
#     else:
#         pass
#     index +=1
    


# for loop 

# for i in list1:
#     if type(i) == int:
#         if i % 2 != 0:
#             print(i)
#         else:
#             pass
#     else:
#         pass
            
 
# find all odd numbers from given list. [while / for]
# list1 = [23, True, "Hi", [4, 5, 6, 7], 90, 9, "Password@123", [17, "jai", 6, False], (78, 56, 33, "Hello")]

# index = 0 
# while index < len(list1):
#     if type(list1[index]) == int:
#         if list1[index] % 2 != 0:
#             print(list1[index])
#         else:
#             pass
#     elif type(list1[index]) == list:
#         i = 0
#         while i < len(list1[index]):
#             if type(list1[index][i]) == int:
#                 if list1[index][i] % 2 != 0:
#                     print(list1[index][i])
#                 else:
#                     pass
#             else:
#                 pass
#             i +=1
#     elif type(list1[index]) == tuple:
#         j = 0
#         while j < len(list1[index]):
#             if type(list1[index][j]) == int:
#                 if list1[index][j] % 2 != 0:
#                     print(list1[index][j])
#                 else:
#                     pass
#             else:
#                 pass
#             j +=1
#     else:
#         pass
#     index +=1

# for i in list1:
    # if type(i) == int:
    #     if i % 2 != 0:
    #         print(i)
    #     else:
    #         pass
    # elif type(i) == list:
    #     for j in i:
    #         if type(j) == int:
    #             if j % 2 != 0:
    #                 print(j)
    #             else:
    #                 pass
    #         else:
    #             pass
    # elif type(i) == tuple:
    #     for k in i:
    #         if type(k) == int:
    #             if k % 2 != 0:
    #                 print(k)
    #             else:
    #                 pass
    #         else:
    #             pass
    # else:
    #     pass
        
# import time
# list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in list2:
#     for j in i:
#         print(j)
        
    
    