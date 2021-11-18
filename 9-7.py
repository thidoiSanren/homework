class User:
    def __init__(self, first_name, last_name, telephone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone_number

    def describe_user(self):
        print(self.first_name, self.last_name, int(self.telephone))

    def greet_user(self):
        print("hello, " + str(self.first_name) + str(self.last_name))


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post']

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, telephone):
        super().__init__(first_name, last_name, telephone)
        # self.privileges = ['can add post', 'can delete post']
        self.privileges = Privileges()


me = Admin('s', 'lb', '18158513611')
# me.show_privileges()
# me.describe_user()
me.privileges.show_privileges()