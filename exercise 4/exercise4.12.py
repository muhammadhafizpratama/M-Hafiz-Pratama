friends_pizzas = ['pepperoni', 'cheese', 'veggie']
my_pizzas = friends_pizzas[:]

my_pizzas.append('pineapple')
friends_pizzas.append('sausage')

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
