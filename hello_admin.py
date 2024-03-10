user_names: list[str] = ["Asad", "Muhammad Ali", "Admin", "Shehrooz", "Afzal"]

for user in user_names:
    if user.lower() == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")