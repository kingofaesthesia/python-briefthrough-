# user_name = input("Please tell us your name; ")
# print(f"Hi,Welcome {user_name}!")

# #More Booleans...
# x is y ---- # x is the same as y
# x is not y ---- # x is not the same as y

#Calculating the gross-pay for a user by provided parameters for their Hours and Rate.
#Handling exceptional errors.
#Adding conditional flows.
# try:
#     hours = int(input("Enter Hours; "))
#     rate = float(input("Enter Rate; "))
#     if hours > 40:
#         gross_pay = hours * rate * 1.5
#     else:
#         gross_pay = hours * rate

#     print(f"The gross pay for {hours} hours and {rate} rate is {gross_pay}.")
# except ValueError:
#     print("Invalid Input\n"
#           f"Try numeric inputs.")

# #Building a Grade Checker System that collects and measures inputs from (0.0 - 1.0)
# try:
#     score = float(input("Enter a grade between 0.0 and 1.0 to get an Alphabet Score!\n ; "))
#     if score > 0.0 and score < 1.01:
#         # continue
#         if score == 0.9:
#             print("A")
#         elif score >= 0.8:
#             print("B")
#         elif score >= 0.7:
#             print("C")
#         elif score >= 0.6:
#             print("D")
#         elif score >= 0.5:
#             print("E")
#         elif score <= 0.4:
#             print("F")
#         else:
#             print("Invalid Range.")
#     else:
#         print("Out of Range\n"
#               f"Try inputing from ranges 0.0 upward(ends at 1.0)")
# except ValueError:
#     print("Error, try numeric values(decimals preferably.)")

# def compute_pay():
#     try:
#         hours = int(input("Enter Hours; "))
#         rate = float(input("Enter Rate; "))
#         if hours > 40:
#             gross_pay = hours * rate * 1.5
#         else:
#             gross_pay = hours * rate
#         print(f"The gross pay for {hours} hours and {rate} rate is {gross_pay}.")
#     except ValueError:
#         print("Invalid Input\n"
#             f"Try numeric inputs.")

# compute_pay()

# def compute_pay(a,b):
#         if a > 40:
#             pay = a * b * 1.5
#         else:
#             pay = a * b
#         return pay

# print(compute_pay(29,6.5)

# word = 'banana'
# count = 0
# for letter in word:
#    if letter == str('n'):
#       count = count + 1
# print(count)

# class Letter_counter:
#     def __init__(self,word,letter):
#         self.word = word
#         self.letter = letter

#     def calculate_alp(self,word,letter):
#         word = self.word
#         count = 0
#         for letter in self.word:
#             if self.letter == str(letter):
#               count += 1
#         return count

#     def display_details(self):
#         return f"Your word is {self.word} and your letter is {self.letter}."


# my_num = Letter_counter('banana','a')
# print(my_num.display_details())
# print(my_num.calculate_alp('banana','a'))

# def letter_checker(word,letter):
#      count = 0
#      for i in word:
#         if i == str(letter):
#            count += 1
#      return count

# print(letter_checker('banahahahana','a'))

# ----------Data Structures = Lists,Tuples,Arrays and Dictionaries.------------------------------------------------#

#More String,Lists and Files Built-In functions.
# startswith() Returns either True or False
# endswith() Returns either True or False
# find() Specify a position to start looking.
# open() Opens a specific file (txt).
# close() Closes an opened file (txt).
# exit() Terminate the program.
# extend() Takes a list as an argument and appends all items into a specific list.
# remove() Removes an item from a list.
# sort()/list.sort(Reverse=True) Arrange items in a list in ascending order/descending order.
# del() Deletes an item in a list.
# pop() Temporary removes items from a list.
# sum() Adds up the sum of each integer in a given list.
# len() Counts the number of items in a list.
# min() Finds the maximum integer in a list.
# max() Finds the minimum integer in a list.
# list() Converts strings to a list of characters.
# split() Split items in a list.
# join() Combine items to a given list.
# delimeter() A symbol used to seperate words. e.g ;(-) The hyphen.
# list() Used to convert a string into a list.
# zip() Used to combine two or more sequence into a sequence
# dict()
# values()
# items()
# get('key','default value')
# lower()
# sorted()
# reversed()
# punctuation()
# translate()
# tuple()

# def chop(a):
#     return a[1:-1]
# list = [0,1,3,4,5,5,6,8]

# print(chop(list))

# def middle(a):
#     return a[0:-1]
# list = [0,1,3,4,5,5,6,8]
# print(middle(list))

# print(help(type(list)))

#Writing a program that collects integric inputs,appends them into a list and finally,prints out the minimum and maximum value in it.
# empty_list = []
# while True:
#     num = input("Enter a number; ").title()
#     if num == "Done":
#        break
#     value = int(num)
#     empty_list.append(value)
# print(f"{empty_list}\n"
#       f"Minimum Value ; {min(empty_list)}\n"
#       f"Maximum Value ; {max(empty_list)}")

# #Calculating the number of times a letter appears in a dictionary using loops and conditions.
# word = 'boogie'
# d = dict()
# for i in word:
#     if i not in d:
#        d[i] = 1
#     else:
#       d[i] = d[i] + 1
# print(d)

#You can’t modify the elements of a tuple, but you can replace one tuple with another:
# t = tuple('a',)
# t = ('A',) + t[1:]
# print(t)

# #Splitting words in a text.
# text = 'How are you?'
# split_list = text.split() #Splits elements in list into words.
# print(split_list)
# >>> ['How','are','you?'}


# One of the unique syntactic features of the Python language is the ability to have
# a tuple on the left side of an assignment statement. This allows you to assign more
# # than one variable at a time when the left side is a sequence.
# m = [ 'have', 'fun' ]
# (x, y) = m # Omitting the parentheses has an equally valid syntax.
# print(x)
# >>>'have'
# print(y)
# >>>'fun'

#Tuples also allow us to swap  the values of two variables in a simple syntax, e.g;
# a, b = b, a

# The number of variables on the left and the number of values on the right must be
# the same,else it gives the exception;  ValueError

# addr = 'monty@python.org'
# uname, domain = addr.split('@') #Remove the '@' symbol and split the remaining elements into two.
# The return value from split is a list with two elements; the first element is assigned
# to uname, the second to domain.
# print(uname)
# >>>monty
# print(domain)
# >>>python.org

