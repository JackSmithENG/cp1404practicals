for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Printing stars in a straight line
stars = int(input("Number of stars: "))

for i in range(0, stars, 1):
    print("*", end=" ")
print()
print()

# Star pyramid
counter = 0
for i in range(stars + 1):
    for j in range(i):
        print("*", end=" ")
    print()
