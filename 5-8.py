# users = ['slb', 'qy', 'syq', 'mfq', 'skl', 'admin']
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello, " + user + "!")
else:
    print("We need to find some users!")