# Regex(Regular Expressions)
# import re
# re.search() '^'- Beginning of a line.
# re.findall() '\S+key\S+' Search for any word with 'key's' specific character.
# ˆ Matches the beginning of the line.
# $ Matches the end of the line.
# . Matches any character (a wildcard).
# \s Matches a whitespace character.
# \S Matches a non-whitespace character (opposite of \s).
# * Applies to the immediately preceding character(s) and indicates to match zero or more times.
# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.
# + Applies to the immediately preceding character(s) and indicates to match one or more times.
# +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”
# ? Applies to the immediately preceding character(s) and indicates to match zero or one time.
# ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.
# [aeiou] Matches a single character as long as that character is in the specified set.
# In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
# [a-z0-9] You can specify ranges of characters using the minus sign. This example
# is a single character that must be a lowercase letter or a digit.
# [ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
# ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
# \b Matches the empty string, but only at the start or end of a word.
# \B Matches the empty string, but not at the start or end of a word.
# \d Matches any decimal digit; equivalent to the set [0-9].
# \D Matches any non-digit character; equivalent to the set [ˆ0-9]
# s.count(substr) Counts the number of occurences of a substring
# s.find(substr) Finds index of the first occurence of a substring, or -1
# s.rfind(substr) Finds index of the last occurence of a substring, or -1
# s.index(substr) Like find, except ValueError is raised if not found
# s.rindex(substr) Like rfind, except ValueError is raised if not found
# s.startswith(substr) Returns True if string starts with a given substring
# s.endswith(substr) Returns True if string ends with a given substring
# s.replace(substr, replacement) Returns a string where occurences of one string are replaced by another
# s.lower() Change all letters to lowercase
# s.upper() Change all letters to uppercase
# s.capitalize() Change the first character to upper case and change the rest to lower case
# s.title() Change to titlecase
# s.swapcase() Change all uppercase letters to lowercase, and vice versa



# Search for lines that start with 'From' and # Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^From:'/ '^F..m', line): '^' line's that start with 'Word'., '..' Starts with F and two chharacters before 'm'.
#      print(line)

#Example 2
# # Search for lines that start with From and have an at sign
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^From:.+@', line):  # "Keyword :.+ 'sign'"
#     print(line)
# >>> From: stephen.marquard@uct.ac.za #Matches From with @ sign.


# # Find all words in this string that starts from "@"(email-addresses)
# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s) / non whitespace character - '@' sign - another non whitespace character.
# print(lst)
# >>> ['csev@umich.edu', 'cwen@iupui.edu']

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^X\S*: [0-9.]+', line): #
#    print(line)
#Translating this, we are saying, we want lines that start with X-, followed by zero
# or more characters (.*), followed by a colon (:) and then a space. After the
# space we are looking for one or more characters that are either a digit (0-9) or
# a period [0-9.]+. Note that inside the square brackets, the period matches an
# actual period (i.e., it is not a wildcard between the square brackets).

#Extracting the numbers.
# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

# import re
# hand = open('mbox-short.txt')
# for line in hand:
	# line = line.rstrip()
	# x = re.findall('^X\S*: ([0-9.]+)', line)
	# if len(x) > 0:
		# print(x)

# ^From .* [0-9][0-9]:
# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
#OR
# The translation of this regular expression is that we are looking for lines that start
# with From (note the space), followed by any number of characters (.*), followed by
# a space, followed by two digits [0-9][0-9], followed by a colon character. This is
# the definition of the kinds of lines we are looking for.

# import re
# hand = open('mbox-short.txt')
# for line in hand:
	# line = line.rstrip()
	# x = re.findall('^From .* ([0-9][0-9]):', line)
	# if len(x) > 0:
	#    print(x)

# import re
# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+',x)
# print(y)
# >>>$10.00

#Networking programs on the Internet with sockets for Python.

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#       break
#     print(data.decode(),end="")

# mysock.close()

# #Making a multiplication table with a for loop;
# time = 8
# for i in range(12):
#     print(f"{time} multiplied by {i} is equal to {time * i}")

# #Using the join method to concatenate lots of strings
# a="first"
# b="second"
# print(a+b)
# print(" ".join([a, b, b, a]))

# #Summing up a set of numbers in a list.
# s=0
# for i in [0,1,2,3,4,5,6,7,8,9]:
#     s = s + i
# print("The sum is", s) #45

# #Using format strings
# from math import sqrt, log
# l=[1,3,65,3,-1,56,-10]
# for x in l:
#     if x < 0:
#         continue
#     print(f"Square root of {x} is {sqrt(x):.3f}") #:.3f in three floats.
#     print(f"Natural logarithm of {x} is {log(x):.4f}") #:. 4f in four floats.

#Dice.py

# numbers = [1,2,3,4,5,6]
# time = [1,2,3,4,5,6]

# for num in numbers:
#     print(f"{num} in range({time}")
#     if num < 0:
#         for i in time:
# #             print(f"{num},{i}")

# Dice = [1,2,3,4,5,6]
# time = range(6)

# for i in Dice:
#     for i in time:
#         if (i + time) == 5:
#             print(f"{i} ,{time}")

# numbers = [1,2,3,4,5,6]
# for i in numbers:
#     print(i)


# #Functions
# def double(x):
#     "This function multiplies its argument by two." #Python saves the docstring for documentation.
#     return x*2
# print(double(4), double(1.2), double("abc"))

# #Accessing Saved Docstrings.
# print("The docstring is:", double.__doc__)
# help(double)   # Another way to access the docstring

# def sum_of_squares(a, b):
#     "Computes the sum of arguments squared"
#     return a**2 + b**2
# print(sum_of_squares(3, 4))


# def sum_of_squares(lst):
#     "Computes the sum of squares of elements in the list given as parameter"
#     s=0
#     for x in lst:
#         s += x**2
#     return s
# #The arguments were bring wrapped into a list.
# print(sum_of_squares([-2])) #-2 * -2 = 4
# print(sum_of_squares([-2,4,5])) # -2 * -2 + 4 * 4 + 5 * 5 = 45

#  This works perfectly!
# There is however some extra typing with the brackets around the lists.
# #  Let's see if we can do better:

# #Argument Packing.
# def sum_of_squares(*n): #(*) Accepts mulgtiple parameters.
#     "Computes the sum of squares of arbitrary number of arguments"
#     ans=0
#     for i in n:
#         ans = ans + i**2
#     return ans

# lst=[1,5,8]

# print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))

# print(sum_of_squares(-2)) #4
# # print(sum_of_squares(-2,4,5)) # 45


# #Argument Unpacking
# There is also syntax for argument unpacking.
# It has confusingly exactly same notation as argument packing (star),
# but they are separated by the location where used.
# Packing happens in the parameter list of the functions definition,
# and unpacking happens where the function is called:

# lst=[1,5,8]
# print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# # print(sum_of_squares(lst))    # Does not work correctly


# print(1, 2, 3, end=' |', sep=' -*- ') # end with this " 1" and seperate them with " -*- "
# print("first", "second", "third", end=' |', sep=' -*- ') #Space sensitive


# Global variables(Variables Visibility)
# i=2
# def f():
#     global i
#     i=5       # rebind the global i variable #Take all instances of i and make them 5.
#     print(i)  # This will print 5
# f()
# print(i)      # This will print 5

