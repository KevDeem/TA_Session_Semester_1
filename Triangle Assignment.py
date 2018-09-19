number = int(input("Input number here: "))

y=1
while y < number:
    print("*" * y)
    y = y + 1

print("")

y=1
while y < number:
    print(" " * (number - y) + "*" * (y))
    y = y + 1

print("")

y = 1
while y< number:
    print(" " * y + "*" * (number - y))
    y = y + 1

print("")

y = 1
while y < number:
    print("*" * (number - y))
    y = y + 1

print("")

y = 1
while y < number:
    print(" " * (number - y) + "*" * (y + (y-1)))
    y = y + 1

print("")

y = 1
while y < number:
    print(" " * (number - y) + "*" * (y + (y-1)))
    y = y + 1

x = 1
while x < number:
    print(" " * (x) + "*" * (number - x) + ("*" * (number - x - 1)))
    x = x + 1
