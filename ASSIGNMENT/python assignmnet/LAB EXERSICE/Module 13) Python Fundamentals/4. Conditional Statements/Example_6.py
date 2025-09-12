n = int(input("Enter NUmber  N ->  "))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        print(f"{n} Number is prime")
        break
else:
    print(f"{n}-Number is not prime")