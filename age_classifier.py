idade = float(input("Enter your age:"))
if idade <= 0 or idade > 130:
    print("Invalid age")
elif idade <= 11:
    print("Child")
elif idade <= 17:
    print("Teenager")
elif idade <= 59:
    print("adult")
elif idade <= 130:
    print("Senior")