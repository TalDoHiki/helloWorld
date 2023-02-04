# print("Te amo")
# print("Akemin!")

# fn = "Felpe"
# ln = "Hikimin"
# fl = fn+" "+ln
# print("Hello "+fl)

# n = input("What's your name?: ")
# age = int(input("How old are you?: "))
# print("Hello "+n)
# print("You're "+str(age)+" years old, cool!")
# if(int(age)<18):{
# print("But that's a shame, you're a minor, "+n)
# }

# import math
# import time

# n = input("What's the square of 4?: ")
# if(int(n)==2):
#    print("Good, you're right!")
# else:
#    print("Damn, you miss :(")

# website = "http://google.com"
# slice = slice(7,-4)
# print(website[slice])

 age = int(input("How much older are you?: "))
 if age>=100:
   age = (age/100)
   print("You're ",str(age)," century(ies) old!")
 elif age>=18:
    print("You're an adult!")
 else:
    print("You're a child!")

# name = None
# while not name:
#    name = input("Enter your name: ")
# print ("Hello "+name)
# for i in range(10):
#    print(i+1)
# for i in range(50,100+1,2):
#    print(i)
# for i in "Felpe":
#    print(i)


# for seconds in range(0,60,1):
#    time.sleep(0)
#    print(hours,":",minutes,":",seconds)
# if seconds == 60:
#    minutes + 1
# if minutes == 60:
#    minutes = 0
#    hours = 1
# if hours == 1:
#    seconds = minutes = hours = 0

# rows = int(input("How many rows?: "))
# columns = int(input("How mane columns?: "))
# symbol = input("Enter a symbol to use: ")
# for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

# while True:
#    name = input("Enter your name: ")
#    if name !="":
#        break

# ph = "423-4126-7890"
# for i in ph:
#    if i == "-":
#        continue
#    print(i, end="")

# food = ["pizza","hamburger","hotdog","spaghetti"]
# for x in food:
#    print(x, end=", ")

# drinks = ["coffee","soda","tea"]
# dinner = ["rice", "pizza"]
# dessert = ["cake","ice cream"]
# food = [drinks,dinner,dessert]
# print(food[2])

# def hello():
#    print("aaaa!")
#   print("bbbbb!")
# hello()

# def multiply(n1,n2):
#    result = n1 * n2
#    return result
# x = multiply(6,8)
# print(x)

# def hello(first,middle,last):
#    print("Hello, "+first+" "+middle+" "+last)
# hello(last="ok",middle="am",first="I")

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# n = 1000
# print("The number is {:.3f}".format(n))
# print("The number is {:,}".format(n))
# print("The number is {:b}".format(n))
# print("The number is {:o}".format(n))
# print("The number is {:X}".format(n))
# print("The number is {:E}".format(n))

# import random
# x=random.randint(1,6)
# y=random.random()
# myList = ['rock','paper','paper','scissors']
# z = random.choice(myList)
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","Ace"]
# random.shuffle(cards)
# print(cards)

# try:
#    num = int(input("Enter a number to divide: "))
#    den = int(input("Enter a number to divide by: "))
#    result = num / den
#    print(result)
# except ZeroDivisionError:
#    print("Dude... It's zero")
# except ValueError:
#    print("Only numbers, plz")
# except Exception:
#    print("something went wrong :(")
# finally:
#    print("This is absolute")

# import os
# path = "C:\\Users\\guear\\Documents\\Code"
# if os.path.exists(path):
#    print('Tha locations exists!')
#    if os.path.isfile(path):
#        print("That is a file")
#    elif os.path.isdir(path):
#        print("That is a directory!")
# else:
#    print("That location doesn't exist!")

# try:
#    with open('a.txt') as file:
#        print(file.read())
# except FileNotFoundError:
#    print("The file has not found")

# text = input("Tell what you're thinking: ")
# with open('a.txt','w') as file:
#    print(file.write(text))

# import shutil
# shutil.copy2('a.txt','copy.txt')

