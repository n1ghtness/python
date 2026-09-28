grade = float(input("Enter the student's grade (0 to 10): "))
if grade > 10:
    print("Invalid grade")
elif grade >= 7 and grade <= 10:
    print("Passed")
elif grade < 7 and grade >= 5:
    print("Recovery exam!")
else:
    print("Failed!")