# Python Version - 3.9.5
        #  Ch 1 Topic 1 Print() Function
print("Hello World")                   # Python
print("Hello 'my' World")
print('Hello "my" World')
print('Hello \'my\' World')                # Escape Sequence
print("Hello \"my\" World")
print("this is backslash \\\\")
print("Line A \nLine B \nLine C")
print("Hell\blo")
print("Name\tSourav")
print("Line A \\n Line B")                  # Output : Line A \n Line B 
print("Line A \\t Line B")                  # Output : Line A \t Line B
print("\\\" \\\'")                          # Output : \'' \'
# Ex 1      **** these follow lines ****
print("This is \\\\ Double Backslash")      # Output : This is \\ Double Backslash
print("There are /\\/\\/\\/\\ Mountain")    # Output : There are /\/\/\/\ Mounatain
print("\\\" \\n \\t \\\' ")                 # Output : \" \n \t \'
print(r"Line A \n Line B")                # Raw String
print("\U0001F618")                         # Output : Emoji
            # Python As A Calculator
print(2+3)
print(2+3*4)
print(2/4)                                  # Float Point Division
print(4/2)
print(4//2)                                 # Integral Division
print(2//4)
print(2**0.5)                               # Power Exponential
print(2**3)
print(round(2**0.5,4))
print(2**3/2*6-4*(3-4/2))
print(3%2)
print((2+3)*2)
print((2+3)*5/2%6)
print(299795624**2)
                # Variable
number1 = 3
print(number1)
number2 = 8
print(number2)
                # String, Number
name = "Sourav"               
print(name)
name = "Biswas"
print(name)
        # Rule 1 : Variable not Start with No. and Special sign # Letter,_,.... First Letter
        # user_one_name = Rohit|Snake Writting Case Python  # userOneName = Krishna|Camel Writting Case Java
    # Ch - 2  Cantatination
First_Name = "Sourav "
Last_Name = "Biswas"
Full_Name = First_Name + Last_Name
print(Full_Name)
print(First_Name + "3")
print(First_Name + str(3))
print(First_Name* 3)
        # User Input    # Input Function
name = input("type your name")
print("Hello" + name)
        # String
age = input("what is your age ?")
print("your age is" + age)
address = input("What is your Address ?" )
print("Your address is" + address)
print("thanks for your precious time")
                # Int Function
number_one = int(input("enter First number "))
number_two = int(input("enter Second number"))
total = number_one + number_two
print("total is" + str(total))
number1 = str(48)
number2 = float("96")
number3 = int("64")
print(number2 + number3)
name, age = " Sourav Biswas ","21"
print("hallo" + name + "your age is " + age)
x = y = z = 1
print(x+y+z)
name, age = input("enter your name and age ").split(',')           # two or more string in one line
print(name)
print(age)
print(f"hello {name} your age is {age} ")            # String Formmating  #  Python 3.6
print("hello {} your age is {} ",format(name, age))                       #  Python 3
                # Ch - 1        Ex - 1  # Ask user to input 3 number using string formatting
num1 = input("enter your first number")
num2 = input("enter your second number")
num3 = input("enter your third number")
(int(num1) + int(num2) + int(num3))/3
print(f"average of three numbers : {(int(num1) + int(num2) + int(num3))/3}")
                # String Indexing
language = ("python")
print(language[4])      # [ ] Always use for indexing letter
print(language[-1])
print(language[5])
print(language[-6])
# Slicing/Selecting Sub Sequence        # Syntax - [Start Argument : Stop Argument - 1]
print("language"[:])
print("language"[0:2])
print("language"[2:4])
print("language"[3:6])
print("language"[-3:6])
print("language"[:3])
                # Step Argument         # Syntax - [Start Argument : Stop Argument - 1 : Step]
print("language"[::])
print("language"[0:7:2])
print("language"[2:7:3])
print("language"[0::6])
print("language"[-3:6])
print("language"[0::3])
print("language"[-1::-1])
print("Thiruvananthapuram"[::-1])
# Ch - 2          Ex - 1          # Ask user name and print back user name in reverse order     # Try to make your program in 2 lines
name = input("type your name")
reverse = name[-1::-1]
print(f"reverse of your name is {reverse}")
name = input("type your name")
print(f"reverse of your name is {name[-1::-1]}")
        # String Method
name = "Sourav Biswas"
print(len("Sourav"))            #  Lenth () Function  # Count Letter in String
print(len(name))
print(name.lower())             # Lower () function   # Small Letter
print(name.upper())             # Upper  () function  # Capital Letter
print(name.title())             # Title () function   # 1C rest small
print(name.count())             # Count () function   # Count letter
        #  Ch - 2  # Ex - 3  # Take two comma seperated input from user # 1.) user's name # 2.) a single character
        # Output - 2 lines # 1.) user's name length 2.) count the character that user inputed
name, char = input("enter comma seperated and character : ").split(',')
print(f"lenth of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")
dots = "......................"
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.replace(" ","") + dots)
string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))          # Replace () function
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.find("is"))                #Find () function
is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)
print(name.center(21,"*"))              # Center Method
name = input("type your name")
print(name.center(len(name) + 8,"*"))
# String are Immuable = Original String Never Change
name = "Subho"
name = name + "jit"
print(name)
name += "jit"
print(name)
age = int("20")
age = age + int("1")
print(age)
age += int("1")
print(age)
age *= int("2")
print(age)
# Ch - 3 If Statement # If condition is true then this code will execute
age = input("enter your age : ")
age = int(age)
if age >= 14:
        print("you are above 14")
