
while True:
    print("Tell me two numbers, I will add them.")
    print('Input "q" can quit.')

    first_number = input("\nfirst number is :")
    if first_number == 'q':
        break
    second_number = input("\nsecond number is :")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('\nPlease input number, not str\n')
    else:
        print(answer)