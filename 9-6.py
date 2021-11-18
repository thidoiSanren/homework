class Restaurant:
    """
    Some message about the restaurant
    """

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of this restaurant is " + self.restaurant_name)
        print("The type of this restaurant is  " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, name, type, list):
        super(IceCreamStand, self).__init__(name, type)
        self.flavors = list

    def tell_flavors(self):
        print(self.flavors)


icecream = IceCreamStand('demaxiya', 'Amer', ['hagendasi', 'aioiuniyta'])
icecream.tell_flavors()
