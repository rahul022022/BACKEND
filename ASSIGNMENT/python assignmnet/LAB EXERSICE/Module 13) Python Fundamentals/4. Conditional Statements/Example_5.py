# A = int(input("Enter A Number -> "))
# B = int(input("Enter B Number -> "))

# if A>B:
#     print("A is greater number")
# else:
#     print("B is less number")

# if A<B:
#     print("B is greater number ")
# else :
#     print("A is less number")


num = int(input("Enter a number -> "))
num_check= int(input("Enter number check -> "))

if num>num_check:
    print(f"{num} is greater then {num_check}")

elif num<num_check:
    print(f"{num_check} is greater then {num}")

else:
    print(f"{num} is equal to {num_check}")