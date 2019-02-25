def count_login():
    password = input()
    if password == '12345':
        print('enter login ')
    else:
        print('flase,please input again')
    count_login()
count_login()
