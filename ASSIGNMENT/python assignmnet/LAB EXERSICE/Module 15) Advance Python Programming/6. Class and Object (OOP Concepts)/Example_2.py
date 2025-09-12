# Program: Demonstrate local and global variables in a class


x = 100

class Demo:
    def show(self):
     
        y = 50
        print("Local variable y:", y)
        print("Global variable x (inside method):", x)

d = Demo()
d.show()

print("Global variable x (outside class):", x)
