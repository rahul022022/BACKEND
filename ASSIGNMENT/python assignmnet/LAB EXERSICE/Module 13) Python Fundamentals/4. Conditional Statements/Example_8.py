'''
Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
using a nested if.
'''
name = input("Enter your name -> ")
age = int(input("Enter your Age -> "))
weight = float(input("Enter your Weight -> "))

if age>=18:
    if weight>=60:
        print(f"{name} Your eligible for blood donate")

    else:
        print(f"{name}So sorry your weight is low for blood donate")
else:
    print(f"{name}Your not eligible for blood donate due to age")