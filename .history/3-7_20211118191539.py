peoples = ['a', 'b', 'c', 'd']
# for i in range(4):
#     print(peoples[i] + ',' + 'welcome to my party')
# print("Oh, I'm sorry to hear that " + peoples[0] + " can't come here!")
peoples[0] = 'e'
peoples.insert(0, 'wdnmd')
peoples.insert(3, 'haha')
peoples.append('duca')
for i in range(6):
    print(peoples[i])
one = peoples.pop(0)
two = peoples.pop(5)
for i in range(4):
    print('and' + peoples[i])
del peoples[0]
del peoples[0]
del peoples[0]
del peoples[0]

print(peoples)
