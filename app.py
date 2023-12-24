import math

# Type cpnversion

# birth_year="1999"
# print(type(birth_year))
# age=2019-int(birth_year)
# print(type(age))
# print(age)

# String
# name="Rup Kumar Sarkar"

# print(name[-1])

# To get 0 to 5 chracter
# print(name[0:5])

# print(name.upper())
# print(name.title())
# print(name.find('u'))
# print(name.replace('Sarkar','Das'))




# Math Function

# x=2.9
# print(round(x))
# print(math.floor(x))
# print(abs(-5555))




# if-else
# x=2
# if(x==2):
#     print("true")
# else:
#     print("false")




# ******Ambiguity is the reason for learning programming language instead of Simple english or other language

# speed_of_light=299792458
# cycles_per_second=200000000 #2.7GHz
# print(speed_of_light/cycles_per_second)






# String concatenation

# name='Rup'

# print (name+'kumar')



# Extract link from page



# s='udacity'
# t='bodacious'
# Write a python code that prints out udacious without using any quote characvters

# print(s[:3]+t[4:])

# Assume text is a variable that holds a string.Write pthon code that prints out the position of the first occurrance of 'hoo' in the value of text, or -1 if it does not occur at all

# print('text'.find('hoo'))

#find 2nd r in text
# text="rup kumar"

# print(text.find('r',text.find('r')+1))
# i=1
# while i!=10 :
#     i=i+1
#     print(i)

# find median of three number






# def biggestOfTwo(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# def median(a, b, c):
#     result = biggestOfTwo(a, b)

#     if result > c:
#         return c
#     else:
#         return result

# print(median(2, 6, 8))


# Given your Birthday and the current date,calculate your age in days

# from datetime import datetime, date

# def calculate_age(birth_year):
#     # Get the current year
#     current_year = date.today().year

#     # Calculate the age
#     age = current_year - birth_year

#     return age

# # Example usage
# birth_year = int(input("Enter your birth year (YYYY): "))

# age = calculate_age(birth_year)
# print("Your age is:", age)


# Define a procedure ,replace spy,that takes a its input a list of three numbers and modifies the vaue of the third elements in the input list to be one more than its previous value

# spy=[0,0,7]
# x=spy
# spy[2]=x[2]+1
# print (spy,x)

#print su of numbers





# def sum_list(p):
#     sum = 0
#     for e in p:
#         sum += e
#     return sum

# p = [2, 5, 7, 8]
# result = sum_list(p)
# print(result)




# pop operation

# p=[2,6,5,4,8]
# x=p.pop()
# p.append(9)
# print(x)
# print(p)

# web Scripping

# step:
# 1.Load webite
# 2.Parst Html Data
# 3.Extract tidy data
# 4.Transform  data into required format


# define procedure ,mae hashtabletht tkes as input a number  n buckets amnd outputs an empty hash table with n buckets empt uckets

# def make_hashtable(nbuckets):
#     i = 0
#     table = []

#     while i < nbuckets:
#         table.append([])
#         i = i + 1

#     return table

# print(make_hashtable(3))


# def make_hashtable(nbuckets):
#     table = []

#     for i in range(nbuckets):
#         table.append([])

#     return table

# print(make_hashtable(3))


# index
# l=[29,45,6,7,4]

# print(l.index(7))


# Dictionary

# elements={}

# elements['A']={'name':'Apple','wt':'2kg'}
# elements['O']={'name':'Orange','wt':'6kg'}
# print(elements['A']['name']+">"+elements['A']['wt'])


# check palindrome

# def isPalindrome(s):
#     n = len(s)
#     l = 0

#     if s == "":
#         return True
#     else:
#         if s[0] == s[n-1]:
#             return isPalindrome(s[l+1:n-1])
#         else:
#             return False

# print(isPalindrome("acccdcca"))



# fibonacci number
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(5))





