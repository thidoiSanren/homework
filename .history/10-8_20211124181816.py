def open_files(filename):
    """open files 打开文件"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print("The file is ont found!")
        pass
    else:
        print(contents)


files = ['cats.txt', 'guest.txt']
for file in files:
    open_files(file)

