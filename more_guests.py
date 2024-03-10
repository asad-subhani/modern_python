import math
# we got the following list from last program after changing the missing guest with new one
guests : list[str] = ["Muhammad Ali", "Ahad", "Bilal"]

for i in guests:
    print(f"{i} We got a bigger table and have space for more guests")

guests.insert(0, "Usman")
guests.insert(math.floor(len(guests)/2), "Ashraf")
guests.append("Zia Ullah")

print("\n")
for i in guests:
    print(f"{i}, You're invited for dinner tonight.")


print(guests)
