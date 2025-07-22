# COMPREHENSIONS :-

    # TYPES OF COMPREHENSIONS:-
        # 1) LIST COMPREHENSION
        # 2) TUPLE COMPREHENSION
        # 3) SET COMPREHENSION
        # 4) DICTIONARY COMPREHENSION
        
        
# 1) LIST COMPREHENSION:-

# list_of_squares = [i ** 2 for i in range(1, 11)]
# print(list_of_squares)

# count =1

# while count < 11:
#     list_of_squares.append(count **2)
#     count +=1
    
# print(list_of_squares)


# for i in range(1, 11):
#     list_of_squares.append(i ** 2)

# print(list_of_squares)


####################################

# 2) Get the 'a to z' all charecters in list

# lowercase_letters = [chr(i) for i in range(ord('a'), ord('z'))]
# print(lowercase_letters)

# count = ord('a')
# while count < ord('z')+1:
#     lowercase_letters.append(chr(count))
#     count +=1
    
# print(lowercase_letters)


# for i in range(ord('a'), ord('z')):
#     lowercase_letters.append(chr(i))
# print(lowercase_letters)


#########################


# 3) give me all odd numbers in between 35, 60

# odd_nums = [i for i in range(35, 60) if i % 2 != 0]
# print(odd_nums)



# tuple comprehension:-

# t1 = (x for x in range(35, 60) if x % 2 == 0)
# print(t1)

# for i in t1:
#     print(i, end=" ")
    
    
# create a tuple comprehension where all the 
# numbers in between 100 to 200 
# divisible by 3 and 5 are available

# nums_div_by_3_5 = (i for i in range(100, 200) if i % 3 == 0 and i % 5 == 0)
# print(nums_div_by_3_5)

# for i in nums_div_by_3_5:
#     print(i, end=" <-> ")


# write a tuple comprehension which is printing
# all the capitalize words from a string.

# str1 = "My dear Bujji..! you are so lovely, Lets work together and kill our Enemy"


# l1 = str1.split(" ")
# # print(l1)

# capitalize_words = (i for i in l1 if i.istitle())

# for i in capitalize_words:
#     print(i, end=", ")
    

###############################

# Creare a set comprehension of -5 to 6 squares.

# set1 = {i ** 2 for i in range(-5, 7)}
# print(set1)


# create a set comprehension where all the 
# unique charecters from str1 are available

# str1 = "This is mars Ursa Station. I am bobafet 2-0-4-5 agentic AI"

# unique_chars = {i for i in str1}
# print(unique_chars)


# l1 = [1, 2, 3, 4, 5, 9, 3, 6, 10]

# l2 = [3, 4, 5, 6, 7, 6, 5, 9, 19]

# use l1 and l2 and create a set comprehension where from 
# both the lists only common numbers will be there 
# and no duplicate

# commons = {i for i in l1 if i in l2}
# print(commons)


# new_way = set(l1) & set(l2)
# print(new_way)
###################################################



# Dictionary Comprehension:-

dict1 = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
dict2 = {'name':"shiv", 'age':32, 'email':'shiv@gmail.com'}
dict3 = {'A':65, 'B':66, 'C':67, 'D':68, 'E':69}
dict4 = {'countries': ['India', 'Rusia', 'USA', 'Singapore', 'China'], 'capitals':['Delhi', 'Moscow', 'Singapore', 'Bijing']}


# all 1 to 11 numbers squares
dict_squares = {i: i**2 for i in range(1, 11)}
print(dict_squares)


# all even 1 to 11 numbers cubes

dict_cubes = {i: i ** 3 for i in range(1, 11) if i%2 == 0}
print(dict_cubes)

countries = ['India','Rusia', 'China', 'USA', 'Nepal']
capitals = ['Delhi', 'Moscow', 'Bijing', 'Washington DC', 'Kathmandu']

dict_country_caps = {countries[i]: capitals[i] for i in range(len(countries))}
print(dict_country_caps)


dict_chars_ascii = {chr(i): i for i in range(ord('A'), ord('Z')+1)}
print(dict_chars_ascii)


