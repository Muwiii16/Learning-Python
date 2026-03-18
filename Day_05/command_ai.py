user_status = input("Are you and Admin or a User?: ")
clean_status = user_status.strip().lower()

command = input("Select a command:\n1.Status\n2.Reboot\n3.Hello\n---> ")
clean_command = command.strip().lower()

if clean_command == "status":
    print("All systems are operational.")
elif clean_command == "reboot":
    if clean_status == "admin":
        print("Rebooting the system...")
    else:
        print("Access Denied: Admin privileges required.")
elif clean_command == "hello":
    print("Hi there!")
else:
    print("Command not recognized.")