else:
        print("Sorry you can't play")
# Ch - 1 Ex -1  # Number Guessing Game # Make a Variable winning_number and assign any number to it. Ask user to guess a number
winning_number = 27
user_input = input("guess anumber Between 1 to 50 : ")
user_input = int(user_input)
if user_input == winning_number :
        print("YOU WIN !!!")
else :
        if user_input > winning_number :
                print("Better Luck Next Time, too high")
        else : 
                 print("Better Luck Next Time, too low")
# AND, OR Operator # Cheak two condition at same time
name = input("enter your name : " )         # AND Operator # If one condition is true then true
age = int(input("enter your age : "))
if name == "Sourav Biswas" and age == int("21") :
        print("Condition True")
else :
        print("Condition False")
name = input("enter your name please : " )         # OR Operator  # If one condition is true then true
age = int(input("enter your age please : "))
if name == "Sourav Biswas" or age == int("21") :
        print("Condition True")
else :
        print("Condition False")
# Ex - 2  # Watch Coco # Ask user's name and age  # If user's name start with ('A' or 'a') and age above 10 then :
# print you can watch Coco movie        # Else you cannot watch Coco movie
user_name = input("enter your name please : " )
user_age = int(input("enter your age please : "))
if user_age >= 10 and (user_name[0] == 'a'or user_name[0] == 'A') :
        print("You can watch Coco movie ")
else :
        print("You cannot watch Coco movie")
# If - Elif - Else Statement    # Show Ticket Pricing        # 1 to 3 (free) # 4 to 10 (150) # 11 to 60 (250) Above 60 (200)
age = int(input("enter your age please : "))
if age == 0 :
        print("you can't Watch Show")
elif 0 < age <= 3 :
        print(" Ticket Pricing : Free")
elif 3 < age <= 10 :
        print("Ticket Pricing : 150")
elif 11 < age <= 60 :
        print("Ticket Pricing : 250")
else :
        print("Ticket Pricing : 200")
# In Keyword       # if within
if 'a' in name :
    print("a is present in name")
else :
    print("not present")    
if name :                   # Cheaking Empty or Not
    print("string is not empty")
else :
    print("string is empty")
name = input("enter your name please : " )
if name :
        print(f"your name is {name}")
else :
        print("you didn't type anything")
                # Loops
i = 1
while i <= 10 :
        print("Hello World")
        i += 1
                # Sum of n numbers program using while loop
number = int(input("enter a number : "))
total = 0
n = 1
while i <= n :
        total += n
        n += 1
print(total)
# Ch -3 # Ex - 4 # Problem # Ask User to input a number containing more than # Calculate and print
number = int(input("enter a number : "))
total = 0
i = 1
while i <len(number) :
        total += int(number([i]))
        i += 1
        print(total)
# Ask user name # Print Each Words # Output # S : 1 # o : 1 # u : 1 # r : 1 # a : 2 # v : 1 # B : 1 # i : 1 # s :2 w : 1
name = input("enter your name please : " )
temp_var = ""
i = 0
while i < len(name) :
        if name [i] not in temp_var :
                temp_var += name[i]
                print(f"{name[i]} : {name.count(name[i])}")
        i += 1
# Infinite Loop
while True :
        print("Hello World")
i = 0
while i <= 10 :
        print("Hello World")
        i += 1
# For Loop with range function
for i in  range(int(number)) :
        print("World is Vast")
for i in  range(1, 7) :
        print("Hello Mom")
        print(f"Hi Mom : {i}")
# Sum from 1 to n
n = int(input("enter a number : "))
total = 0
for i in  range(1, n+1) :
        total += 1
print(total)
# Break and Continue
for i in range(1, 11) :
        if i == 5 :
                break
        print(i)
for i in range(1, 11) :
        if i == 5 :
                continue
        print(i)
#  Modify Number Guess Game
import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input("guess number between 1 and 100"))
game_over = False
while not game_over:
        if number == winning_number :
                print(f"you win, and you guessed this number in {guess} times")
                game_over = True
        else :
                if number<winning_number :
                        print("two low")
                        guess += 1
                        number = int(input("guess again"))
                else :
                        print("two high")
                        guess += 1
                        number = int(input("guess again"))
#  DRY Method - Don't Repeat Yourself # Modify Number Guess Game
import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input("guess number between 1 and 100"))
game_over = False
while not game_over:
        if number == winning_number :
                print(f"you win, and you guessed this number in {guess} times")
                game_over = True
        else :
                if number<winning_number :
                        print("two low")
                else :
                        print("two high")
guess += 1
number = int(input("guess again"))
# Step Argument in range function
for i in range (1, 11) :
        print(i)
for i in range (1, 11, 1) :
        print(i)
for i in range (1, 11, 2) :
        print(i)
for i in range (0, 11, 1) :
        print(i)
for i in range (10, 0, -1) :
        print(i)
for i in range (10, 0, -1) :
        print(i)
for i in range (1, -11, -1) :
        print(i)
                # For loop String
for i in name :
        print(i)
num = input("enter a number")
total = 0
for i in num :
        total += int(i)
        print(total)
        #  Function Introduction
