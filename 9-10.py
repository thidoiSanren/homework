# import pa
#
# me = pa.Admin('s', 'lb', '123')
# me.privileges.show_privileges()


from random import randint


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, 6)
        return x


die = Die()
x = die.roll_die()
print(x)