# def number():            # outer function
#     n=2
#     def inside_num():        # inner function
#         #nonlocal n   #nonlocal n, makes all n variables = 20 # Without this nonlocal statement, (P.S : See it as; Not your average n, hehe)
#         n=20         # this will create a new local variable
#         print(n)
#     inside_num()   #Calling n as 2 because of it being an outer function.
#     print(n) #Call the initial n in the number() function, which is 2.

# #The main function running.
# number()
# # >>>>20
# # >>>>20 withhout 'nonlocal n' it gives 2

# The global and nonlocal statements are similar.
# The first will force a variable refer to a global variable,
# and the second will force a variable to refer to the variable in the nearest outer scope
# (but not the global scope).

# def triple(*n):
#     ans = 0
#     for i in n:
#        ans = ans + i*3
#        return f"triple of {i} is equal to {ans}."

# print(triple(5,6,7))

# def square(*n):
#     ans = 0
#     for i in n:
#         ans = ans + i**2
#         return f"square{i} = {ans}"
# # print(square(2))

# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     print(f"{square(i)},{triple(i)}")

# #Data Structures
# The generic form of a slice is sequence[first:last:step].
# If any of the three parameters are left out,
# they are set to default values as follows: first=0, last=len(L), step=1.
# So, for instance "abcde"[1:]=="bcde".
# The step parameter selects elements that are step distance apart from each other.


# We can assign values to elements of a list by indexing or by slicing. An example:
# L=[11,13,22,32]
# L[2]=10          # Changes the third element
# print(L)
# >>>[11, 13, 10, 32]

# # Or we can assign a list to a slice:
# L[1:3]=[4]
# print(L)
# >>>[11, 4, 32]

# #Zip function - zip()
# L1=[1,2,3]
# L2=["first", "second", "third"]
# print(zip(L1, L2))               # Note that zip does not return a list, like range
# print(list(zip(L1, L2)))         # Convert to a list

# Here's another example of using the zip function.

# days="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split() #Seperate each space character into a comma
																		  #and make it a single element,
# weathers="rainy rainy sunny cloudy rainy sunny sunny".split()
# temperatures=[10,12,12,9,9,11,11]
# for day, weather, temperature in zip(days,weathers,temperatures):
#     print(f"On {day} it was {weather} and the temperature was {temperature} degrees celsius.")

# # Or equivalently:
# #for t in zip(days,weathers,temperatures):
# #    print("On {} it was {} and the temperature was {} degrees celsius.".format(*t))
# >>>On Monday it was rainy and the temperature was 10 degrees celsius, e.t.c.


# #Using the enumerate() function;
# L=[1,2,98,5,-1,2,0,5,10]
# counter = 0
# for i, x in enumerate(L):
#     if x == 5:
#         counter += 1
#         if counter == 2:
#             break
# print(i)
# >>>7

# #Alternative syntaxes to Dictionary Creation
# dict([("key1", "value1"), ("key2", "value2"), ("key3", "value3")]) # list of items
# dict(key1="value1", key2="value2", key3="value3") #Tuples are hashable

# d={}
# d[2]="value"
# print(d)
# >>>{2: 'value'}

# # Dictionary object contains several non-mutating methods:
# d.copy()
# d.items()
# d.keys()
# d.values()
# d.get(k[,x])

# Some methods mutate the dictionary:
# d.clear()
# d.update(d1)
# d.setdefault(k[,x])
# d.pop(k[,x])
# d.popitem()

# Sets
# Set is a dynamic, unordered container.
# It works a bit like dictionary, but only the keys are stored.
# And each key can be stored only once.

# s={1,1,1}
# print(s)
# s=set([1,2,2,'a'])
# print(s)
# s=set()  # empty set
# print(s)
# s.add(7) # add one element
# print(s)
# >>>{1}
# >>>{1, 2, 'a'}
# >>>set()
# >>>{7}

# A more useful example of sets:
# s="mississippi"
# print(f"There are {len(set(s))} distinct characters in {s}")
# There are 4 distinct characters in mississippi
# The set provides the following non-mutating methods:

# s=set()
# s1=set()
# s.copy()
# s.issubset(s1)
# s.issuperset(s1)
# s.union(s1)
# s.intersection(s1)
# s.difference(s1)
# s.symmetric_difference(s1);

# s=set([1,2,7])
# t=set([2,8,9])
# print("Union:", s|t)
# print("Intersection:", s&t)
# print("Difference:", s-t)
# print("Symmetric difference", s^t)
# >>>Union: {1, 2, 7, 8, 9}
# >>>Intersection: {2}
# >>>Difference: {1, 7}
# >>>Symmetric difference {1, 7, 8, 9}
# There are also the following mutating methods:
# s.add(x)
# s.clear()
# s.discard()
# s.pop()
# s.remove(x)

# first, second = [4,5]
# a,b,c = "bye"
# print(c)
# d=dict(a=1, b=3)
# key1, key2 = d
# print(key1, key2)
# >>>e
# # >>>a b

# L=[ a**3 for a in range(1,11)]
# print(L)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# L=[ 100*a + 10*b +c for a in range(0,10)
#                     for b in range(0,10)
#                     for c in range(0,10)
#                     if a <= b <= c]
# print(L)
# >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23,]

# Similary a dictionary comprehension creates a dictionary:

# d={ k : k**2 for k in range(10)}
# print(d)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# And a set comprehension creates a set:

# s={ i*j for i in range(10) for j in range(10)}
# print(s)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27,]

# The map function gets a list and a function as parameters,
# and it returns a new list whose elements are elements of the original list transformed by the parameter function.
# For this to work the parameter function must take exactly one value in and return a value out.
# An example will clarify this concept:

# def double(x):
#     return 2*x
# L=[12,4,-1]
# print(map(double, L))
# >>><map object at 0x7fb81413ef60>

# The map function returns a map object for efficiency reasons.
# However, since we only want print the contents,
# we first convert it to a list and then print it:

# print(list(map(double,L)))
# >>>[24, 8, -2]

# s="12 43 64 6"
# L=s.split()        # The split method of the string class, breaks the string at whitespaces
#                    # to a list of strings.
# print(L)
# print(sum(map(int, L)))  # The int function converts a string to an integer

# #Lamda Functions
# The lambda expression has the form lambda param1,param2, ... : expression

# L=[2,3,5]

# print(list(map(lambda x : 2*x+x**2, L)))

# Filter Function
# def is_odd(x):
#     """Returns True if x is odd and False if x is even"""
#     return x % 2 == 1         # The % operator returns the remainder of integer division
# L=[1, 4, 5, 9, 10]
# print(list(filter(is_odd, L)))
# >>>[1,5,9]

# L=[1,2,3,4]
# from functools import reduce   # import the reduce function from the functools module
# reduce(lambda x,y:x+y, L, 0)
# >>>10

