salary= input("salary: ")
salary= float(salary)

if salary <= 4999.99:
    print("income tax: ", 0)
    
if salary >= 5000 and salary <= 9999.99:
    print("income tax",salary * 0.06)

if salary >= 10000 and salary <= 19999.99:
    print("income tax: ", salary * 0.15)

if salary >= 20000 and salary <= 29999.99:
    print("income tax: ", salary * 0.2)

if salary >= 30000 and salary <= 39999.99:
    print("income tax: ", salary * 0.25)

if salary >= 40000:
    print("income tax: ", salary * 0.3)
