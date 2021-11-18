# def display_message():
#     print("what")
# display_message()

# def make_shirt(size, graph='I love python'):
#     print("The size of shirt is " +str(size))
#     print("This shirt has the graph of " + str(graph))
# make_shirt(34)

def make_album(name, music,number=''):
    if number:
        album = {'name': name, 'music': music, 'number': number }
    else:
        album = {'name': name, 'music': music }
    return album

while True:
    name = input("please input singer name:")
    if name == 'q':
        break
    music = input("Please input the name of the music:")
    if music == 'q':
        break
    number = input('Please input the number of music:')
    if number == 'q':
        break
    album = make_album(name, music,number=int(number))
    print(album)