def add_two(a, b) : 
        return a + b
        total = add_two (a, b)
print(total)
def add_two(a, b) :
        a = int(input("enter your first number"))
        b = int(input("enter your second number"))
        total = add_two(a, b)
        print(total)
def add_two(first_name, last_name):
        first_name = input("type first name")
        last_name = input("type second name")
        total = add_two(first_name, last_name)
        print(add_two(first_name, last_name))
# return and print
def add_three(a, b, c) :
        return(a+b+c)
        print(a+b+c)
        print(add_three(5, 5, 5))
def last_char(name) :
        return name [-1]
        print(last_char("sourav"))
def odd_even(num):
        if num % 2 == 0 :
                return True
                print("even")
        else:
                return False
                print("odd")
def song ():
        return "happy birthday song"
        print(song())
# Ch - 4 Ex - 1 Define a function which takes two number as input and return greater of two number
def greater (num1, num2):
        if num1 > num2 :
                return num1
        else:
                return num2
num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
bigger = int(greater (num1, num2))
print(f"{bigger} is greater")
def greatest (a,b,c):
        if a>b and a>c :
                return a
        elif b>a and b>c :
                return b
        else :
                return
print(greatest(10,20,30))
 # Function inside function
def new_greatest(a,b,c) :
        bigger = greater (a,b)
        return greater(bigger, c)
print(new_greatest(10,20,30))
# Ch 4 Ex - 2  # Palindromes
word = input("please Enter a word : ")
def is_palindromes(word):
        reversed_word = word[::-1]
        if word == reversed_word :
                return True
        else:
                return False
print(is_palindromes(word))
# Fibonacci Series  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,377, 610, 987, 1597, 2584, 4181,
def fibonacci_seq(n) :
        a = 0
        b = 1
        if n == 1:
                print(a)
        elif n == 2 :
                print(a, b)
        else :
                print(a,b,  end = " ")
                for i in range(n-2):
                        c = a + b
                        a = b
                        b = c
                        print(b , end = " ")
fibonacci_seq(17)
# Defalt parameters
def user_info(first_name = "Unknown", last_name = "Unknown", age = none):
        print(f"your first_name is {first_name}")
        print(f"your last_name is {last_name}")
        print(f"your age is {age}")
user_info("Sourav", "Biswas", 21)
#  Scope  # Never  Use in Professional Programming
X = 5
def fun():
        X  = 7
        return X
        print(fun())
        print(X)
# Data Structure  # List ---> this ch # Order collection of items # You can store anything in list int, float, string
numbers = [1,2,3,4]
print(numbers[1])
word = ["word 1","word 2","word 3"]
print(word[:-1])
mixed = [1,2,3,4,"fixed","six",2.3,None]
print(mixed[-1])
mixed[1] = "two"                                # To Change The String Characters
# Add data to list # how to add item to our list # Most common things that you can do with your list and most important
fruit = ['grape','apple']
fruit.append('mango')
print(fruit)
fruit = []
fruit.append('grapes')
#  More Method to add data #  some Method to add data in our list # insert method # how to join (concatenate) two list # extended method
fruit1 = ['grape','orange']
fruit1.insert(1,'grapes')
print(fruit1)
fruit2 = ['mango','apple']
fruit = fruit1 + fruit2
print(fruit)
fruit1.append(fruit2)
fruit1.extend(fruit2)
print(fruit1)
print(fruit2)
#  Common methods to delete data from list
fruit = ['orange','apple','kiwi','pear','banana']       # pop method
fruit.pop(1)
print(fruit)
del fruit[1]
print(fruit)
fruit.remove('banana')
print(fruit)
# append, extend, insert        # pop, remove, Del
# In keyword with list
fruit = ['orange','apple','pear','banana','kiwi']
if 'apple' in fruit :
        print('apple is present')
else :
        print('not present')
# count # sort method # sorted function # reverse # clear
fruit = ['orange','apple','pear','banana','kiwi']
print(fruit.count('apple'))
print(fruit.sort())
numbers = [3, 5, 1, 9, 10]
numbers.sort()
print(sorted(numbers))
print(fruit)
numbers.clear()
print(numbers)
numbers_copy =  number.copy()
print(numbers)
# 'is' vs '==' # List Comperision
fruit1 = ['orange','apple','pear','banana','kiwi']
fruit2 = ['orange','apple','pear','banana','kiwi']
fruit3 = ['orange','mango','grapes','pomegranate','plum','apple','pear','banana','kiwi']
print(fruit1 == fruit2)         # Value are same
print(fruit1 is fruit2)         # place are same
# Split Method          # Convert String to List
user_info('Sourav Biswas, 21').split( )
user_info('Sourav Biswas, 21').split(',')
print(user_info)
name, age = ('Sourav Biswas, 21').split(',')
print(name)
print(age)
# Join Method          # Converting List to String
user_info = ['Sourav Biswas, 21']
print(','.join(user_info))
# List vs Array # List - Store any data / flexible # Javascript Array - Python List / flexible # Python array module - fix data type # numpy arrays - binding c
# List vs String # String are Immuable # List are Mutable
S = 'string'
t = S.title()
print(t)
l = ["word 1","word 2","word 3"]
l.pop()
print(l)
l.append("word 3")
print(l)
# Looping in List
for fruit in fruit3 :           # For Loop
        print(fruit)
