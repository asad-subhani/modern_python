# we got the following list from last program after adding new guests.
guests : list[str] = ['Usman', 'Muhammad Ali', 'Ashraf', 'Ahad', 'Bilal', 'Zia Ullah']

for i in range(0, len(guests)-2):
    removed_guest: str = guests.pop()
    print(f"{removed_guest} we are sorry but you can't join us tonight.")

print ("\n")
for rem in guests:
    print(f"{rem} You're still invited for dinner tonight.")
print(guests)
del guests[1]
del guests[0]
print(guests)