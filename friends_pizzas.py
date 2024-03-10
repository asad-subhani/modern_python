pizzas : list[str] = ['Crown Crust', 'Pepperoni', 'Double Cheese']
friends_pizzas: list[str] = pizzas [:]

friends_pizzas.append("vegitarian Extra")
pizzas.append("Non Vegitarian")

print("Pizzas in 'pizzas' list are:")
for i in pizzas:
    print(i)


print("\nPizzas in 'friends_pizzas' list are:")
for i in friends_pizzas:
    print(i)