i = 0
while i < len(fruit3):
        print(fruit[i])
        i += 1
# List inside List
matrix = [[1, 2, 3],[4, 5, 6,],[7, 8, 9]]
print(matrix[2])
for i in matrix:
        print(i)
for sublist in matrix:
        print(sublist)
print(matrix[2][2])
print(matrix[1][1])
S = 'string'
print(type(S))
# Generate lists with range functions   # Something more about pop method     # Index method    # pass list to a function
numbers = list(range(1, 11))
print(numbers)
print(numbers.pop())
print(numbers.index(1))
def negative_list(l):
        negative = []
        for i in l :
                negative.append(-i)
        return negative
print(negative_list(numbers))
# Ch -5 Ex - 1 # Define a function which will take list contaning number as input and return list containing square of every elements
def square_list(l):
        square = []
        for i in l :
                square.append(i**2)
        return square
print(square_list(numbers))
# Ex - 2 # Define a function which will list as a argument and this function will return a reverse method or [::-1] but try to do this with the help of append and return method
def reverse_list(l):
        r_list = []
        for i in range(len(l)):
                popped_items = l.pop()
                r_list.append(popped_items)
        return r_list
print(reverse_list(l))
# Ex - 3 # define a function that take list of word as argument and return list with reverse of every element in that list
# ['abc','tuv','xyz'] = ['cba','vut','zyx']
def reverse_elements(l):
        element = []
        for i in l:
                element.append(i[::-1])
        return element
words = ['abc','tuv','xyz']
print(reverse_elements(words))
# Ex - 4  # filter odd even # define a input function # Input # List [1,2,3,4,5,6,7] # Output [[1,,3,5,7],[2,4,6]]
def filter_odd_even(l):
        odd_nums = []
        even_nums = []
        for i in l:
                if i % 2 == 0:
                        even_nums.append(i)
                else:
                        odd_nums.append(i)
        output = [odd_nums, even_nums]
        return output
nums = [1,2,3,4,5,6,7]
print(filter_odd_even(nums))
# Common element finder function define a function which take 2 list as input and return a list which contain comman elements of both lists
# Input = [1,2,5,8],[1,2,7,6] # Output = [1,2]
def common_finder(l1,l2):
        output =[]
        for i in l2:
                if i in l1:
                        output.append(i)
        return output
print(common_finder([1,2,4,5],[1,2,6,7]))
number = [6,60,2]       # Min and Max Function
print(min(number))
print(max(number))
def greatest_diff(l):
        return max (l) - min(l)
print(greatest_diff(numbers))
# Ex - 6 Last Exercise  # Function # [1,2,3,[1,2],[3,4]] # input # Type
def sublist_counter(l):
        count = 0
        for i in l:
                if type(i) == list:
                        count += 1
                return count
mixed = [1,2,3,[1,2],[3,4]]
print(sublist_counter(mixed))
# Ch - 6 tuple data structure # tuple can can store any data type # most important tuple are immutable, once tuple is created you can,t update
# Data inside # tuples are faster than lists 
# Methods # count,index # len function # Slicing
example = ('1','2','3','4')
example[0] = 1
print(example[:2])
# looping in tuple # tuple with one element # tuple without parenthesis # tuple unpacking # list inside tuple # some function that you can use with tuple
mixed = (1,2,3,4.0)             # for loop and tuple
for i in mixed:                 # NOTE - you can use while loop too # tuple with one element
        print(i)
word = ('word',)
print(type(word))
guitars = 'Yamha','taylor','baton rogue'        # tuple without parenthesis 
print(type(guitars))
guitarist = ('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')          # tuple unpacking
guitarist1,guitarist2,guitarist3 = (guitarist)
print(guitarist2)
favorites = ('southern Manolia',['Tokyo Ghoul Theme','landscape'])
favorites[1].pop()
favorites[1].append('we made it')
print(favorites)
# Function returning teo values
def fun(int1,int2):
        add = int1 + int2
        multiply = int1*int2
        return add,multiply
print(fun(2,3))
add,multiply = fun(2,3)
print(add)
print(multiply)
nums = tuple(range(1,11))       # Something more about tuples, list, str
print(nums)
nums = list((1,2,3,4,5,6,7,8,9,10))
nums = str((1,2,3,4,5,6,7,8,9,10))
# Output = "((1,2,3,4,5,6,7,8,9,10))"
print(type(nums))
# List = Str / Tuple = Str / Tuple = List
# Ch - 7 Dictionary # Q - Why we use dictionaries ? # A - Because of limitation of list, lists are not enough to represent # real data
user = ['sourav',21,['coco','OMG'],['awakening','fairy']]
# this list containers user name,age,fav movie,fav tunes        # You can do this but this is not a good way to do this
# Q - what are dictionaries     # A - Unorderd collection of data in key : value pair
# how to create dictionaries
user = {'name':'Sourav','age': 24}
print(user)
print(type(user))              # No Indexing, only key
# Secondary method to create dictionary
user1 = dict(name = 'Sourav',age = 21)
print(user1)
# How to access data from dictionary    # NOTE - There is no indexing because of unorderd collection of data.
print(user['name'])
print(user['age'])
# which type of data a dictionary can store # anything # numbers,string,list,dictionary
user_info = {
        'name' : 'Sourav',
        'age' : '21',
        'fav_movie' : ['coco','OMG'],
        'fav_tunes' : [],
}
print(user_info['fav_movies'])
# How to add data to empty dictionary
user_info1 = {}
print(user_info1)
# Cheak if key exist in dictionary
if 'name' in user_info:
        print('present')
