# prompt = "\nWe will give you this."
# prompt = "\nwhat:"
# message=''
# while message != 'quit':
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

age = "Tell me your age: "
message = ''
active = True
while active:
    message = input(age)
    if message == 'quit':
        break
    elif int(message) < 3:
        print("free")
    elif int(message) <= 12:
        print(10)
    elif int(message) > 12:
        print(15)
