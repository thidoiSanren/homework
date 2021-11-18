pizzas = ['KFC', 'M', 'DE']
for pizza in pizzas:
    print('I like ' + pizza + '.')
print("I really like pizzas!")
friend_pizza = pizzas[:]
pizzas.append('Bi')
friend_pizza.append('Han')
print('My favourite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are: ")
for pizza in friend_pizza:
    print(pizza)