else:
        print('not present')
# Cheak if value exist in dictionary
if 'sourav' in user_info.vales():
        print('present')
else:
        print('not present')
# loop in dictionaries
for i in user_info:
        print(i)
for i in user_info.values():
        print(i)
# Key Method
user_info_keys = user_info.key()
print(user_info_keys)
for i in user_info:
        print(user_info(i))
dict_items = user_info.items()          # Items Method
print(user_info)
print(type(user_info))
for key, value in user_info.items():
        print(f'key is {key} and value is {value}')
for i,j in user_info.items():
        print(f'key is {i} and value is {j}')
# how to add data
user_info['fav_songs'] = ['song 1','song 2']
print(user_info)
popped_items = user_info.pop('fav_tunes')
print(user_info)
print(f'popped_item is {popped_items}')
print(user_info)
popped_items = user_info.pop.items()            # Pop item Method
print(user_info)
more_info = {'state':'Haryana','hobbies':['coding','reading','guitar']}
user_info.update(more_info)
print(user_info)
# fromkeys      # d = {'name':'unknown','age':'unknown'}
d = dict.fromkeys(['name','age','hetight','weight'],'unknown')
print(d)
d = dict.fromkeys('abc',"unknown")
d = dict.fromkeys(range(1,11),'unknown')
d = dict.fromkeys(['name','age'],['unknown','unknown'])
print(d['name'])
print(d.get('name'))
if 'name' in d:
        print('present')
else:
        print('not present')
if d.get('name'):
        print('present')
else:
        print('not present')
d.clear()       # Clear Method
print(d)
d1 = d.copy()   # Copy Method
print(d1)
# more about get, two same keys in dictionaries
user = {'name':'Sourav','age':21}
print(user.get('name'))
print(user.get('name','not found !'))
# Exercise        # define a function that takes a number(n)    # return a dictionary containing cube of number from 1 to n
# Example # cube_finder(4)      # cube = {}     # {1:1,2:8,3:27,4:64,}
def cube_finder(n):
        cubes = {}
        for i in range (1,n+1):
                cube[i] = i**3
        return cubes
print(cube_finder())
d = {'h':2,'a':1,'h':3}
print(d)
def word_counter(s):
        for char in s:
                count[char] = s.count(char)
        return word_counter
print(word_counter('Sourav'))
user = {}
name = input("what is your name ? : ")
age = input("what is your age ? : ")
fav_movies = input("your fav_movies comma seperated: ").split(',')
fav_songs = input("your fav_songs comma seperated: ").split(',')
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_songs
print(user)
for key,value in user.items():
        print(f'{key} : {value}')
# set data type         # unorderd collection of unique items
s = {1,2,3,4,5,6,7,7,8}
print(s[1])
l = {(1,2),(34,5),(6,3),(6,23),(9,3)}
print(type(l))
s2 = list(set(1))
print(s2)
s.add(9)                # Add Method
s.remove(6)             # Remove Method
s.discard(11)           # Discard Method
s.clear()               # Clear Method
s.copy()                # Copy Method
s = {1,1.1,2.3,'string'}
# Set not save - List, Dictionaries     # More about sets       # in keyword in sets and for loop
s = {'a','b','c','d','e'}
#       in keyword to cheak if items is present or not in set
if 'a' in s:
        print('present')
else:
        print('not present')
for item in s:
        print(s)
l = [1,2,3,3,2,4,3,4,56,7,8,9,10]
print(list([l]))
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1 | s2)
print(s1 & s2)
# List Comprehension   # With the help of list comprehension we can create of list in one line          # Create a list of square from 1 to 10
square = []
for i in range(1, 11):
        square.append(i**2)
print(square)

square2 = [i**2 for i in range(1, 11)]
print(square2)

negative = []
for i in range(1, 11):
        negative.append(-i)
print(negative)

negative2 = [-i for i in range(1, 11)]
print(negative2)

names = ['Sourav','Manoj','Rohit']
name_list = []
for name in names :
        name_list.append(name[0])
print(name_list)

name_list2 = [name[0] for name in names]
print(name_list2)
# Ex 1 Define a function that list of string # List containing reverse of every string # NOTE - Use list comprehensive because we already did this ex
# using normal method # Example # l = ['abc','tuv','xyz'] # reverse_string(1) ---> ['cba','vut','zyx']
def  reverse_string(l):
        return[name[::-1] for name in l]
print(reverse_string(['abc', 'tuv', 'xyz']))

def reverse_string(l):
        new_list = []
        for name in l:
                new_list.append(name[::-1])
        return new_list
print(reverse_string(['abc', 'tuv', 'xyz']))

# List Comprehensive with if statement
numbers = list(range(1,11))
nums = []
for i in numbers :
        if i%2 == 0:
                nums.append(i)
print(nums)

even_nums = [i for i in numbers if i%2 == 0]
even_nums2 = [i for i in range(1,11) if i%2 == 0]
print(even_nums)
print(even_nums2)
odd_nums = [i for i in range(1,11) if i % 2 != 0]
print(odd_nums)
# num to string  # Define a function  # Example  # input ---> [True,False,[1,2,3],1,3,1.0]  # output ---> ['1','1.0','3']
def num_to_string(l):
        return [str(i) for i in l if (type(i)== int or type(i) == float) ]
