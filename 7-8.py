sandwich_orders = ["a", 'pastrami', 'b', 'pastrami', 'c', 'pastrami']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#
#     print("I made your tuna sandwich!")
#     finished_sandwiches.append(sandwich)
# for sandwich in finished_sandwiches:
#     print(sandwich)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)