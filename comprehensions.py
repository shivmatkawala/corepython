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
    
    



