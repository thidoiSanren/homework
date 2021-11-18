while True:
    user_name = input("Tell me what is your name?")
    if user_name == 'quit':
        break
    else:
        print("Hello, " + user_name)

    with open('guest.txt', 'a') as guest:
        guest.write(user_name + '\n')
