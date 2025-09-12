import random

print("Random number between 1 and 100:", random.randint(1, 100))

# Generate 5 random numbers between 1 and 100
print("Five random numbers between 1 and 100:")
for _ in range(5):
    print(random.randint(1, 100))