# If we wanted to get a product of all numbers in a sequence, we would use
# reduce(lambda x,y:x*y, L, 1)
# >>>24

# An iterable is an object whose elements can be gone through one by one using a for loop.
# Such as range(1,7)

# "--".join(["abc", "def", "ghi"])
# 'abc--def--ghi'
# L=[str(x) for x in range(100)]
# s=""
# for x in L:
#     s += " " + x    # Avoid doing this, it creates a new string at every iteration
# print(s)            # Note the redundant initial space
# print(" ".join(L))  # This is the correct way of building a string out of smaller strings

# >>> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
# >>>35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
# >>>67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
# >>>0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
# >>>34 35 36 37 38 39 40 41 42 43


#Classes
# class MyClass(object):
#     """Documentation string of the class"""

#     def __init__(self, param1, param2):
#         "This initialises an instance of type ClassName"
#         self.b = param1 # creates an instance attribute
#         c = param2      # creates a local variable of the function
#         # statements ...

#     def f(self, param1):
#         """This is a method of the class"""
#         # some statements

# class B(object):
#     def f(self):
#         print("Executing B.f")
#     def g(self):
#         print("Executing B.g")

# class C(B):
#     def g(self):
#         print("Executing C.g")

# x=C()
# x.f() # inherited from B
# x.g() # overridden by C

# The inheritance relation of two classes B and C can be tested with function issubclass:
# issubclass(C,B)==True but issubclass(B,C)==False
# Function isinstance(obj, cls) allows us to test whether an instance has type cls or has an ancestor class of type cls. Let’s create instances x=C() and y=B().
# Now we have isinstance(x,B)== isinstance(x,C)==isinstance(y,B)==True. But isinstance(y,C)==False.
# a=1 # This creates a class attribute


#World's simplest browser with Python.
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket protocols as parameters

# mysock.connect(('data.pr4e.org', 80)) #We connect the site we want to retrieve to Port 80

# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #r\n\rn as blank spaces(equivalent)
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:   #if reply ois less than 1 break the connection.
#        break
#     print(data.decode(),end='') #Decode the data and end with space.

# mysock.close()  #Close the connncetion.

# #Webpage
# HTTP/1.1 200 OK
# Date: Wed, 11 Apr 2018 18:52:55 GMT
# Server: Apache/2.4.7 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# #Text in document(body)
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# # encode() and decode() methods convert strings into bytes objects and back again
# The next example uses b'' notation to specify that a variable should be stored as
# a bytes object. encode() and b'' are equivalent

# >>> b'Hello world'
# b'Hello world'
# >>> 'Hello world'.encode()
# b'Hello world'

#Retrieving images via HTTPS.
# import socket
# import time


# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#    data = mysock.recv(5120)
#    if len(data) < 1: break
#    #time.sleep(0.25)
#    count = count + len(data)
#    print(len(data), count)

# picture = picture + data
# mysock.close()

# # Look for the end of the header (2 CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header length', pos)
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()

# #Output

# $ python urljpeg.py
# 5120 5120
# 5120 10240
# 4240 14480
# 5120 19600
# ...
# 5120 214000
# 3200 217200
# 5120 222320
# 5120 227440
# 3167 230607
# Header length 393
# HTTP/1.1 200 OK
# Date: Wed, 11 Apr 2018 18:54:09 GMT
# Server: Apache/2.4.7 (Ubuntu)
# Last-Modified: Mon, 15 May 2017 12:27:40 GMT
# ETag: "38342-54f8f2e5b6277"
# Accept-Ranges: bytes
# Content-Length: 230210
# Vary: Accept-Encoding
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: image/jpeg

#Retrieving webpages with the urllib (urllibrary)

# import urllib.request

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# Once the web page has been opened with urllib.urlopen, we can treat it like a
# file and read through it using a for loop.
# When the program runs, we only see the output of the contents of the file. The
# headers are still sent, but the urllib code consumes the headers and only returns
# the data to us.(Splendid)

#Output
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

#Retrieving Binary files(photos and videos) with urllib
# import urllib.request, urllib.parse, urllib.error
# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('cover3.jpg', 'wb')
# fhand.write(img)
# fhand.close()

# #In order to not run out of memory;
# import urllib.request, urllib.parse, urllib.error
# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
# fhand = open('cover3.jpg', 'wb')
# size = 0
# while True:
#    info = img.read(100000)
#    if len(info) < 1: break
# size = size + len(info)
# fhand.write(info)
# print(size, 'characters copied.')
# fhand.close()

# # Search for link values within URL input

# import urllib.request, urllib.parse, urllib.error
# import re
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# links = re.findall(b'href="(http[s]?://.*?)"', html)
# for link in links:
# print(link.decode())


# #Parsing HTML using the BeautifulSoup Library
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
# print(tag.get('href', None))

# #Output
# Enter - https://docs.python.org
# genindex.html
# py-modindex.html
# https://www.python.org/
# #
# whatsnew/3.6.html
# whatsnew/index.html
# tutorial/index.html
# library/index.html
# reference/index.html
# using/index.html
# howto/index.html
# installing/index.html
# distributing/index.html
# extending/index.html
# c-api/index.html
# faq/index.html
# py-modindex.html
# genindex.html
# glossary.html
# search.html
# contents.html
# bugs.html
# about.html
# license.html
# copyright.html
# download.htm

# #Using the BeautifulSoup library code to pull out specific tags
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
# # Look at the parts of a tag
# print('TAG:', tag)
# print('URL:', tag.get('href', None))
# print('Contents:', tag.contents[0])
# print('Attrs:', tag.attrs)


# #Using Web Services (XML and JSON)
# #Parsing XML
# import xml.etree.ElementTree as ET
# data = '''
# <person>
# <name>Chuck</name>
# <phone type="intl">
# +1 734 303 4456
# </phone>
# <email hide="yes" />
# </person>'''
# tree = ET.fromstring(data) #Converts all XML properties into a string.
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

# #Output
# Name: Chuck
# Attr: yes


# #Looping XML through nodes
# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
# <users>
# <user x="2">
# <id>001</id>
# <name>Chuck</name>
# </user>
# <user x="7">
# <id>009</id>
# <name>Brent</name>
# </user>
# </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
# for item in lst:
# print('Name', item.find('name').text)
# print('Id', item.find('id').text)
# print('Attribute', item.get('x'))

# #Output
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute

# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
# <users>
# <user x="2">
# <id>001</id>
# <name>Chuck</name>
# </user>
# <user x="7">
# <id>009</id>
# <name>Brent</name>
# </user>
# </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
# lst2 = stuff.findall('user')
# print('User count:', len(lst2))

# #Output
# User count: 2
# User count: 0