print(num_to_string([True,False,[1,2,3],1,3,1.0]))
# List comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in nums:
        if i%2 == 0:
                new_list.append(i**2)
        else:
                new_list.append(-i)
print(new_list)

new_list2 = [i**2 if (i % 2 == 0) else -i for i in nums]
print(new_list2)
# List Comprehension in nested list
example = [[1,2,3],[1,2,3],[1,2,3]]
nested_comp = [[i for i in range(1,4)] for j in range (3)]
print(nested_comp)

new_list = []
for j in range(3):
        new_list.append([1,2,3])
# Dictionary Comprehension              # Square = {1:1,2:4,3:9}
square = {f'square of {num} is':num**2 for num in range(1,11)}
for k,v in square.items():
        print(f'{k} : {v}')
string = 'Sourav'
for i in string:
        print(i)
word_count = {char:string.count(char) for char in string}
print(word_count)
# Dictionary Comprehension with If else         # d = {1:'odd',2:'even'}
odd_even = {i:('even' if i%2 == 0 else 'odd') for i in range(1,11)}
print(odd_even)
# Sets Comprehension
s = {k**2 for k in range(1,11)}
print(s)
names = ['Sourav','Manoj','Rohit']
first = {name[0] for name in names}
print(first)

# * args | *operator
def all_total(*args):
        print(args)
        print(type(args))
all_total(1,2,3,4,5,65)

def all_total(*args):
        total = 0
        for nums in args:
                total += nums
        return total
print(all_total(675,54,67,45,76,87,3))
# *args as a argument
def multiply_nums(*args):
        multiply = 1
        print(args)
        for i in args:
                multiply *= i
        return multiply
nums = [2,3,4]
print(multiply_nums(*nums))
# Ch 1 Ex - 1  # Define a function # input  # nums, iterable(tuples,list) containig as args  # Example  # nums = [1,2,3]  # to_power(3,*nums)  #output list ---> [1**3,8,27]  # if user didn't pass any args then give a user a message 'hey, you didn't pass args'  # else return list
# NOTE - Use list comprehension
def to_power(nums,*args):
        if args:
                return [i**nums for i in args]
        else:
                return "hey, you didn't pass arg"
nums = [1,2,3]
print(to_power(3,*nums))
# **kwargs - keyword args | double star operator
# **kwargs as a parameter
def func(**kwargs):
        for k, v in kwargs.items():
                print(f'{k} : {v}')
func(first_name = 'Sourav', last_name = 'Biswas')
# *args - tuples        # **kwargs - Dictionary
# Dictionary Unpacking
d = {'name' : 'Sourav','age' : 21}
func(**d)
# Function with all type of parameters          # PADK # Parameters # *args  # Default parameters # **kwargs
def func(name,*args,last_name = 'Unknown',**kwargs):
        print(name)
        print(args)
        print(last_name)
        print(kwargs)
func('Hercules', 1,2,3,a = 1, b = 2)
# Ch - 11  # Ex - 2  # Define a function Name = ['Hanuman','Ram'] # Print(func(names,reverse_str = True))
def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ['Hanuman','Ram']
print(func(names, reverse_str = True))
# Lambda Expression (Anonymous Function)
def add (a,b):
        return a+b
add2 = lambda a,b : a+b
print(add2(2,3))
# built in, map, reduce, filter
multiply = lambda a,b :a*b
print(multiply(2,4))
def is_even (a):
        return a%2 == 0
print(is_even(5))
is_even2 = lambda a : a%2 == 0
print(is_even2(5))
def last_char(s):
        return s[-1]
last_char = lambda s : s[-1]
print(last_char('Sourav'))
#  Lambda with if , else
def func(s):
        if len(s)>5:
                return True
        return False
def func(s):
        return len(s)>5
func = lambda s: True if len(s)>5 else False
print(func('Ramayan'))
# Enumurate function
#  we use enumerate function with for loop to track position of our items in iterable  # how we can do this without in enumerate function names
names = ['abc','abcdef','Sourav']
pos = 0
for name in names:
        print(f'{pos} ---> {name}')
        pos += 1
# With enumerate function
for pos, name in enumerate(names):
        print(f'{pos} ---> {name}')

# define a function that take  to argument      # 1)  list containing string            # 2) string that want to find in your list and this function will return the index of string list and if string is not present then return -1
def find_pos(l, target):
        for pos, name in enumerate(l):
                if names == target:
                        return pos
                return -1
print(find_pos(names, 'Sourav'))

# map function
numbers = [1,2,3,4]
def square(a):
        return a**2
squares = list(map(square, numbers))
print(squares)

square = list(map(lambda a: a**2,numbers))
print(square)

square_new = [i**2 for i in numbers]
print(square_new)

new_list = []
for num in numbers:
        new_list.append(square(num))
print(new_list)

names = ['abc','abcd','abcde']
length = map(len,names)
for i in length:
        print(i)
for j in length:
        print(j)
#  Filter function
def is_even(a):
        return a%2 ==0
numbers = 3,4,2,1,5,6,9,8,10
evens =[]
evens = tuple(filter(is_even, numbers))
print(evens)
def is_odd(a):
        return a%2 !=0
