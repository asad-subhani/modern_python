# per: float = float(input("Enter your percentage: "))

# if per<= 33:
#   print(f"Your percentage is {per} and your grade is 'F'")
# elif per<= 50:
#   print(f"Your percentage is {per} and your grade is 'D'")
# elif per<= 65:
#   print(f"Your percentage is {per} and your grade is 'C'")
# elif per<= 75:
#   print(f"Your percentage is {per} and your grade is 'B'")
# elif per<= 85:
#   print(f"Your percentage is {per} and your grade is 'A'")
# else:
#   print(f"Your percentage is {per} and your grade is 'A+'")

tags: list[str] = input("Enter tags , seperated: ").split(",")
print(list(i.strip() for i in tags))