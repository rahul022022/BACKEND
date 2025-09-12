import re

text = "Python is easy to learn"

# Try to match at the beginning
match = re.match(r"Python", text)

if match:
    print("Match found at the beginning:", match.group())
else:
    print("No match at the beginning")