# #JSON (Javascript Object Notation)
# #Example
# {
# "name" : "Chuck",
# "phone" : {
# "type" : "intl",
# "number" : "+1 734 303 4456"
# },
# "email" : {
# "hide" : "yes"
# }
# }

# #Parsing JSON
# import json
# data = '''
# [
# { "id" : "001",
# "x" : "2",
# "name" : "Chuck"
# } ,
# { "id" : "009",
# "x" : "7",
# "name" : "Brent"
# }
# ]'''
# info = json.loads(data)
# print('User count:', len(info))
# for item in info:
# print('Name', item['name'])
# print('Id', item['id'])
# print('Attribute', item['x'])

# #Output
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7


# #API's (Application Programming Interface)
# #Application 1: Google Geocoding Web Service

# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl
# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
# if api_key is False:
# api_key = 42
# serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# while True:
# address = input('Enter location: ')
# if len(address) < 1: break
# parms = dict()
# parms['address'] = address
# if api_key is not False: parms['key'] = api_key
# url = serviceurl + urllib.parse.urlencode(parms)
# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters')
# try:
# js = json.loads(data)
# except:
# js = None
# if not js or 'status' not in js or js['status'] != 'OK':
# print('==== Failure To Retrieve ====')
# print(data)
# continue
# print(json.dumps(js, indent=4))
# lat = js['results'][0]['geometry']['location']['lat']
# lng = js['results'][0]['geometry']['location']['lng']
# print('lat', lat, 'lng', lng)
# location = js['results'][0]['formatted_address']
# print(location)

# #Output
# $ python3 geojson.py
# Enter location: Ann Arbor, MI
# Retrieving http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42
# Retrieved 1736 characters

# {
# "results": [
# {
# "address_components": [
# {
# "long_name": "Ann Arbor",
# "short_name": "Ann Arbor",
# "types": [
# "locality",
# "political"
# ]
# },
# {
# "long_name": "Washtenaw County",
# "short_name": "Washtenaw County",
# "types": [
# "administrative_area_level_2",
# "political"
# ]
# },
# {
# "long_name": "Michigan",
# "short_name": "MI",
# "types": [
# "administrative_area_level_1",
# "political"
# ]
# },
# {
# "long_name": "United States",
# "short_name": "US",
# "types": [
# "country",
# "political"
# ]
# }
# ],
# "formatted_address": "Ann Arbor, MI, USA",
# "geometry": {
# "bounds": {
# "northeast": {
# "lat": 42.3239728,
# "lng": -83.6758069
# },
# "southwest": {
# "lat": 42.222668,
# "lng": -83.799572
# }
# },
# "location": {
# "lat": 42.2808256,
# "lng": -83.7430378
# },
# "location_type": "APPROXIMATE",
# "viewport": {
# "northeast": {
# "lat": 42.3239728,
# "lng": -83.6758069
# },
# "southwest": {
# "lat": 42.222668,
# "lng": -83.799572
# }
# }
# },
# "place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
# "types": [
# "locality",
# "political"
# ]
# }
# ],
# "status": "OK"
# }
# lat 42.2808256 lng -83.7430378
# Ann Arbor, MI, USA

#OOP
# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print (stuff[0])
# print (stuff.__getitem__(0))
# print (list.__getitem__(stuff,0))

# class PartyAnimal:
# x = 0
# def __init__(self):
# print('I am constructed')
# def party(self) :
# self.x = self.x + 1
# print('So far',self.x)
# def __del__(self):
# print('I am destructed', self.x)
# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains',an)

# # When this program executes, it produces the following output:
# # I am constructed
# So far 1
# So far 2
# I am destructed 2
# an contains 42

#Multiple Instances
# class PartyAnimal:
# x = 0
# name = ''
# def __init__(self, nam):
# self.name = nam
# print(self.name,'constructed')
# def party(self) :
# self.x = self.x + 1
# print(self.name,'party count',self.x)
# s = PartyAnimal('Sally')
# j = PartyAnimal('Jim')
# s.party()
# j.party()
# s.party()

# #Output
# Sally constructed
# Jim constructed
# Sally party count 1
# Jim party count 1
# Sally party count

#Inheritance
# from party import PartyAnimal
# class CricketFan(PartyAnimal):
# points = 0
# def six(self):
# self.points = self.points + 6
# self.party()
# print(self.name,"points",self.points)
# s = PartyAnimal("Sally")
# s.party()
# j = CricketFan("Jim")
# j.party()
# j.six()
# print(dir(j))

# #Output
# Sally constructed
# Sally party count 1
# Jim constructed
# Jim party count 1
# Jim party count 2
# Jim points 6
# ['__class__', '__delattr__', ... '__weakref__',
# 'name', 'party', 'points', 'six', 'x']

#Databases and SQL (SQLite)

#CodewithMosh
#Data Structures
#Lists
# zero_5 = [0] * 5
# print(zero_5)
# >>>[0, 0, 0, 0, 0]

# numbers = list(range(20))
# print(numbers[::2])
# >>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#All even numbers
# print(numbers[::-1])
#Ought to print numbers in reverse order

# num_list = [1,2,3,4,5,5,7,5,9]
# first,second,third,fourth,*other,last = num_list   #Note the asterisks before the other
# print(first,last)
# >>>1 9
# print(other)
# >>>[5, 5, 5, 5]   #Note that it presented all other values inside a list.
# print(other[2])
# >>>7

# items = ["hair","comb","brush"]
# for index,item in enumerate(items):
#     print(index,item)
# >>>0 hair
#    1 comb
#    2 brush

# letters = ["a","b","c"]
#Add
# letters.append("d")
# letters.insert(4,"e") #Takes two arguments(Position,Object)

#Remove
# letters.pop() #Without any argument, this removes the last item in a list.
# letters.pop(0) #Takes a postion as argument.
# del letter[1:3] #Takes a index, also takes slices in range.
# letters.clear() #Remove all items in a list

# letters = ["a","b","c","d"]
# letters.index("b")  #Get the index of item "b"
# letters.count("a") #How many times does the letter "a" appear in the list
###If item not in list, it returns a Traceback Error
# if "e" in letters:
	# print(letters.index("e"))

# items = [
#     ("Product1",10)
#     ("Product2",5)
#     ("Product3",7)
#     ("Product4",2)
#     ("Product5",3)
# ]

# items.sort()
# print(items)
# items.sort(Reverse=True)
# print(items)
# print(items.sorted())  #Prints the previous form of the sorted list.

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

#Using lambda functions
# key=lambda parameters:expression
# items = [
#     ("Product1",10),
#     ("Product2",5),
#     ("Product3",7),
#     ("Product4",2),
#     ("Product5",3)
# ]

# items.sort(key=lambda item: item[1])
# print(items)
# >>>[('Product4', 2), ('Product5', 3), ('Product2', 5), ('Product3', 7), ('Product1', 10)]

