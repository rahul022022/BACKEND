# String manipulation using methods

text = "   hello world from python   "

print("Original String:", text)
print("Stripped String:", text.strip())           # remove spaces
print("Uppercase:", text.upper())                 # HELLO WORLD...
print("Lowercase:", text.lower())                 # hello world...
print("Title Case:", text.title())                # Hello World From Python
print("Replace 'python' with 'programming':", text.replace("python", "programming"))
print("Does string start with '   h'?:", text.startswith("   h"))
print("Split into words:", text.split())          # list of words
print("Join words with '-':", "-".join(text.split()))
print("Count of 'o':", text.count("o"))
