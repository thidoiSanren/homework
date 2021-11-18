import json

def get_number():
    filename = 'numbers.json'
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number

def tell_number():
    yournumber = get_number()
    if yournumber:
        print("Your numeber is :" + yournumber)
    else:
        yournumber = input("Tell me your number:")
        filename = 'numbers.json'
        with open(filename, 'w') as file:
            json.dump(yournumber, file)
            print("We will remeber your number " + yournumber)

tell_number()
