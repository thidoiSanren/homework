from use import User


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