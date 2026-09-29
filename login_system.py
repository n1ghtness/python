username = "n1ghtness"
password = "123456"
login_username = input("Enter your login: ")
login_password = input("Enter your password: ")
if login_username == username and login_password == password:
    print("Login successful!")
elif login_username != username and login_password == password:
    print("Incorrect username.")
elif login_username == username and login_password != password:
    print("Incorrect password.")
else: 
    print("Incorrect username and password.")