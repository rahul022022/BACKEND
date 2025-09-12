import re

text = "Python programming is powerful"

# Search for the word 'programming'
match = re.search(r"programming", text)

if match:
    print("Word found at position:", match.start())
else:
    print("Word not found")