# items = [
#      ("Product1",10),
#      ("Product2",5),
#      ("Product3",7),
#      ("Product4",2),
#      ("Product5",3),
# ]
# for item in items:
#     print(item[1])
# >>>10
# 5
# 7
# 2
# 3
#Using the map and lambda function

# x = list(map(lambda item: item[1],items)) #Map takes two arguments ;
# a lambda function and an iterable like the 'items' list.
# print(x)
# >>><map object at 0x00000199B001B820>
#When coverted to a list
# >>>[10, 5, 7, 2, 3]

# items = [
#      ("Product1",10),
#      ("Product2",5),
#      ("Product3",7),
#      ("Product4",2),
#      ("Product5",3),
# ]
# filtered = list(filter(lambda item: item[1] >= 5,items))
# print(filtered)
# >>><filter object at 0x0000023259E0B820>
#When converted to lists
# >>>[('Product1', 10), ('Product2', 5), ('Product3', 7)]

#List Comprehensions (map and filter alternatives)
# items = [
#      ("Product1",10),
#      ("Product2",5),
#      ("Product3",7),
#      ("Product4",2),
#      ("Product5",3),
# ]
# prices = [expression iterable for loop]
# prices = [item[1] for item in items]
# print(prices)
# >>>[10, 5, 7, 2, 3]

# filtered = [expression iterable for loop and the condition]
# filtered = [item for item in items if item[1] >= 5] #Super Case Sensitive
# print(filtered)
# >>>[('Product1', 10), ('Product2', 5), ('Product3', 7)]

# item1 = [1,2,3]
# item2 = [100,200,300]
# sol = list(zip("abcdefght",item1,item2))
# print(sol)

# >>><zip object at 0x000002419DBEBAC0>
#After converting to list
# >>>[(1, 100), (2, 200), (3, 300)]
# >>>[('a', 1, 100), ('b', 2, 200), ('c', 3, 300)] #Super argument sensitive


#Stack Structure
# browsing_session = []
# browsing_session.append(1)
# print(browsing_session)
# browsing_session.pop()

# if not browsing_session: #If items still exists in browsing_session lists,
# print the last items from the back.
#    print(browsing_session[-1])

#Queue Structure
# from collections import deque
# contain = deque([])
# contain.append(1)
# contain.append(2)
# contain.append(3)
# contain.append(4)
# print(contain)
# # >>>deque([1, 2, 3, 4])
# contain.popleft()
# print(contain)
# >>>deque([1, 2, 3, 4])
# >>>deque([2, 3, 4])

#Tuples Structure
#Tuples are read only structures(they cannot be modified)
#They canm be unpacked too
# tup = (1,2,3)
# x,y,z = tup
# print(x)
# >>>1
# tup = 1,2,3
# print(type(tup))
# tup1 = 1,
# print(type(tup1))
# >>><class 'tuple'>
# >>><class 'tuple'>

#Swapping Variables
# x = 10
# y = 11

# x,y = y,x

# z = x
# x = y
# y = z

# print("x",x)
# print("y",y)
# >>>x 11
# >>>y 10

#Array Structure
# from array import array

# container = array("i",[1,2,3,4]) #Takes two arguments ; TypeCode and an iterable(lists)
# container.append(5)
# print(container)
# >>>array('i', [1, 2, 3, 4, 5])

#Sets Structure
#Sets are collections with no duplicates

# numbers = [1,1,1,2,3,4,5]
# setter = set(numbers)
# setter2 = {1,6,7}
# print(setter)
# >>>{1, 2, 3, 4, 5}  #They are reperesnted with the curly braces {}
# setter.add(5)
# setter.remove(1)
# print(setter)
# >>>{2, 3, 4, 5}

#Mathematical operations for sets

# numbers = [1,1,1,2,3,4,5]
# setter = set(numbers)
# setter2 = {1,6,7}
# print(setter ^ setter2)
# >>>{2, 3, 4, 5, 6, 7}
# print(setter & setter2)
# >>>{1}
# print(setter - setter2)
# >>>{2, 3, 4, 5}
# print(setter | setter2)
# >>>{1, 2, 3, 4, 5, 6, 7}

#Dictionaries Structure
# point = {"x":1,"y":2}  #This is a dictionary, a collection of key,value pairs.
# point = dict(x=1,y=2)
# point[3]     #Doesn't index by numerical values
# point["z"] = 3
# print(point)
# >>>{'x': 1, 'y': 2, 'z': 3}
# del point["x"]
# print(point)
# >>>{'y': 2, 'z': 3}
#Getting and assigning items in a dictionary.
# points.get("a",0)
# print(points)  #This takes two arguments, the key to find and
# an already assigned or connstatnt variables that shows when the key is not found in the dict.
#Looping through dictionaries
# point = {"x":1,"y":2,"z":3}
# for item in point:
	# print(item)
# >>>x
#    y
#    z
# for key in point.items():
#     print(key)
# # >>>('x', 1)  #Returns a tuple contain each key and value pair in the dictionary
#    ('y', 2)
# #    ('z', 3)
# point = {"x":1,"y":2,"z":3}
# for key,value in point.items():
#     print(key,value)        #This is a cleaner and more pythonic way of looping through dicts.
# # >>>

#Dictionary Comprehension
# Remember lists comprehensions.
# [expression iterable for loop]

# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)
# # >>>[0, 2, 4, 6, 8]

# values = [x*2 for x in range(5)]
# print(values)
# >>>[0, 2, 4, 6, 8]  #Perfect, same but more pythonic.

#Comprehensions for Dictionaries
# val = {x:x*2 for x in range(5)}
# print(val)
# >>>{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Comprehension for Tuples
# val = (x*2 for x in range(5))
# print(val)
# >>><generator object <genexpr> at 0x0000027E26951FC0>  ???
# from sys import getsizeof
# val = (x*2 for x in range(10000000))  #Items in a generator are only visible when iterated.
# for x in val:
#     print(x)
# >>>0
# >>>2
# >>>4
# >>>6
# size = getsizeof(val)
# print("gen; ",size)
# >>>gen;  104   #Gen size always constant.
# lst = [x*2 for x in range(100)]
# size2 = getsizeof(lst)
# print(size2)
# >>>920
# print(len(lst))
# >>>100
# print(len(val))
# >>>TypeError: object of type 'generator' has no len()

#Unpacking Operator
# lst = [1,2,3,4,5]
# print(lst)
# >>>[1, 2, 3, 4, 5]
#To Unpack;              #We use a single asterisk to unpack for lists.
# print(*lst)
# >>>1 2 3 4 5
#We can also unpack multiple items.
# first = [1,2,3,4]
# second = ["a","b","c","d"]
#Let's unpack;
# container = [*first,*second]
# print(container)
# >>>[1, 2, 3, 4, 'a', 'b', 'c', 'd']
# container2 = [*first,*second,*"Wassup"]
# print(container2)
# >>>[1, 2, 3, 4, 'a', 'b', 'c', 'd', 'W', 'a', 's', 's', 'u', 'p']

