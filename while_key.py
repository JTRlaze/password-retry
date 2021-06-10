password = '123qwe'
i = 3
x = 1
while x <= 3:
    user = input('請輸入密碼:')

    if user == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤! ')
        if 3-x > 0:
            print('還有{}次機會'.format(3-x))
        else:
            print('嘗試太多次失敗 請五分鐘後再試')
    x = x + 1
