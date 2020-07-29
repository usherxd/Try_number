import random
print('來猜大小吧！')
hh = input('請輸入上限值： ')
lw = input('請輸入下限值： ')
hh = int(hh)
lw = int(lw)

r = random.randint(lw,hh)
l = lw
t = hh
count = 0

while True:
    count += 1
    print('來猜個數字吧！', l,'~', t)
    num = input('請輸入數字： ')
    num = int(num)
    if r == num:
        print('哇！猜對了，數字為「', r, '」，總共猜了', count, '次！')
        break
    elif num < r and num < (hh + 1):
        if num > l:
            l = num
            print('數字猜大一點')
        else:
            print(l, '以下不用猜了哦！')

    elif num > r and num < (hh + 1):
        if num < t:
            t = num
            print('數字猜小一點')
        else:
            print(t, '以上不用猜了哦q_q')

    elif num > 101:
        print('你猜過頭了吧')

    print('這是你猜的第', count, '次')