#for loop 
#Lab 11.12 PROJECT Password Creator

import random

capital_let = "QWERTYUIOPASDFGHJKLZXCVBNM"
small_let = "qwertyuiopasdfghjklzxcvbnm"
numbers = "0123456789"
special_char = "?,.<>!%$][]{*#@}"

upper, lower, digits, odd = True, True, True, True

finalpass = ""

if upper:
    finalpass += capital_let
if lower: 
    finalpass += small_let
if digits:
    finalpass += numbers 
if odd:
    finalpass += special_char

length = 15
howmuch = 3

for x in range(howmuch):
    password = "".join(random.sample(finalpass,length))
    print(password)


