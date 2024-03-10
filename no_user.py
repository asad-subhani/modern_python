user_names: list[str] = []

if (len(user_names) == 0):
        print("We need to find some users!")
else:
    for user in user_names:
        if user.lower() == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")