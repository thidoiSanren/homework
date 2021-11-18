class User:
    def __init__(self, first_name, last_name, telephone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone_number

    def describe_user(self):
        print(self.first_name, self.last_name, int(self.telephone))

    def greet_user(self):
        print("hello, " + str(self.first_name) + str(self.last_name))


Me = User('slb', 'lb', '18158513611')
Me.describe_user()
Me.greet_user()
