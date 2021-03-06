"""
birthday.py
Author: Suhan
Credit: None
Assignment: Birthday

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name=input("Hello, what is your name? ")
month=input("Hi {0}, what was the name of the month you were born in? ".format(name))
month = month.lower()
year=int(input("And what year were you born in, {0}? ".format(name)))
day=int(input("And the day? "))

winter=['december', 'january', 'february']
spring=['march','april','may']
summer=['june','july','august']
fall=['november','september','october']

twenties=list(range(2000,2999,1))
nineties=list(range(1990,1999,1))
eighties=list(range(1980,1989,1))
stone=list(range(0,1979,1))

if month== "october" and day==31:
    print("You were born on Halloween!")
elif month=="september" and day==18:
    print("Happy birthday!")

elif month in winter and year in twenties:
    print("{0}, you are a winter baby of the two thousands.".format(name))
elif month in spring and year in twenties:
    print("{0}, you are a spring baby of the two thousands.".format(name))
elif month in summer and year in twenties:
    print("{0}, you are a summer baby of the two thousands.".format(name))
elif month in fall and year in twenties:
    print("{0}, you are a fall baby of the two thousands.".format(name))

elif month in winter and year in nineties:
    print("{0}, you are a winter baby of the nineties.".format(name))
elif month in spring and year in nineties:
    print("{0}, you are a spring baby of the nineties.".format(name))
elif month in summer and year in nineties:
    print("{0}, you are a summer baby of the nineties.".format(name))
elif month in fall and year in nineties:
    print("{0}, you are a fall baby of the nineties.".format(name))

elif month in winter and year in eighties:
    print("{0}, you are a winter baby of the eighties.".format(name))
elif month in spring and year in eighties:
    print("{0}, you are a spring baby of the eighties.".format(name))
elif month in summer and year in eighties:
    print("{0}, you are a summer baby of the eighties.".format(name))
elif month in fall and year in eighties:
    print("{0}, you are a fall baby of the eighties.".format(name))

elif month in winter and year in stone:
    print("{0}, you are a winter baby of the Stone Age.".format(name))
elif month in spring and year in stone:
    print("{0}, you are a spring baby of the Stone Age.".format(name))
elif month in summer and year in stone:
    print("{0}, you are a summer baby of the Stone Age.".format(name))
elif month in fall and year in stone:
    print("{0}, you are a fall baby of the Stone Age.".format(name))