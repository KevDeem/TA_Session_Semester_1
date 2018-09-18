name = input("name: ")
number = input("number: ")
total = input("total sales($): ")

total = int(total)

print("name: ", name)
print("number: ", number)
print("total sales($)", total)


if total <= 200:
    print("commision($)", total * 0.05)

if total >= 200.01 and total <= 1000:
    print("commision($): ", (200 * 0.05) + ((total - 200) * 0.08))

if total >= 1000.01 and total <=2000:
    print("commision($)", (200 * 0.05) + ((1000 - 200) * 0.08) + ((total - 1000) * 0.1))

if total >= 2000.01:
    print("commision($)", (200 * 0.05) + ((1000 - 200) * 0.08) + ((1000) * 0.1) + (total - 2000) * 0.12)
