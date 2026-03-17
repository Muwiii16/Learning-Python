user_password = input("Please enter your password: ")
clean_password = user_password.strip()

if clean_password == "admin":
    print("Access Granted: Welcome back.")
else:
    print("Access Denied: Incorrect password.")
