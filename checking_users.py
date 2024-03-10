user_names: list[str] = ["Asad", "Muhammad Ali", "Admin", "Shehrooz", "ARFAN"]
new_users: list[str] = ["asad", "Subhani", "ADMIN", "Sharukh", "Arfan"]

user_lower: list[str] = [i.lower() for i in user_names]


for user in new_users:
    if user.lower() in user_lower:
        print("You have to enter different user name!")
    else:
        print("Valid Username")