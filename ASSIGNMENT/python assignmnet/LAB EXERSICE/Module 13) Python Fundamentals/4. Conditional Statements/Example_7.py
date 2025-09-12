'''
Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder. 
'''

percentage = float(input("Enter your percentage -> "))

if percentage >= 90:
    print("congratulations you got *A+*")

elif percentage >= 80:
    print("A Grade")

elif percentage >= 60:
    print("B Grade")

elif percentage >= 40:
    print("C Grade")

else:
    print("Fail")