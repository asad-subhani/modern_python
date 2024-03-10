guests : list[str] = ["Muhammad Ali", "Akash", "Bilal"]
for i in range(0,len(guests)-1):
    if guests[i] == "Akash":
        print(f"{guests[i]} is not joining us at dinner today.")
        guests[i] = "Ahad"

print("\n")
for index in guests:
    print(f"{index} still joinning us in the dinner.")