odds =[]
odds = tuple(filter(is_odd, numbers))
print(odds)
# Iterator and Iterable
numbers = [1,2,3,4]
square = (map(lambda a: a**2,numbers))
number_Iter = iter(numbers)
print(next(number_Iter))
print(next(number_Iter))
print(next(number_Iter))
print(next(number_Iter))
# Iterable - List,Tuple,String          # Iterator - 
# Zip Function
user_id = ['user1','user2','user3']
name = ['Sourav','Rohit','Amit']
last_name = ['Biswas','Sharma','Saroj']
print(dict(zip(user_id,name,last_name)))

example =[('a',1),('b',2)]
print(dict(example))

l1 = [1,3,5,7]
l2 = [2,4,6,8]
l = [(1,2),(3,4),(5,6),(7,8)]
# *oparator with zip
new_list = []
for pair in zip(l1,l2):
        new_list.append(max(pair))
print(new_list)
# This is Challenge  # define a function take any number of lists containing number [1,2,3],[4,5,6],[7,8,9] # return average (1+4+7)/3,(2+5+8)/3,(3+6+9)/3
# Try to make this anonymous function in one line using Lambda
def average_finder(l1,l2):
        average = []
        for pair in zip(l1,l2):
                average.append(sum(pair)/len(pair))
        return average
print(average_finder([1,2,3],[4,5,6]))

def average_finder(*args):
        average = []
        for pair in zip(*args):
                average.append(sum(pair)/len(pair))
        return average
print(average_finder([1,2,3],[4,5,6],[7,8,9]))

average_finder = lambda *args : [sum(pair)/len(pair) for pair in zip (*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))
# All, Any function
number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5,6,7,8]
evens = []
for num in number1:
        evens.append(num % 2 == 0)
print(evens)
print(all([True, True, True, True, True]))
print(all([True, True, False, True, True]))
print(all([num % 2 == 0 for num in number1]))
print(any([num % 2 == 0 for num in number1]))

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return 'Wrong input'
print(my_sum(1,2,3,4,8.9))
print(my_sum(1,2,3,4,8.9,'Hanuman',['car','mat']))
# Advance min() and max()
def func(item):
        return len(item)
names = ['Sourav Biswas','Manoj','ab','z']
print(min(names, key = func))
print(max(names, key = lambda item : len(item)))

students1 = {
        'Himanshu' : {'score':90, 'age' : 24},
        'Manoj' : {'score':80, 'age' : 22},
        'Rohit' : {'score':77, 'age' : 23}
}
print(max(students1, key = lambda item : students1[item]['score']))

students2 = [
        {'name':'Himanshu','score':90, 'age' : 24},
        {'name':'Manoj','score':80, 'age' : 22},
        {'name':'Rohit','score':77, 'age' : 23}
]
print(max(students2, key = lambda item : item.get('score')))
print(max(students2, key = lambda item: item.get('age'))['name'])

# Advance Sorted key func
fruits = ['grape','mango','apple']
fruits.sort()
print(fruits)
sorted(fruits)
print(fruits)
print(sorted(fruits))

guitars = [
        {'model': 'Yamaha f310','price':8400},
        {'model': 'faith apollo venus','price':35000},
        {'model': 'taylor 814ce','price':450000},
        {'model': 'faith naptune','price':50000}
]
print(sorted(guitars, key = lambda d:d['price'],reverse = True))

# More about function           # What are doc srtrings         # how to write doc string       # what is help function
def add(a,b):
        return a+b
print(add.__doc__)
print(len.__doc__)
print(sum.__doc__)
help(sum)

# Ch - 14       # Decorator
# you have to a complete understanding of functions     # first class function/closures         # then finally we will learn about decorators
def square(a):
        return a**2
s = square
print(s(7))
print(list(map(square, numbers)))

def my_map(func, numbers):
        new_list =[]
        for item in l:
                new_list.append(func(item))
        return new_list
print(my_map(square,numbers))
print(list(map(lambda a:a**2,numbers)))

def my_map2(func,numbes):
        return[func(item) for item in numbers]
print(my_map2(lambda a:a**3,numbers))
# Function Return Function
def outer_func():
        def inner_func():
                print('inside inner func')
        return inner_func

def outer_func2(msg):
        def inner_func2():
                print(f'message is {msg}')
        return inner_func2
var = outer_func2('hello there !')
var()
# Function Return Function (Closure) Practice
def to_power(x):
        def calc_power(n):
                return n**x
        return calc_power
cube = to_power(3)
print(cube(4))
square = to_power(2)
print(square(4))

#  Decorators Intro      # Decorators - enhance the functionally of other function      # @ use for decorators
def decorator_function(any_function):
        def wrapper_function():
                print('this is awesome function')
                any_function()
        return wrapper_function
# This is awesome function
def func1():
        print('this is function1')
def func1():
        print('this is function2')
var = decorator_function(func1)
var()

from functools import wraps
def decorator_function(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs):
                '''this is wrapper function'''
                print('this is awesome function')
                return any_function(*args,**kwargs)
        return wrapper_function
# This is awesome function
@decorator_function
def func(a):
        print(f'this is function with argument {a}')
func(5)
@decorator_function
def add(a,b):
        return a + b
        '''this is add function'''
print(add(7,8))
print(add.__doc__)
print(add.__name__)