#Unpacking a Dictionary;
# store1 = dict(x=1,y=2,z=3)
# store2 = dict(x=10,a=3,b=4)
# #Unpacking a dictionary takes to asterisks (**)
# combined = dict(**store1,**store2,d=6)
# print(combined)
# >>>TypeError: dict() got multiple values for keyword argument 'x'
# store1 = {"x":1,"y":2,"z":3}
# store2 = {"x":10,"a":3,"b":4}
# #Unpacking a dictionary takes to asterisks (**)
# combined = {**store1,**store2,"d":6}
# print(combined)
#Note that when repeating keys, only the last of it is being printed in the dict.("x":1 was ommitted)
# >>>{'x': 10, 'y': 2, 'z': 3, 'a': 3, 'b': 4, 'd': 6}
# from pprint import pprint
# sentence = "This is a common interview question"
# letr_freq = {}
# for letr in sentence:
#     if letr in letr_freq:
#         letr_freq[letr] += 1
#     else:
#         letr_freq[letr] = 1
# print(letr_freq)
# >>>{'T': 1, 'h': 1, 'i': 5, 's': 3,
# ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2,
#  'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1,
# 'w': 1, 'q': 1, 'u': 1}
#Let's print it in a better way with the pprint function.(Pretty Print)
# pprint(letr_freq,width=1)
# >>>{' ': 5,
#  'T': 1,
#  'a': 1,
#  'c': 1,
#  'e': 3,
#  'i': 5,
#  'm': 2,
#  'n': 3,
#  'o': 3,
#  'q': 1,
#  'r': 1,
#  's': 3,
#  't': 2,
#  'u': 1,
#  'v': 1,
#  'w': 1}
# sentence = "This is a common interview question"
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
#Let's Sort 'char_freq'
# sort_char_freq = sorted(char_freq.items())
# pprint(sort_char_freq)
# >>>[(' ', 5),
#  ('T', 1),
#  ('a', 1),
#  ('c', 1),
#  ('e', 3),
#  ('h', 1),
#  ('i', 5),
#  ('m', 2),
#  ('n', 3),
#  ('o', 3),
#  ('q', 1),
#  ('r', 1),
#  ('s', 3),
#  ('t', 2),
#  ('u', 1),
#  ('v', 1),
#  ('w', 1)]
#Still not correctly sorted
#Let's make a lambda function.
# sentence = "This is a common interview question"
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# sort_char_freq = sorted(char_freq.items() ,key=lambda kv: kv[1], reverse=True)
# pprint(sort_char_freq)
# >>>[('i', 5),
#  (' ', 5),
#  ('s', 3),
#  ('o', 3),
#  ('n', 3),
#  ('e', 3),
#  ('m', 2),
#  ('t', 2),
#  ('T', 1),
#  ('h', 1),
#  ('a', 1),
#  ('c', 1),
#  ('r', 1),
#  ('v', 1),
#  ('w', 1),
#  ('q', 1),
#  ('u', 1)]
#Classes
#A class is a blueprint for creating new objects.
#An object is an instance of a class.

# class Point:
#     '''First Method with the __init__ method is caled a constructor.'''
#     default_ink = "pencil"
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __eq__(self,other):
#         return self.x == other.x and self.y == other.y
#     def __str__(self):
#         return f"{self.x},{self.y}"
#     def __gt__(self,other):
#         return self.x > other.x and self.y > other.y
#     def __add__(self,other):
#         return Point(self.x + other.x ,self.y + other.y)

#     @classmethod    #This makes a method particularly for the class.
#     def zero(cls):
#         return cls(0,0)

#     def draw(self):
#         print(f"Point; {self.x},{self.y}")

# r_point = Point(1,2)
# r_point.draw()
# >>>Point; 1,2
# print(r_point.default_ink)
# >>>pencil
# print(Point.default_ink)
# >>>pencil
#Note that if changed:
# Point.default_ink ="Pen"
#All corresponding instances of the Class also changes.
# print(Point.default_ink)
# >>>Pen
# print(r_point.default_ink)
# >>>Pen
# inst_check = isinstance(r_point,Point)
# print(inst_check)
# >>>True

# r_point = Point(1,2)
# r_point = Point.zero() #Is alternated to this.
# print(r_point.draw())
# >>>Point; 0,0
# >>><__main__.Point object at 0x000001E0D686BE50>
# print(r_point.__str__())
# >>>1,2
# print(str(r_point))
# >>>1,2

# rh_point = Point(1,2)
# lh_point = Point(1,2)
# print(rh_point == lh_point)
# >>>False
#wtf right?? Let's use the __eq__ magic method in our 'Point' class.
# >>>True

# up_point = Point(10,20)
# dn_point = Point(1,2)
# print(up_point > dn_point)
# >>>TypeError: '>' not supported between instances of 'Point' and 'Point'
#How do we go about the Type error:
#Let's create another magic method for the __gt__ operations in our 'Point' class.
# >>>True
#What if we switch arguments.
# up_point = Point(10,2)
# dn_point = Point(10,20)
# print(up_point > dn_point)
# >>>False
#Let's interchange.
# up_point = Point(10,2)
# dn_point = Point(10,20)
# print(up_point > dn_point)
# >>>False
#What they where equal again.
# up_point = Point(10,20)
# dn_point = Point(10,20)
# print(up_point == dn_point)
#True
# >>>False

#Let's add two classes with the __add__ magic method.
# p_point = Point(2,4)
# a_point = Point(3,6)

# combined = p_point + a_point
# print(combined)
# >>>TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
#We get another TypeError;
#Let's use the add Magic Method.
# p_point = Point(2,4)
# a_point = Point(3,6)
# combined = p_point + a_point
# print(combined)
# >>>5,10

#More Magic Methods for creating class containers.

# class BlogCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self,tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
#     def __setitem__(self,tag,count):
#         self.__tags[tag.lower()] = count
#     def __getitem__(self,tag):
#         return self.__tags.get(tag.lower(), 0)
#     '''Adding a Magic Method to check the len of self.tags'''
#     def __len__(self):
#         return len(self.__tags)
#     def __iter__(self):
#         return iter(self.__tags)

# cloud = BlogCloud()
# cloud.add('Python')
# cloud.add('Python')
# cloud.add('Python')
# cloud.add('Python')
# cloud.add('Javascript')
# cloud.add('Solidity')
# cloud.add('Solidity')
# cloud.add('Vyper')
# cloud.add('Brownie')
# cloud.add('Javascript')

