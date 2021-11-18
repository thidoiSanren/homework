# def make_sandwich(*toppings):
#     print(toppings)
#
#
# make_sandwich('a', 'b', 'v')


def cars_message(maker, number, **toppings):
    files = {}
    files['maker'] = maker
    files['number'] = number
    for key, value in toppings.items():
        files[key] = value
    return files


# car = cars_message('Jiben', '2-',
#                    color='red', para='lunzi')
# print(car)
