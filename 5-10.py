current_users = ['slb', 'qy', 'syq', 'mfq', 'skl', 'admin']
new_users = ['slb', 'zh', 'lh', 'lh', 'lch', 'xsb']
for user in new_users:
    if user in current_users or user.upper() in current_users:
        print('The user has been used!')
    else:
        print('You can use this name!')  