# print(cloud.tags)
# >>>{'python': 4, 'javascript': 2, 'solidity': 2, 'vyper': 1, 'brownie': 1}
# print(len(cloud))
# >>>TypeError: object of type 'BlogCloud' has no len()
# >>>5   #Also the same as checking the len of cloud.tags.
#Let's iterate through the class instance.
# print(cloud["Vyper"])
# >>>TypeError: 'BlogCloud' object is not subscriptable
#Let's make another Magic Method called __iter__ for our class.
#This makes our instance iterable, to return an item at a time (using loops)

#Let's modify a value by it's key, let's set an item.

# >>>TypeError: 'BlogCloud' object does not support item assignment
#Let's now create the __setitem__ magic method in our class.
#Setting the item.
# cloud["Vyper"] = 10
#Getting the item.
# print(cloud.__getitem__("Vyper"))
# >>>10
#Private Members
# print(cloud.__dict__)
# >>>{'_BlogCloud__tags': {'python': 4, 'javascript': 2, 'solidity': 2, 'vyper': 1, 'brownie': 1}}
# print(cloud.tag["PYTHON"])
# >>>AttributeError: 'BlogCloud' object has no attribute 'tag'\
#Let's access it here;
# print(cloud._BlogCloud__tags)
# >>>{'python': 4, 'javascript': 2, 'solidity': 2, 'vyper': 1, 'brownie': 1}


# class Product:
#     def __init__(self,price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self,value):
#         if value < 0:
#             raise ValueError("Cannot take a Negative Value")
#         self.__price = value

# cream = Product(-10)
# >>>ValueError: Cannot take a Negative Value
#Because expression is non-pythonic.

# print(cream.get_price())
# >>>ValueError: Cannot take a Negative Value

#Let's make the class more Pythonic with the property decorators.
# class Product:
#     def __init__(self,price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self,value):
#         if value < 0:
#             raise ValueError("Cannot take a Negative Value")
#         self.__price = value

# tan_lotion = Product(10)
# tan_lotion.price = 20
# # print(tan_lotion.price)
# # >>>20
# tan_lotion.price = 100
# print(tan_lotion.price)
# >>>100
# >>>RecursionError: maximum recursion depth exceeded in comparison
# >>>ValueError: Cannot take a Negative Value

# class Asukwo(object):  #All classes inherits from the object class in Python.
#     def __init__(self):
#         self.age = 1970
#     def farm(self):
#         return "Time to plant Yams."
#     def eat(self):
#         return "Time to eat food."

# Marvel = Asukwo()
#To check instances and substances of a class, we use the 'isinstance' and 'issubclass' functions respectively.
# print(isinstance(Marvel, Asukwo)) #Is Marvel an instance of Asukwo?
# >>>True
# print(issubclass(Asukwo, object)) #Is Asukwo a subclass of the invisible object?
# >>>True
# print(Marvel.age)
# >>>1970
# print(Marvel.farm())
# >>>Time to plant Yams


# class Asukwo(object):  #All classes inherits from the object class in Python.
#     def __init__(self):
#         print("Husband")
#         self.age = 1970
#     def farm(self):
#         return "Time to plant Yams."
#     def eat(self):
#         return "Time to eat food."

# class Isabella(Asukwo):
#     def __init__(self):
#         super().__init__()
#         print("Wife")
#         self.clothes = 1000
#     def cook(self,food):
#         return f"Time to cook {food}."
#     def hair(self,style):
#         return f"Time to make {style} hairstyle."

# Jemimah = Isabella()  #Jemimah is an instance of Isabella whic is a subclass of Asukwo.
# print(Jemimah.hair("All-back"))
# >>>Husband
	#  Wife
	#  Time to make All-back hairstyle.
# print(Jemimah.farm())
# >>>...
	#Time to plant Yams.
# print(Jemimah.age)
# >>>...
# >>>1970

#Multilevel Inheritance
#A perfect example of a multi_level inheritance

# class Flyer:
#     def fly():
#         pass
# class Swimmer:
#     def swim():
#         pass
# class FlyingFish(Flyer,Swimmer):
#     pass

#A Good Example of Inheritance.
# class InvalidOperationError(Exception):
#     pass
# class Stream:
#     def __init__(self):
#         self.opened = True
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError ("Cannot open already Opened File")
#         self.opened = True
#         print("Reading File from a String")
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError ("Cannot closed already closed file")
#         self.opened = False
#         print("Reading File from a Network")

# class Network(Stream):
#     def read(self):
#         print("Reading data from a network")
# class File(Stream):
#     def read(self):
#         print("Reading data from a file")

# ever_py = File()
# ever_py.read()
# >>>Reading data form a file
# ever_py.close()
# ever_py.close()
# >>>__main__.InvalidOperationError: Cannot closed already closed file
# ever_py.open()
# ever_py.read()
# ever_py.open()
# >>>__main__.InvalidOperationError: Cannot open already Opened File

# #Creating Abstract Classes.
# from abc import ABC,abstractmethod
# class InvalidOperationError(Exception):
#     pass
# class Stream(ABC):
#     def __init__(self):
#         self.opened = True
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError ("Cannot open already Opened File")
#         self.opened = True
#         print("Opened File...")
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError ("Cannot closed already closed file")
#         self.opened = False
#         print("Closed File...")
#     @abstractmethod
#     def read(self):
#             pass

# class Network(Stream):
#     def read(self):
#         print("Reading data from a network")
# class File(Stream):
#     def read(self):
#         print("Reading data from a file")
# class MemoryStream(Stream):
#     # def read(self):
#         # print("Reading data from Memory")
#     def work(self):
#        print("Working data from Memory")

# ever_py = MemoryStream()df
# ever_py.work()

# >>>TypeError: Can't instantiate abstract class MemoryStream without abstract method read
#Solution: The MemoryStream method must be named read or must have a read function.
# from pprint import pprint
# words = "Vought for Ethereum 2024"
# dicn = {}

# for letr in words:
#     if letr in dicn:
#         dicn[letr] += 1
#     else:
#         dicn[letr] = 1

# pprint(dicn,width=2)

# pprint(sorted(dicn.items(), key=lambda kv: kv[1] ,reverse=True))

#Extending built in types with classes.
# class Text(str):
#     def duplicate(self):
#        return self + self

# text = Text("VoughtforETH")
# text.      #The dot notation here gets all methods of a string (str)

# Let's duplicate
# print(text.duplicate())
# >>>VoughtforETHVoughtforETH

#Crafting namedtuples
# Namedtuples can be used in place of classes with lesser methods and attributes.

# from collections import namedtuple

# Point = namedtuple("Point", ["x","y"])
# p1 = Point(x=1,y=2)
# p2 = Point(x=7,y=14)
# print(p1.x)
# >>>x
# print(p2.y)
# >>>14







# Connecting a webbrowser to a program in Python.
import webbrowser

print("Deployment Completed")
address = "https://google.com"
try:
    webbrowser.open(address)
except ConnectionError:
    print("Error, cannot connect.")
    
