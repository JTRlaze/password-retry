password = '123qwe'
x = 1
while x <= 3:
    user = input('請輸入密碼:')
    if user == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤! 還有{}次機會'.format(3-x))
    x = x + 1
