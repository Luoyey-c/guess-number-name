print('这是一个在0-100的猜数字小游戏')
import random
num =  random.randint(1,100)
while True:
    try:
        guess = int(input("输入数字:"))
        if guess < 0:
            print('你输入的数字不在范围内')
        elif guess > 100:
            print('你输入的数字不在范围内')
        else:
            if guess == num:
                    print('你猜对了')
                    break
            elif guess < num:
                    print("你猜小了")
            elif guess > num:
                    print('你猜大了')
    except ValueError:
        print('请输入有效数字')