"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("pi es un {} con un valor de {}".format(type(pi), pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i < 50: 
    print("i es menor de 50")
elif i > 50: 
    print ("i es mayor de 50")
else: 
    print("i es igual a 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
    print("Naranja")
elif picked_fruit == "strawberry":
    print("rojo")
else:
    print("amarillo")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplies(x,y):
    result = x * y
    return result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiplies(12,96))

print("48 x 17 =",multiplies(48,17))

print("196523 x 87323 =",multiplies(196523,87323))
