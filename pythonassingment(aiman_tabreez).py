# -*- coding: utf-8 -*-
"""PythonAssingment(Aiman Tabreez).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EIk3mFtwKKfvCetEd3qGfEBdAsaDf-Aq
"""

import math
a = int(input("Enter The Number:"))
b = int(input("Enter The Number:"))
def Addition(a,b):
    sum = a+b
    return sum
def Subtraction(a,b):
    sub = a-b
    return sub
def Multiplication(a,b):
    mul = a*b
    return mul
def Division(a,b):
    div = a/b
    return div
def Square(a):
    s = a**2
    return s
def SquareRoot(a):
    sr = math.sqrt(a)
    return sr
def x(a):
    n = 1/a
    return n
choice =1 
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. 1/Any Number")

    choice=int(input("Enter choice: "))
    if choice==1:
        print(Addition(a,b))
    elif choice==2:
        print(Subtraction(a,b))
    elif choice==3:
        print(Multiplication(a,b))
    elif choice==4:
        print(Division(a,b))
    elif choice==5:
        print(Square(a))
    elif choice==6:
        print(SquareRoot(a))
    elif choice==7:
        print(x(a))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!")