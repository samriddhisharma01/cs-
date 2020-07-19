# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input("Enter a number: "))
if n>0:
    print(f"{n} is positive")
elif:
    print(f"{n} is negative")
else:
    print("the number is zero")
    
n=int(input("Enter a number: "))
if n!=0:
    if n>0:
        print(f"{n} is positive")
    else:
        print(f"{n} is negative")
else:
    print("the number is zero")
    
n=int(input("Enter a number: "))
if n%2==0:
    print(f"[n] is even")
else:
    print(f"[n] is even")
    
n=int(input("Enter a year: ")) 
if n%4==0:
    print("it is a leap year")
else:
    print("it's not a leap year")
    
n=int(input("Enter your marks: "))   
if n<60:
    print("your grade is F")
elif n in range(60,70):
    print("your grade is D")
elif n in range(70,80):
    print("your grade is C")
elif n in range(80,90):
    print("your grade is B")
elif n>90:
    print("your grade is A")