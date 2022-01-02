# Task 4
# The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

# Завдання 4
# Програма математичної вікторини
# Напишіть програму, яка запитує відповідь на математичний вираз, перевіряє, чи правий користувач чи ні, а потім відповідає відповідним повідомленням.

from math import sqrt
try:
    side_triangle = float(input('Enter the side of the equilateral triangle: '))
except ValueError:
    print("Error,please enter number,if it is not an integer, use a point to separate")


def area_equl_triangle(a):
    height = (a*sqrt(3))/2
    square = (0.5*a*height).__round__(2)
    return square


rez = area_equl_triangle(side_triangle)
user_rez = float(input("Enter your result,like-(0.03): "))
if user_rez - rez <= 2:
    print("almost correct")
elif rez != user_rez:
    print("you are wrong")
print("The area of an equilateral triangle", rez)
print()

