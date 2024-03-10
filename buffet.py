menu:tuple[str, str, str, str, str] = ('Chicken Biryani', 'Beaf Palao', 'Kabuli Palao', 'Achari Biryani', 'Sweet Rice')
print("Restorant offers these dishes:\n")
for i in menu:
    print(i)

# menu[3] = 'Afgani Palao'

menu1:tuple[str, str, str, str, str] = ('Chicken Biryani', 'Beaf Palao', 'Afgani Palao', 'Achari Biryani', 'Zarda Rice')
print("\nNew Updated menu is:")
for i in menu:
    print(i)