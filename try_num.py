import random
r = random.randint(1,100)
l = 1
t = 100

while True:
    print('來猜個數字吧！', l,'~', t)
    num = input('請輸入數字： ')
    num = int(num)
    if r == num:
        print('哇！猜對了，數字為', r)
        break
    elif num < r and num < 101:
        if num > l:
            l = num
            print('數字猜大一點')
        else:
            print(l, '以下不用猜了哦！')

    elif num > r and num < 101:
        if num < t:
            t = num
            print('數字猜小一點')
        else:
            print(t, '以上不用猜了哦q_q')

    elif num > 101:
        print('你猜過頭了吧')