from functools import wraps
def print_function_data (function):
        @wraps(function)
        def wrapper(*args,**kwargs):
                print(f'you are calling {function.__name__}')
                print(f'{function.__doc__}')
                return function(*args,**kwargs)
        return wrapper
@print_function_data
def add(a,b):
        return a + b
print(add(4,9))

# Ex - 14 Decorator
from functools import wraps
import time
def Calculate_time(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            print(f'Executing .... {function.__name__}')
            t1 = time.time()
            returned_value = function(*args,**kwargs)
            t2 = time.time()
            total_time = t2 - t1
            print(f'This function took {total_time} seconds')
            return returned_value
        return wrapper
@Calculate_time
def square_finder(n):
        return [i**2 for i in range(1,n+1)]
square_finder(1000)
# Decorators Practice
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg) == int)
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print('Invalid Arguments')
        return wrapper
@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += 1
    return total
print(add_all(1,2,3,4,5,))
# Decorators Practice Short
from functools import wraps
def only_int_allow(function):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg) == int for arg in args]):
                return function(*args,**kwargs)
            print('Invalid Arguments')
        return wrapper
    return decorator
@only_int_allow(str)
def string_join(args):
    string = ' '
    for i in args:
        string += 1
    return string
print(string_join('Sourav','Biswas'))
# Ch - 15 Generators
# generator are iterators       # create your first generator with generator        # generator function        # generator comprehension

def nums(n):
    for i in range(1,n+1):
        print(i)
num(10)
def nums(n):
    for i in range(1,n+1):
        yield(i)
num(10)
for number in nums(10):
    print(number)
numbers = num(10)
for num in numbers:
    print(num)
for num in numbers:
    print(num)
    # Ch -15 Ex - 1     # define generator function # Take one number as argument   # Generate A sequence of even number 1 to that number
# 5 --> 2,4         # 7 --> 2,4,6
def even_generator(n):
    for num in range(1,n+1):
        if num % 2 == 0:
            yield(num)
for num in even_generator(20):
    print(num)
for num in even_generator(20):
    print(num)
def even_generator(n):
    for num in range(2,n+1,2):
        print(num)
even_num = even_generator(20)
for num in even_num:
    print(num)
# Generator Comprihension
square = (i**2 for i in range(1,11))
for num in square:
    print(num)
for num in square:
    print(num)
# List Vs Generators    # memory usage, time       # whento use list, when to use generator
l = [i**2 for i in range(10000000)]     # List
g = (i**2 for i in range(10000000))     # Generator
import time
t1 = time.time()
l = [i**2 for i in range(10000000)]
print(time.time() - t1)
t1 = time.time()
g = (i**2 for i in range(10000000))
print(time.time() - t1)
# Object Oriented Programming
# Common topic in almost all programming language (Python C++,Java) with common idea but with different syntax
# OPP is just a style way to write a code very helpful in creating real world programs
# Objectives    # What is class         # How to create an class        # What is init method
# What are Attributes, Instance variable        # How to create our object
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
print(p1.first_name)
print(p2.first_name)
# Ex - 1      # Create a laptop class with attributes like brand names, model name, price        # Create two object/intense of your laptop class
class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price
laptop = Laptop('hp','au114tx',63000)
print(laptop.name)
# Instance Method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
print(p2.full_name())
print(p2.is_above_18())
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
print(p2.full_name())
print(p2.is_above_18())
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
print(p2.full_name())
print(p2.is_above_18())

class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name
    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price
laptop1 = Laptop('hp','au114tx',63000)
laptop2 = Laptop('apple','macbook pro',230000)
print(laptop1.apply_discount(7))
print(laptop2.apply_discount(7))

class Circle:
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132806647093844609550582231725359408128481117450284102701938
    def __init__(self,radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius
c = Circle(4)
c1 = Circle(5)
print(c.calc_circumference())
print(c1.calc_circumference())

class Person:
    count_instance = 0
    def __init__ (self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Sourav', 'Biswas', 21)
p2 = Person('Sourav', 'Biswas', 21)
p2 = Person('Sourav', 'Biswas', 21)
print(Person.count_instance)

# Class methods         # Difference between class method instance methods
class Person:
    count_instance = 0      # class variable / class attribute
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def count_instance(cls):
        return  f'You have create {cls.count_instance} instance of {cls.__name__} class'
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
print(Person.count_instance())
                # Class Method As constructor
class Person:
    count_instance = 0      # class variable / class attribute
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    @classmethod
    def count_instance(cls):
        return  f'You have create {cls.count_instance} instance of {cls.__name__} class'
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Sourav','Biswas',21)
p2 = Person('Rupa','Biswas',19)
p3 = Person.from_string('Sourav,Biswas,21')
print(p3.full_name())
# Statics Method
class Person:
    count_instance = 0      # class variable / class attribute
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    @classmethod
    def count_instance(cls):
        return  f'You have create {cls.count_instance} instance of {cls.__name__} class'
    @staticmethod
    def hello():
        print('hello, static method called')
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price
    
    def make_a_call(self,phone_number):
        print(f'calling {phone_number} ...')

                # Encapsulation # Abstraction # Naming Convention # Name Mangling
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    def make_a_call(self,phone_number):
        print(f'calling {phone_number} ...')
    def full_name(self):
        return f'{self.brand}{self.model_name}'
    def send_message(self):
        pass          # twilio
phone1 = Phone('Nokia','1100',1000)
print(phone1.price)

