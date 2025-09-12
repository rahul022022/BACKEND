try:
    f = open("testfile.txt", "r")   
    data = f.read()
    print("File contents:", data)

except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You don’t have permission to open this file.")
finally:
    try:
        f.close()
        print("File closed successfully.")
    except:
        print("File was never opened, so nothing to close.")
