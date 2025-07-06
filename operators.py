# OPERATORS

    # 1) Arithmetic Operators:-
# x = 5
# y = 2

        # Addition +
# print(f"{x} and {y} Addition is : {x + y}")

        # Subtracction -
# print(f"{x} and {y} Subtraction is : {x  - y}")

        # Multiplication *
# print(f"{x} and {y} Multiplication is : {x * y}")

        # Normal Division /
# print(f"{x} and {y} Normal Division is : {x / y}")

        # Floor Division  //
# print(f"{x} and {y} Floor Division is : {x // y}")

        # Power **
# print(f"{x} Power is {y} : {x ** y}")

        # Mod %
# print(f"{x} Mod {y} is : {x + y}")

    # 2) Assignment Operator:-
        # To assign a value to a variabble we use =
# m = 10
# n = "fathima"

x = 5

        # add and assign operator +=
# x = x + 3
# print(x)
# x+=3
# print(x)

        # subtract and assign operator -=
# x-=2
# print(x)
        # multiply and assign operator *=
# x *= 4
# print(x)
        # normal division and assign operator /=
# x /= 5
# print(x)

        # Floor division and  assign operator //=
# x //= 3
# print(x)

        # Power and assign **=
# x **=2
# print(x)

   
        # mod and assign %=
# x %=7
# print(x)

    # 3) Comparison Operator:-
# x = 5
# y = 2

# print(x == y)
# print(x > y)
# print(x < 2)
# print(x != y)
# print(x <= y)  #  both the conditions are false --> false
# print(x >= y)  # at least one condition is true --> true

    # 4) Membership Operator:-
        # 1) in
        # 2) not in
# str1 = "Apple"

# print('l' in str1)
# print('A' in str1)
# print('E' in str1)

# l1 = ['A', 23, 45.5, 9-7j, 100, 'Apple']
# print(100 in l1)

# tup1 = (1, 2, 3, 4, 5, 6)
# print(23 not in tup1)

# set1 = {4, 5, 6, 7, 3, 2, 4, 5}
# print(4 in set1)

    # 5) Identity Operator:-
# m =  100
# n = 1000
# print(m is n)
# print(id(m))
# print(id(n))

# x = 'Apple'

# y = 'apple'.title()


# print(x)
# print(id(x))

# print(y)
# print(id((y)))

# print(x is y)


    # 6) ternary Operator:-
# balls = "yellow"

# result = "balls are green" if balls == "green" else "balls are yellow"
# print(result)

# x = 15
# y = 100

# result = f"{x} is greater" if x > y else f'{y} is greater'
# print(result)

# age = int(input("Enter your age: "))

# eligibility = "you are not eligible" if age < 18 else "you are eligibile"

# print(eligibility)


# if age >= 0 ---> please enter a valid age.
# if age < 18 ---> please apply after few years.
# if age == 18 ---> congrats..! you have just turned 18 and you are eligible.
# if age > 18 and age < 45 ---> "you are eligible, get your voting card soon"
# if age > 45  and age <60 ----> "hurry..! you are already late to get voting card"
# if age > 60 ----> "Please take rest..! No need to vote."

# age = int(input("Enter your age: "))

# result = "please enter a valid age" if age <= 0 else "please apply after few years" if age < 18 else "congrats..! you have just turned 18 and you are eligible." if age == 18 else "you are eligible, get your voting card soon" if age > 18 and age <= 45 else "hurry..! you are already late to get voting card" if age >45 and age <= 60 else "Please take rest..! No need to vote."

# print(result)

###########################################################

    # 7) Bitwise Operator:-
    
# print(23 & 45)   #5
# print(bin(23))
# print(bin(45))
# print(bin(5))


# print(56 & 89)
# print(bin(56))
# print(bin(89))
# print(bin(24))


# print(23 | 45)

# print(bin(23))
# print(bin(45))
# print(bin(63))


# print(56 | 89)

# print(bin(56))
# print(bin(89))
# print(bin(121))


# print(23 ^ 45)

# print(bin(58))



# print(56 ^ 89)

# print(int("1100001", 2))  97

# print(int('11111110', 2))


# print(10 >> 1)

# print(20 >> 1)

# print(56 >> 1)

# print(56 >> 1)
# print(bin(56))
# print(int("11100", 2))


# print(int('1110', 2))

print(56 << 3)

print(int('1110000', 2))
