magicians = ['jason', 'lol', 'alice']
lists = []

def show_magicians(magicians):
    print(magicians)


def make_great(list):
    while list:
        magician = 'the great ' + list.pop()
        lists.append(magician)
    return lists
lists = make_great(magicians)
show_magicians(lists)
